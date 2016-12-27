#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import math

pos_dict = {}
neg_dict = {}

for line in codecs.open("positive.prob","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    pos_dict[lis[0]] = float(lis[1])

for line in codecs.open("negative.prob","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    neg_dict[lis[0]] = float(lis[1])

pos_prob = 0
neg_prob = 0

for line in codecs.open("test.txt.chasen","r","euc-jp"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        if pos_prob > neg_prob:
            print pos_prob,neg_prob,"positive"
            pos_prob = 0
            neg_prob = 0
        else:
            print pos_prob,neg_prob,"negative"
            pos_prob = 0
            neg_prob = 0
    else:
        lis = line.split("\t")
        if lis[0] in pos_dict:
            pos_prob += math.log(float(pos_dict[lis[0]]))
        else:
            pos_prob += 0.00001

        if lis[0] in neg_dict:
            neg_prob += math.log(float(neg_dict[lis[0]]))
        else:
            pos_prob += 0.00001
