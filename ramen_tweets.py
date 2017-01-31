#!/usr/bin/python                                                                                                                                                               
# -*- coding: utf-8 -*-                                                                                                                                                         
from random import choice
import tweepy
import sys

def tweet_image():
    consumer_key        = 'aH3wcFjp8IJ3FMjExrUXLl4nD'
    consumer_secret     = '0TOsRtfaAJFWSmOyCFnkhfwq2aZEOmEraCEElUg4dr0Ii8jmej'
    access_token        = '800556554420224000-ZbCac56flWdHcjTBTa9eXwHKQ6SKQ0Y'
    access_token_secret = '6q0plxzru9Z00KebRQOCj0Hiwff92lDdsxZimz2hHFwDz'

    # Twitter OAuth                                                                                                                                                             
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    # Twitter API                                                                                                                                                               
    api = tweepy.API(auth)

    #meigen
    meigen = []
    for line in open('meigen.txt','r'):
        line = line.rstrip()
        meigen.append(line)

    text = choice(meigen)

    #meigen                                                                                                                                                                     
    gazo = []
    for line in open('gazo.txt','r'):
        line = line.rstrip()
        gazo.append(line)

    pic = choice(gazo)

    # Send Tweet                                                                                                                                                                
    try:
        api.update_with_media(filename=pic+'.jpg', status=text)
    except tweepy.TweepError as e:
        print e
        #print 'Error code {0}: {1}'.format(e[0][0]['code'], e[0][0]['message'])

if __name__ == '__main__':
    tweet_image()
