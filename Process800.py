f = open('source/800.txt')
fw = open('voc/800.txt','w')

l = f.readline()
while l:
    l = l.split('□')[0]
    fw.write(l+"\n")
    l = f.readline()

