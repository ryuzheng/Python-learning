m=0
protein=''
with open ("rosalind_prot.txt","r")as f1:
    x=f1.read()
    while m<len(x):
        c=x[m:m+3]
        # print(c)
        if c=="UUU" or c=="UUC":
            protein+="F"
        elif c=="UUA" or c=="UUG" or c=="CUU" or c=="CUC" or c=="CUA" or c=="CUG":
            protein+="L"
        elif c=="UCU" or c=="UCC" or c=="UCA" or c=="UCG" or c=="AGU" or c=="AGC":
            protein+="S"
        elif c=="UAU" or c=="UAC":
            protein+="Y"
        elif c=="UGU" or c=="UGC":
            protein+="C"
        elif c=="UGG":
            protein+="W"
        elif c=="CCU" or c=="CCC" or c=="CCA" or c=="CCG":
            protein+="P"
        elif c=="CAU" or c=="CAC":
            protein+="H"
        elif c=="CAA" or c=="CAG":
            protein+="Q"
        elif c=="CGU" or c=="CGC" or c=="CGA" or c=="CGG" or c=="AGA" or c=="AGG":
            protein+="R"
        elif c=="AUU" or c=="AUC" or c=="AUA":
            protein+="I"
        elif c=="AUG":
            protein+="M"
        elif c=="ACU" or c=="ACC" or c=="ACA" or c=="ACG":
            protein+="T"
        elif c=="AAU" or c=="AAC":
            protein+="N"
        elif c=="AAA" or c=="AAG":
            protein+="K"
        elif c=="GUU" or c=="GUC" or c=="GUA" or c=="GUG":
            protein+="V"
        elif c=="GCU" or c=="GCC" or c=="GCA" or c=="GCG":
            protein+="A"
        elif c=="GAU" or c=="GAC":
            protein+="D"
        elif c=="GAA" or c=="GAG":
            protein+="E"
        elif c=="GGU" or c=="GGC" or c=="GGA" or c=="GGG":
            protein+="G"
        elif c=="UAA" or c=="UAG" or c=="UGA":
            break
        m+=3
    print(protein)