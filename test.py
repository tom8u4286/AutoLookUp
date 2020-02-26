import urllib.request, json
with urllib.request.urlopen("https://www.dictionaryapi.com/api/v3/references/collegiate/json/beautiful?key=784524c7-31f3-4522-9429-6c821112f06d") as url:
    data = json.loads(url.read().decode())
    print(data[0]["meta"]["id"])
    print(data[0]["fl"])
    print(data[0]["def"][0]["sseq"][0][0][1]["dt"][0][1])
    #print(data["fl"])
    #print(data["def"])
