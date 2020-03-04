import urllib.request, json
import sys
import re

f = open("adj.txt")
#f = json.load(open("test.json"))
#data = json.dumps(f[0]["meta"]["stems"])
words = f.read().split("\n")


key = "784524c7-31f3-4522-9429-6c821112f06d"

fw = open("adj_stems.txt","w")
stems_l = []
cnt = 0
for word in words:
    word = re.sub(r'[^\w\s]','',word)
    word = word.replace(" ", "")
    cnt+=1
    try:
        url = urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key="+key)
        data = json.loads(url.read().decode())
        stems = data[0]["meta"]["stems"]
    except:
        print("Problem line: "+ cnt)
        continue
    #ls = []
    for item in stems:
        if len(item.split(" "))==1:
            stems_l.append(item)
            #ls.append(item)
    #fw.write("\n".join(ls)+"\n")
    sys.stdout.write("\rStatus:%s/%s"%(cnt, len(words)))
    sys.stdout.flush()

fw.write("\n".join(stems_l))
