"""
title: ProcessSubtitle.py
date: Feb/20, 2020
author: YiFan Chu

Purpose:
    This program aims to process the source of the subtitle of movies, and finally yield the vocabulary.
"""
import srt
import re
import sys
import nltk

f = open("source/HouseOfCardsCH1.srt")
fw = open("HouseOfCardsCh1Voc.txt", 'w')

l2000 = [voc.strip(' \n') for voc in open("voc/1200.txt")]+[voc.strip(' \n') for voc in open("voc/800.txt")]+[voc.strip(' \n') for voc in open("voc/frqWords.txt")]+[voc.strip(' \n') for voc in open("voc/frqVerb.txt")]

l = list(srt.parse(f))

lineCount = 1
for line in l:
    s = line.content

    #remove the speciall mark in srt files
    s = s.strip('<\i>')

    #remove the punctuations in lines
    s = re.sub(r'[^\w\s]','',s)

    #remove the numbers
    s = re.sub("\d+", "", s) 

    #use nltk POS tags to check
    #words = nltk.word_tokenize(s)
    #pos_tags = nltk.pos_tag(words)
    #print(pos_tags)
    
    #exit()

    s = s.lower()
        
    vocCount = 1
    s = s.split()
    for voc in l2000:
        if voc in s:
            #remove all the voc in line
            s = list(filter((voc).__ne__,s))
        sys.stdout.write("\rStatus:%s/%s, Lines of File:%s/%s"%(vocCount, len(l2000), lineCount, len(l)))
        sys.stdout.flush()     

        vocCount +=1
    
    if len(s) > 0:
        s = ' '.join(s)
        fw.write(line.content+"\n"+"#"*20+"\n"+s+"\n"+"="*30+"\n")
    lineCount +=1
