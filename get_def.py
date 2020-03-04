from skPublish import API
import json
import sys
import xml.etree.ElementTree as ET


baseUrl = "https://dictionary.cambridge.org/api/v1/"
dictCode = "english-chinese-traditional"
accessKey = "L7E5Rwg0bImD3ZJNFH13CvVNpWnACp3vEpmP6QMOqyMDJKGQSLCZvQzMnHSrAv4I"
api = API( baseUrl , accessKey)

f = open("HouseOfCardsCh1Voc.txt")
fw = open('HouseOFCardsCH1Voc_Chinese.txt','w')
words = f.read().split('\n')
final_l = []
cnt = 0
for word in words:
    cnt+=1
    try:
        results = json.loads(api.searchFirst(dictCode, word , "xml"))
        xmlcontent = results["entryContent"]
    except:
        print("line "+str(cnt)+", error occurred.")
        continue
    root = ET.fromstring(xmlcontent)
    #word = root.find('header').find('title').text
    pos = "("+root.find('toc-page').find('toc-entry').find('toc-pos-block').find('toc-pos').text[:3:]+")"

    l = []
    for i,item in enumerate(root.iter(tag='definition')):
        l.append(str(i+1)+". "+item.find('trans').text)
    
    s = word + pos + " ".join(l)
    #final_l.append(s)
    fw.write(s+'\n')

    sys.stdout.write("\rStatus:%s/%s"%(cnt, len(words)))
    sys.stdout.flush()



