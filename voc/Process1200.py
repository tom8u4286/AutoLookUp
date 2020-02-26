f = open("source/1200.txt", "r")
fw = open("voc/1200.txt", 'w')

l = f.readline()
while l:
    #l = l.split(' ')
    #fw.write(l[1]+"\n")
    #l = []
    l = l.replace('\t', ' ')

    if "art." in l: 
        #print("art. found.")
        l = l.split("art.")
        l = l[0]
        #print(l)
    if "pron." in l: 
        #print("pron. found.")
        l = l.split("pron.")
        l = l[0]
        #print(l)
    if "n." in l: 
        #print("n. found.")
        l = l.split("n.")
        l = l[0]
        #print(l)
    if "adj." in l: 
        #print("adj. found.")
        l = l.split("adj.")
        l = l[0]
        #print(l)
    if "adv." in l: 
        #print("adv. found.")
        l = l.split("adv.")
        l = l[0]
        #print(l)
    if "prep." in l: 
        #print("prep. found.")
        l = l.split("prep.")
        l = l[0]
        #print(l)
    if "v." in l: 
        #print("v. found.")
        l = l.split("v.")
        l = l[0]
        #print(l)
    if "conj." in l: 
        #print("conj. found.")
        l = l.split("conj.")
        l = l[0]
        #print(l)
    if "aux." in l: 
        #print("aux. found.")
        l = l.split("aux.")
        l = l[0]
        #print(l)
    if "int." in l: 
        #print("int. found.")
        l = l.split("int.")
        l = l[0]
        #print(l)
    
    l = l.split(". ")
    l = l[1]
    fw.write(l+"\n")

    
    l = f.readline()
