import urllib.request, json
import sys

f = open("verb.txt")
#f = json.load(open("test.json"))
#data = json.dumps(f[0]["meta"]["stems"])
words = f.read().split("\n")


key = "784524c7-31f3-4522-9429-6c821112f06d"

final_verb_l = []
cnt = 0
for word in words:
    cnt+=1
    url = urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key="+key)
    data = json.loads(url.read().decode())
    stems = data[0]["meta"]["stems"]
    for item in stems:
        if len(item.split(" "))==1:
            final_verb_l.append(item)
    sys.stdout.write("\rStatus:%s/%s"%(cnt, len(words)))
    sys.stdout.flush()

fw = open("final_verbs.txt","w")
fw.write("\n".join(final_verb_l))
