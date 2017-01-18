#!/usr/bin/python
# -*- coding: utf-8 -*-
import MeCab
import tweepy
import codecs
import re
import ramen_tweets
import sys
from random import choice
from os.path import isfile
import fcntl
from fcntl import flock


def getTweet():
    consumer_key        = ''
    consumer_secret     = ''
    access_token        = ''
    access_token_secret = ''

    # Twitter OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)

    # Twitter API
    api = tweepy.API(auth)

    count = 5
    # Timelineの取得 (1)
    # 自分がフォロー関係のツイートを取得する
    #print u'[ Home Timeline : 最新 %d件 ]' % count
    timeline = api.home_timeline(count=count)

    #ここ要らないかもしれない( ˘ω˘ )？
    #for tweet in timeline:
    #    print '--'
    #    print u'発 言 者:\t%s' % tweet.user.screen_name
    #	 print u'本 　 文:\t%s' % tweet.text
    #    print u'MssageId:\t%s' % tweet.id
    #    print u'発言時間:\t%s' % tweet.created_at
    f = open('text.txt', 'w') # 書き込みモードで開く
    for tweet in timeline:
        f.write(tweet.text.encode('utf-8')) # 引数の文字列をファイルに書き込む
    f.close() # ファイルを閉じる

def doChasen():
    # ----- set sentence -----
    f = open('text.txt')
    test_sentence = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()


    # ----- defined functions -----
    tagger = MeCab.Tagger('-Ochasen')
    result = tagger.parse(test_sentence)
    print result
    f = codecs.open('text.txt.chasen','w',"euc_jp")
    f.write(result.decode('utf-8','ignore'))
    f.close()

def tweet_image():

    consumer_key        = 'aH3wcFjp8IJ3FMjExrUXLl4nD'
    consumer_secret     = '0TOsRtfaAJFWSmOyCFnkhfwq2aZEOmEraCEElUg4dr0Ii8jmej'
    access_token        = '800556554420224000-ZbCac56flWdHcjTBTa9eXwHKQ6SKQ0Y'
    access_token_secret = '6q0plxzru9Z00KebRQOCj0Hiwff92lDdsxZimz2hHFwDz'

    # Twitter OAuth                                                                                                                                                             
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
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


    # Twitter API                                                                                                                                                               
    api = tweepy.API(auth)
    # これまでに対応したstatus idのリスト格納用
    data = []

    if isfile('log.txt'):
	f = open('log.txt', 'r')
	flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
	for line in f.readlines():
            data.append(int(line.strip()))
	flock(f, fcntl.LOCK_UN)
	f.close()
    else:
	print 'Warning: log.txt not found'
    # 更新された status_id のリストを書き出し
    f = open('log.txt', 'w')
    flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    for item in data:
        f.write('%d\n' % item)
    flock(f, fcntl.LOCK_UN)
    f.close()

    # 自分への未応答のメンションのそれぞれについて応答
    mentions = api.mentions_timeline(count=5)
    for tweet in mentions:
	if not tweet.id in data:
            try:
		api.update_with_media(filename=pic+'.jpg',status='@%s' % (tweet.user.screen_name.encode('utf-8')) + text,in_reply_to_status_id=tweet.id)
		data.append(tweet.id)
                print text
            except tweepy.TweepError as e:
		print e
	else:
            print 'INFO: already replied %d' % tweet.id

    # 更新された status_id のリストを書き出し
    f = open('log.txt', 'w')
    flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    for item in data:
	f.write('%d\n' % item)
    flock(f, fcntl.LOCK_UN)
    f.close()

def regExp():
    #ツイートの正規表現
    tweet_dict = {}
    noun_dict = {}
    verb_dict = {}
    for line in codecs.open("text.txt.chasen","r","euc_jp"):
        line = line.rstrip('\r\n')
        if line == "EOS":
            pass
        else:
            lis = line.split("\t")
            if re.search(ur"名詞", lis[3]) or re.search(ur"動詞", lis[3]):
                print lis[0]
                if lis[0] in noun_dict:
                    tweet_dict[lis[0]] += 1
                else:
                    tweet_dict[lis[0]] = 1
            else:
                pass
    len_tweet_dict = len(tweet_dict)

    print " ".join([x[0] for x in tweet_dict.items()])

    #ここからharaheri.txtの正規表現
    for line in codecs.open("haraheri.txt.chasen","r","euc_jp"):
        line = line.rstrip('\r\n')
        if line == "EOS":
            pass
        else:
            lis = line.split("\t")
            if re.search(ur"名詞", lis[3]):
                if lis[0] in noun_dict:
                    noun_dict[lis[0]] += 1
                else:
                    noun_dict[lis[0]] = 1
            elif re.search(ur"動詞", lis[3]):
                if lis[0] in verb_dict:
                    verb_dict[lis[0]] += 1
                else:
                    verb_dict[lis[0]] = 1
            else:
                pass


    #ツイートとharaheri.txtを照合
    len_noun_dict = len(noun_dict)
    len_verb_dict = len(verb_dict)
    verb = 0
    noun = 0

    for key in tweet_dict.keys():
        if key in noun_dict:
            noun+=1
        elif key in verb_dict:
            verb+=1

    print "verb=",verb,"noun=",noun

    if verb > 0 and noun > 0:
        tweet_image()


def main():
    getTweet()
    doChasen()
    regExp()



if __name__ == "__main__":
    main()
