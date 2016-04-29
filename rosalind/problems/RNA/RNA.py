RNA=''
with open('rosalind_rna.txt','r') as f1,open('result.txt','w')as f2:
    for n in f1.read():
        if n=='T':
            RNA+='U'
        else:
            RNA+=n
    f2.write(str(RNA))