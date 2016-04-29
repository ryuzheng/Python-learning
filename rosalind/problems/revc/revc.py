RNA=''
with open('rosalind_revc.txt','r') as f1,open('result.txt','w')as f2:
    for n in f1.read():
        if n=='A':
            RNA+='T'
        if n=='T':
            RNA+='A'
        if n=='G':
            RNA+='C'
        if n=='C':
            RNA+='G'
    f2.write(str(RNA)[::-1])