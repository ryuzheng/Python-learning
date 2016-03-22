inputfile=input('要处理的序列的文件名：')
outputfile=input('输出的文件名：')
line=int(input('序列从第几行开始：'))-1
sequence=''
p=0
exon=1
with open(inputfile,'r')as f1,open(outputfile,'a')as f2:
    readlines=(f1.readlines()[line:])
    startline=readlines[0]
    startnum=int(startline[56:63])+(50-1)
    for lines in readlines:
        sequence+=lines[0:54].replace(' ','')
    while p<len(sequence):
        if sequence[p].islower() and sequence[p+1].isupper():
            startPosition=startnum-p-1
        if sequence[p].isupper() and sequence[p+1].islower():
            endPosition=startnum-p-1
            f2.write('exon'+str(exon)+'  '+str(startPosition)+'  '+str(endPosition)+'\n')
            exon+=1
        p+=1
