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

Bump_Post = ['WTB', 'WTS'] # Match if any of these are found in message
def isbump(message):
  return 'BN' in message and any([b in bump.lower() for b in bumps])
