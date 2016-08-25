import re
sequence=''
exonSequence=''
a=0
p=0
s=0
exon=1
with open('tp53UnigeneExon.txt','r')as f1,open('Exon.txt','w')as f2,open('sequence.txt','w')as f3:
    next(f1)
    readLines=(f1.readlines())
    while a < len(readLines)-1:
        if len(readLines[a])>1:
            break
        a+=1
    startLine=readLines[a]
    #if len(re.findall('\d+',startLine))>0:
    #   startNum=int(re.findall('\d+',startLine)[0])+len(re.findall('[A-Za-z]',startLine))-1
    #else:
    #   startNum=0
    startNum=int(re.findall('\d+',startLine)[0])+len(re.findall('[A-Za-z]',startLine))-1
    for lines in readLines:
        sequence+=''.join((re.findall('[A-Za-z]',lines)))
    f3.write(sequence)
    sequence='a'+sequence#在序列前加一个内含子，解决序列一开始就是外显子的bug
    while p<(len(sequence)-1):
        if (sequence[p].islower() and sequence[p+1].isupper()):
            exonSequence=""
            print(p)
            startPosition=startNum-(p+1)+1
            s=p+1
            while sequence[s].isupper():
                exonSequence+=sequence[s]
                s+=1
            endPosition=startNum-(s-1)+1
            f2.write('exon'+str(exon)+'\t'+str(startPosition)+'\t'+str(endPosition)+'\t'+str(exonSequence)+'\n')
            exon+=1
            p=s-1
        p+=1
