i=0
n=0
with open('rosalind_hamm.txt','r') as f1:
    seq1=f1.readline();
    seq2=f1.readline();
    while (i < len(seq1)-1):
        if seq1[i]!=seq2[i]:
            n+=1
        i+=1
    print(n)