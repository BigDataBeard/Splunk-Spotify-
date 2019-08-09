
# encoding = utf-8

import os
import sys
import time
import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # client_id = definition.parameters.get('client_id', None)
    # client_secret = definition.parameters.get('client_secret', None)
    pass

def collect_events(helper, ew):
   #account = helper.get_user_credential_by_username("client_id")
   #account = helper.get_user_credential_by_id("client_secret")
    #helper.log_info(dir(helper))
    #print(dir(helper))
    stanza = helper.get_input_stanza()
    #for blah in stanza:
        
    #event = helper.new_event(source="blah", index="main", sourcetype="asdf", data=json.dumps(stanza))
    #ew.write_event(event)
    
    client_id = helper.get_input_stanza()["test"]["client_id"]
    username = helper.get_input_stanza()["test"]["username"]
    client_secret = helper.get_input_stanza()["test"]["client_secret"]
    
    #client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    #sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    #playlists = sp.current_user_playlists()
    test = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, "http://localhost/", state=None, scope=None, cache_path=None, proxies=None)
    
    
    scope = 'user-library-read'
    #event = helper.new_event(source="blah", index="asdf", sourcetype="asdf", data=test.get_access_token("BQDlnwaAh3uAcSKtdWZr08XoRiDAxCwzm6XanwYiQ5ceUBUSRBps4TQfknaOHj6m0dieYsvCGnOKu6z0Nwypic4PRB_WXNVYbnxDm2vt1f-YqVeJ6yJhLdjckefg_VixghTC3UvpYxhzoAFI9zfNp6XDc-808EV_UaJ3gV8"))
    #ew.write_event(event)
    
    
    #token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost/')
    token = helper.get_input_stanza()["test"]["oauth"]
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playing_track()
        event = helper.new_event(source="blah", index="main", sourcetype="asdf", data=json.dumps(results))
        ew.write_event(event)
        #for item in results['items']:
        #    #track = item['track']
        #    event = helper.new_event(source="blah", index="asdf", sourcetype="asdf", data=json.dumps(item))
        #    ew.write_event(event)
            #print track['name'] + ' - ' + track['artists'][0]['name']
    else:
        print "Can't get token for", username
        
        
        
    #event = helper.new_event(source="blah", index="asdf", sourcetype="asdf", data=helper.get_input_stanza()["aob_test"]["client_secret"])
    #ew.write_event(event)
    """Implement your data collection logic here

    # The following examples get the arguments of this input.
    # Note, for single instance mod input, args will be returned as a dict.
    # For multi instance mod input, args will be returned as a single value.
    opt_client_id = helper.get_arg('client_id')
    opt_client_secret = helper.get_arg('client_secret')
    # In single instance mode, to get arguments of a particular input, use
    opt_client_id = helper.get_arg('client_id', stanza_name)
    opt_client_secret = helper.get_arg('client_secret', stanza_name)

    # get input type
    helper.get_input_type()

    # The following examples get input stanzas.
    # get all detailed input stanzas
    helper.get_input_stanza()
    # get specific input stanza with stanza name
    helper.get_input_stanza(stanza_name)
    # get all stanza names
    helper.get_input_stanza_names()

    # The following examples get options from setup page configuration.
    # get the loglevel from the setup page
    loglevel = helper.get_log_level()
    # get proxy setting configuration
    proxy_settings = helper.get_proxy()
    # get account credentials as dictionary
    account = helper.get_user_credential_by_username("username")
    account = helper.get_user_credential_by_id("account id")
    # get global variable configuration
    global_userdefined_global_var = helper.get_global_setting("userdefined_global_var")

    # The following examples show usage of logging related helper functions.
    # write to the log for this modular input using configured global log level or INFO as default
    helper.log("log message")
    # write to the log using specified log level
    helper.log_debug("log message")
    helper.log_info("log message")
    helper.log_warning("log message")
    helper.log_error("log message")
    helper.log_critical("log message")
    # set the log level for this modular input
    # (log_level can be "debug", "info", "warning", "error" or "critical", case insensitive)
    helper.set_log_level(log_level)

    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, method, parameters=None, payload=None,
                                        headers=None, cookies=None, verify=True, cert=None,
                                        timeout=None, use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()

    # The following examples show usage of check pointing related helper functions.
    # save checkpoint
    helper.save_check_point(key, state)
    # delete checkpoint
    helper.delete_check_point(key)
    # get checkpoint
    state = helper.get_check_point(key)

    # To create a splunk event
    helper.new_event(data, time=None, host=None, index=None, source=None, sourcetype=None, done=True, unbroken=True)
    """

    '''
    # The following example writes a random number as an event. (Multi Instance Mode)
    # Use this code template by default.
    import random
    data = str(random.randint(0,100))
    event = helper.new_event(source=helper.get_input_type(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
    ew.write_event(event)
    '''

    '''
    # The following example writes a random number as an event for each input config. (Single Instance Mode)
    # For advanced users, if you want to create single instance mod input, please use this code template.
    # Also, you need to uncomment use_single_instance_mode() above.
    import random
    input_type = helper.get_input_type()
    for stanza_name in helper.get_input_stanza_names():
        data = str(random.randint(0,100))
        event = helper.new_event(source=input_type, index=helper.get_output_index(stanza_name), sourcetype=helper.get_sourcetype(stanza_name), data=data)
        ew.write_event(event)
    '''
