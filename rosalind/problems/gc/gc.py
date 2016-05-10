#!/usr/bin/python
import re

re1='(>)'	# Any Single Character 1
re2='((?:[a-z][a-z0-9_]*))'	# Variable Name 1
rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)

i=0
x=-1
percentage=0
percentage2=0
sequence=["","","","","","","","","",""]
name=[]
maxSeq=''
maxGC=0

with open('rosalind_gc.txt','r') as f1:
    lines = f1.readlines()
    while i < len(lines):
        m = rg.search(lines[i])
        if m:
            name.append(lines[i])
            x+=1
        else:
            sequence[x]+=''.join((re.findall('[A-Za-z]',lines[i])))
        i+=1
    z=0
    while z<len(sequence):
        GC=0
        for n in sequence[z]:
            if (n=="G") or (n=="C"):
                GC+=1
                percentage=GC/len(sequence[z])
            if percentage > percentage2:
                percentage2=percentage
                maxSeq=name[z]
                maxGC=percentage2
        z+=1
    # print(sequence)
    # print(name)
    print(maxSeq)
    print(maxGC*100)