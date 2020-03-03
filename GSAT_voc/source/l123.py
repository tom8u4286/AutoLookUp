f = open("noun.txt").read().split('\n')

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []



for line in f:
    line = line.split('\t')
    line = list(filter(("").__ne__, line))
    if "一" in line[0]:
        l1.append(line[1])
    if "二" in line[0]:
        l2.append(line[1])
    if "三" in line[0]:
        l3.append(line[1])
    if "四" in line[0]:
        l4.append(line[1])
    if "五" in line[0]:
        l5.append(line[1])

fw = open("noun5.txt","w")
l = l5
#fw = open("adv5.txt","w")
#l = l5
fw.write("\n".join(l))
