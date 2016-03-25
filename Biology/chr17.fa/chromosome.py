with open ('chr17.fa','r')as f1,open ('sequence.fa','w')as f2:
    next(f1)
    sequence=f1.read().replace('\n','')
    f2.write(sequence[7571720-1:7590868-1])
