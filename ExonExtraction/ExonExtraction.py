inputFile=input('要处理的序列的文件名：')
outputFile=input('输出的文件名：')
line=int(input('序列从第几行开始：'))-1
# 输入文件的名称，序列开始的行号等
sequence=''
p=0
exon=1
# 初始化，sequence为处理后的序列,p当前碱基在序列中的位置，exon为外显子的序号
with open(inputFile,'r')as f1,open(outputFile,'a')as f2,open('sequence.txt','w')as f3:
    readLines=(f1.readlines()[line:])
    #从定义的第line行开始读取到文件尾
    startLine=readLines[0]
    startNum=int(startLine[56:63])+(50-1)
    #从第一行算出起始的碱基位置
    #startNum=int(startLine[56:63])-(50-1)
    #正向链的算法
    for lines in readLines:
        sequence+=lines[0:54].replace(' ','')
        #删除序列中的空格，并将序列连起来
    f3.write(sequence)
    #将处理后的序列输出到sequence.txt文件
    while p<len(sequence):
        if sequence[p].islower() and sequence[p+1].isupper():
            startPosition=startNum-p-1
            #startPosition=startNum+p-1
            #正向链的算法
        if sequence[p].isupper() and sequence[p+1].islower():
            endPosition=startNum-p
            #endPosition=startNum+p
            #正向链的算法
            f2.write('exon'+str(exon)+'  '+str(startPosition)+'  '+str(endPosition)+'\n')
            exon+=1
        p+=1
