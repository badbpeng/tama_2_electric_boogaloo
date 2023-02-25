import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists


from tools.logging import logger
from things.actors import actor
from things.User import User


import random
import json
import pickle

yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}


def handle_request():
    logger.debug(request.form)

    act = None
    if exists( f"users/{request.form['From']}.pkl") :
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p) 
    else:
        act= User(request.form['From'])

    act.save_msg(request.form['Body'])
    logger.debug(act.prev_msgs)


    response = ['NOT FOUND']
    #media = []
    response, media = act.get_output(request.form['Body']) 
    print("in twillio webhook")
    print(response)
    logger.debug(response)

    if len(media) != 0:  # Image sends first
        message = g.sms_client.messages.create(
            media_url=media,
            from_=yml_configs['twillio']['phone_number'],
            to=request.form['From'])

    for resp in response:
        if resp != '': # Text sends second
            message = g.sms_client.messages.create(
                body=resp,
                from_=yml_configs['twillio']['phone_number'],
                to=request.form['From'])
    # if response == '' and img_url == '':
    #     message = g.sms_client.messages.create(
    #         body='ERROR',
    #         from_=yml_configs['twillio']['phone_number'],
    #         to=request.form['From'])

    
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    #Need to think about how pickle will work, separate pickles hold text history and pet state?  All in one?  Would that make retreiving a pet more difficult?


    return json_response( status = "ok" )