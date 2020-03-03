"""
title: ProcessSubtitle.py
date: Feb/20, 2020
author: YiFan Chu

Purpose:
    This program aims to process the source of the subtitle of movies, and finally yield the hard vocabulary.
"""
import srt
import re
import sys
import nltk
import urllib.request, json

voc_dir = "GSAT_voc/"

#2000 words from the junior high new_voc/
#prepare the remove list
l_abbr = [voc.strip(' \n').lower() for voc in open(voc_dir+"abbr.txt")]
l_adj = [voc.strip(' \n') for voc in open(voc_dir+"adj.txt")]
l_adv = [voc.strip(' \n') for voc in open(voc_dir+"adv.txt")]
l_aux = [voc.strip(' \n') for voc in open(voc_dir+"aux.txt")]
l_conj = [voc.strip(' \n') for voc in open(voc_dir+"conj.txt")]
l_verb = [voc.strip(' \n') for voc in open(voc_dir+"final_verbs.txt")]
l_noun = [voc.strip(' \n').lower() for voc in open(voc_dir+"noun.txt")]
l_prep = [voc.strip(' \n') for voc in open(voc_dir+"prep.txt")]
l_pron = [voc.strip(' \n') for voc in open(voc_dir+"pron.txt")]
l_well = [voc.strip(' \n') for voc in open(voc_dir+"well.txt")]
l_names = [voc.strip(' \n').lower() for voc in open(voc_dir+"names_HOC.txt")]
l_dirty = [voc.strip(' \n').lower() for voc in open(voc_dir+"dirty.txt")]
l_brand = [voc.strip(' \n').lower() for voc in open(voc_dir+"brand.txt")]
l_letter = [voc.strip(' \n').lower() for voc in open(voc_dir+"letter.txt")]
remove_l = l_abbr + l_adj + l_adv + l_aux + l_conj + l_verb + l_noun + l_prep + l_pron + l_well + l_names + l_dirty + l_brand + l_letter
#prepare the subtitle file, and parse it with srt package
f = open("source/HouseOfCardsCH1.srt")
l = list(srt.parse(f))

final_list = []
lineCount = 0
for line in l: 
    lineCount +=1

    #the fine descript of the file would be indexed by 9999
    if line.index == 9999:
        break
    #use nltk POS tags to check
    #keep_l = ['JJR','JJS','NN','NNS','RB','RBR','RBS','VB','VBD','VBG','VBN','VBP','VBZ']
    #words = nltk.word_tokenize(s)
    #pos_tags = nltk.pos_tag(words)
    #new_l = []
    #for item in pos_tags:
    #    #if item[0] in abandon_l:
    #    #    continue
    #    if '\'' in item[0]:
    #        continue
    #    if item[0].strip('ing') in lfrqVerb:
    #        continue
    #    if item[1] in keep_l:
    #        if item[1] == 'NNS':
    #            word = re.sub(r's$','',item[0]) 
    #            new_l.append(word)
    #        elif item[1] == 'VBZ':
    #            word = re.sub(r's$','',item[0])
    #            new_l.append(word)
    #        else:      
    #            new_l.append(item[0])
    #s = " ".join(new_l).lower()

    #get the subtitles and strip the special marks <i> in the lines.
    line = line.content.strip('<i>').strip('</i>')
    #remove the numbers in line
    line = re.sub(r'[^\w\s]','',line)
    #remove the punctuations in line
    line = re.sub("\d+", "", line)

    words = list(set(line.lower().split())) 
    
    w = []
    for word in words:
        if word in remove_l:
            continue
        if word.endswith("s") and word[:-1] in remove_l:
            continue
        if word.endswith("d") and (word.strip("d") or word.strip("ed")) in remove_l:
            continue
        w.append(word)
            
    #vocCount = 0
    #for voc in remove_l:
    #    vocCount +=1
    #    if voc in words:
    #        #filter: remove all the voc in line
    #        words = list(filter((voc).__ne__,words))
    #    sys.stdout.write("\rStatus:%s/%s, Lines of File:%s/%s"%(vocCount, len(remove_l), lineCount, len(l)-1))
    #    sys.stdout.flush()     
    
    if len(w) > 0:
        final_list += w
        #s = ' '.join(s)
        #fw.write(line.content+"\n"+str(pos_tags)+"\n"+"#"*20+"\n"+s+"\n"+"="*30+"\n")
        #fw.write(str(line.index)+"\n"+s+"\n"+"="*20+"\n")

    sys.stdout.write("\rLines of File:%s/%s"%(lineCount, len(l)-1))
    sys.stdout.flush()     

final_list = sorted(list(set(final_list)))

cleaned_list = []
for word in final_list:
    if word.endswith('s') and word[:-1] in final_list:
        continue
    if word.endswith("ly") and word[:-2] in final_list:
        continue
    if word.endswith("ing") and word[:-3] in final_list:
        continue
    cleaned_list.append(word)


fw = open("HouseOfCardsCh1Voc.txt", 'w')
fw.write("\n".join(cleaned_list))


#key = "784524c7-31f3-4522-9429-6c821112f06d"
#new_list = []
#for word in final_list:
#    w = []
#    with urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key="+key) as url:
#        data = json.loads(url.read().decode())
#        w[0] = word
#        w[1] = data[0]["fl"]
#        w[2] = data[0]["def"][0]["sseq"][0][0][1]["dt"][0][1]
#        new_list.append(" ".join(w))

