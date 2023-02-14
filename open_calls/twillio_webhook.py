import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists


from tools.logging import logger
from things.actors import actor


import re
import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('photo_text_response_test.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


def handle_request():
    logger.debug(request.form)

    act = None
    if exists( f"users/{request.form['From']}.pkl") :
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p) 
    else:
        act= actor(request.form['From'])

    act.save_msg(request.form['Body'])
    logger.debug(act.prev_msgs)
    

    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    response = 'NOT FOUND'

    sent_input = str(request.form['Body']).lower()
    resp_str = CORPUS['input'][sent_input]
    print(resp_str)

    if sent_input in CORPUS['input']:
        response = CORPUS['input'][sent_input]['content'] # Will error check for blank responses at sending time
        if CORPUS['input'][sent_input]['q_send_photo']: # This goes directly to a true/false
            img_url = (CORPUS['input'][sent_input]['photo_url'])
        else: # Not everything will have a url, will error check for blank at sending
            img_url = ''
        #commenting old code out below, so it's there for reference
        #if(re.match(r'.png',resp_str)): #if response will be an image
        #    print("inside regex logic")
        #    response.media(resp_str) #call png file from repo and send it as media
        #else:
        #    response = random.choice(CORPUS['input'][sent_input]) #normal text response
    else:
        CORPUS['input'][sent_input] = ['DID NOT FIND']
    #    with open('chatbot_corpus.json', 'w') as myfile: # Commented out for now
    #        myfile.write(json.dumps(CORPUS, indent=4 ))

    #response.media("Shimae-naga_joy.png") #add picture

    logger.debug(response)

    if img_url is not '':  # Image version
        message_img = g.sms_client.messages.create(
            body=response,
            from_=yml_configs['twillio']['phone_number'],
            media_url=image_url,
            to=request.form['From']
        )
    else:  # Sends no image
        message = g.sms_client.messages.create(
            body=response,
            from_=yml_configs['twillio']['phone_number'],
            to=request.form['From'])

    return json_response( status = "ok" )




