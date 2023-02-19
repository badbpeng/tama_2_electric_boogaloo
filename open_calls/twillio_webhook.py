import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists


from tools.logging import logger
from things.actors import actor


import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file: #configuration file
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

#this file is what is used for the dialogue response
with open('Lily_Chatbot.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


#function interacts with sender by responding
def handle_request():
    logger.debug(request.form)

    #if the phone number associated with the user has a history, it is contained in the pickle
    #file named after their phone number.  The following opens the pickle if it exists otherwise it
    #makes a new actor
    act = None
    if exists( f"users/{request.form['From']}.pkl") :
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p) 
    else:
        act= actor(request.form['From'])

    act.save_msg(request.form['Body']) #save msg to actor
    logger.debug(act.prev_msgs) #logger logs the interactions to the console, providing better visibility
    

    #dump the message history to the pickle
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    #response intialized to not found, will be overwritten if response is found in the dialogue json
    response = 'NOT FOUND'

    #get the input sent by the user and try to match it to json, otherwise dump to json file with not found msg
    sent_input = str(request.form['Body']).lower()
    if sent_input in CORPUS['input']:
        response = random.choice(CORPUS['input'][sent_input])
    else:
        CORPUS['input'][sent_input] = ['DID NOT FIND']
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))

    logger.debug(response)#logger shows the response to the console

    #send the message to the user, not the URL.  This is how you send photos.
    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     media_url=['http://54.67.106.33/static/Shimae-naga_joy.png'],
                     to=request.form['From'])
    return json_response( status = "ok" )


