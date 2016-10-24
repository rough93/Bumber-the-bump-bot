#!/usr/bin/python
# -*- coding: utf-8 -*-
import praw
import collections
import os
import time
from datetime import datetime
from praw.helpers import submission_stream
import requests
import socket

import SH_auth

#########################################################
# Setup

# Set up praw
bumpy_bot = "Bumpy"
user_agent = bumpy_bot + " Answers quesitons. See https://github.com/rough93/Bumpy"

# Login
r = praw.Reddit(user_agent=user_agent)

# Login old-style due to Reddit politics
r.login(my_auth.username, my_auth.password, disable_warning=True)

# Get accessor to subreddit
subreddit = r.get_subreddit('Starcitizen_trades')

# How many submissions to read from initially
submission_read_limit = 100

# Filename containing list of submission ids that 
# have already been processed, updated at end of program
processed_filename = "submissions_already_processed.txt"

#########################################################
# Helper Functions

def GET_submit_text(self, responder):
        """Get the submission text for the subreddit..
        """
        if c.site.over_18 and not c.over18:
            submit_text = None
            submit_text_html = None
        else:
            submit_text = c.site.submit_text
            submit_text_html = safemarkdown(c.site.submit_text)
        return {'submit_text': submit_text,
                'submit_text_html': submit_text_html}
      
      Bump_Post = ['Star Hangar', 'WTS', 'WTB'] # Match if any of these are found in message
def isbump(message):
  return 'BN' in message and any([b in bump.lower() for b in bumps])

def POST_lock(self, thing):
        """Lock a link.
        Prevents a post from receiving new comments.
        """
        if thing.archived_slow:
            return abort(400, "Bad Request")
        VNotInTimeout().run(action_name="lock", target=thing)
        thing.locked = True
        thing._commit()

        ModAction.create(thing.subreddit_slow, c.user, target=thing,
                         action='lock')
        
        
        # NEEDS ADD
        # TIMER
        #LINK TO BUMP TEXT
