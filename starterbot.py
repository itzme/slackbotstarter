#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, json, re, os
from slackclient import SlackClient

class SlackBot:

    def main(self):
        token = os.environ.get("SLACK_TOKEN")

        slack_client = SlackClient(token)

        if slack_client.rtm_connect():

            while True:
                new_evts = slack_client.rtm_read()

                for evt in new_evts:
                    #print evt

                    if 'type' in evt:

                        if str(evt["type"]) == "message" and "text" in evt:
                            # this is where the logic for the human input text is placed.
                            # we also get more information from the JSON
                            keyword = True
                            channel = evt['channel']
                            response = evt['text']
                            print response

                    elif 'reply_to' in evt:

                        #this is where the logic for the chat bot is placed.
                        slack_client.rtm_send_message('This is where the messages will go', 'Hello World')


        else:
            print "Failed."



if __name__ == '__main__':
    bot = SlackBot()
    bot.main()
