A=0
T=0
G=0
C=0
with open ('rosalind_dna.txt','r') as f1:
    for n in f1.read():
        if n=='A':
            A+=1
        if n=='T':
            T+=1
        if n=='C':
            C+=1
        if n=='G':
            G+=1
    print(str(A)+'\t'+str(C)+'\t'+str(G)+'\t'+str(T))