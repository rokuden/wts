#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re

def count_word(word, dictionary):
    if word in dictionary.keys():
        pass
    else:
        dictionary[word] = 0

    dictionary[word] += 1
    return dictionary

frequency = {}
for line in codecs.open("okashira.txt.chasen","r","euc-jp"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur"名詞",lis[3]):
            frequency = count_word(lis[0], frequency)

for x in sorted(frequency.items(),key=lambda x:x[1], reverse=True):
    print "名詞「",x[0],"」は",x[1],"回"
