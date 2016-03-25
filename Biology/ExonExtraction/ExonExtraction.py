sequence=''
exonSequence=''
p=0
s=0
exon=1
with open('tp53UnigeneExon.txt','r')as f1,open('Exon.txt','w')as f2:
    readLines=(f1.readlines()[3:])
    startLine=readLines[0]
    startNum=int(startLine[56:63])+(50-1)
    for lines in readLines:
        sequence+=lines[0:54].replace(' ','')
    while p<len(sequence):
        if (sequence[p].islower() and sequence[p+1].isupper()):
            startPosition=startNum-(p+1)
            s=p+1
            while sequence[s].isupper():
                exonSequence+=sequence[s]
                s+=1
            endPosition=startNum-(s-1)
            f2.write('exon'+str(exon)+'\t'+str(startPosition)+'\t'+str(endPosition)+'\t'+str(exonSequence)+'\n')
            exon+=1
        p+=1
