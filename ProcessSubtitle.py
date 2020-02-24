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

#simple 2000 words from the junior high voc
l1200 = [voc.strip(' \n') for voc in open("voc/1200.txt")]
l800 = [voc.strip(' \n') for voc in open("voc/800.txt")]

#frequent 100 verbs
lfrqVerb = [voc.strip(' \n') for voc in open("voc/frqVerb.txt")]

#frequent easy words that the nltk cannot strip out. manually edited.
lfrqWord = [voc.strip(' \n') for voc in open("voc/frqWords.txt")]

remove_l = l1200+l800+lfrqVerb+lfrqWord

l = list(srt.parse(f))

final_list = []
lineCount = 1
for line in l:
    #get the subtitles and strip the special marks <i> in the lines.
    if line.index == 9999:
        break
    s = line.content.strip('<i>').strip('</i>')

    #use nltk POS tags to check
    keep_l = ['JJR','JJS','NN','NNS','RB','RBR','RBS','VB','VBD','VBG','VBN','VBP','VBZ']
    #abandon_l = ['\'s','\'m','\'re','\'ve','n\'t']
    words = nltk.word_tokenize(s)
    pos_tags = nltk.pos_tag(words)
    #print(pos_tags)
    new_l = []
    for item in pos_tags:
        #if item[0] in abandon_l:
        #    continue
        if '\'' in item[0]:
            continue
        if item[1] == 'VBG' and item[0].strip('ing') in lfrqVerb:
            continue
        if item[1] in keep_l:
            if item[1] == 'NNS':
                word = re.sub(r's$','',item[0]) 
                new_l.append(word)
            elif item[1] == 'VBZ':
                word = re.sub(r's$','',item[0])
                new_l.append(word)
            else:      
                new_l.append(item[0])

    #remove the speciall mark in srt files
    #s = s.strip('<\i>')

    #remove the punctuations in lines
    #s = re.sub(r'[^\w\s]','',s)

    #remove the numbers
    #s = re.sub("\d+", "", s) 

    s = " ".join(new_l).lower()
        
    vocCount = 1
    s = s.split()
    for voc in remove_l:
        if voc in s:
            #remove all the voc in line
            s = list(filter((voc).__ne__,s))
        sys.stdout.write("\rStatus:%s/%s, Lines of File:%s/%s"%(vocCount, len(remove_l), lineCount, len(l)))
        sys.stdout.flush()     

        vocCount +=1
    
    if len(s) > 0:
        final_list += s
        #s = ' '.join(s)
        #fw.write(line.content+"\n"+str(pos_tags)+"\n"+"#"*20+"\n"+s+"\n"+"="*30+"\n")
        #fw.write(str(line.index)+"\n"+s+"\n"+"="*20+"\n")
    lineCount +=1
final_list = list(set(final_list))
fw.write('\n'.join(final_list))
