import os,re,gzip

folder1='dir1'#folder 1
folder2='dir2'#folder 2
limitdeep=int(input('depth: '))
dir1=os.listdir(folder1)
dir2=os.listdir(folder2)
dir1.sort()
dir2.sort()

for filename1 in dir1:
    fn1=re.split('\W+|\_+', filename1)
    for filename2 in dir2:
        fn2=re.split('\W+|\_+', filename2)
        m=0
        n=0
        while m < len(fn1)-1:
            if fn1[m] != fn2[m]:
                break
            if fn1[m] == fn2[m]:
                n+=1
            m+=1
        if n >= limitdeep:
            outputfile='merge-'+re.split('\.',filename1)[0]+'-'+re.split('\.',filename2)[0]
            print(outputfile)
            if not(os.path.exists(r"output")):
                os.mkdir("output")
            with gzip.open(folder1+'/'+filename1,'rb') as f1,gzip.open(folder2+'/'+filename2,'rb') as f2,open('output/'+outputfile,'wb')as f3:
                while True:
                    line = f1.readline();
                    if len(line)==0:
                        break
                    else:
                        f3.write(line)
                f3.write(b'\n')
                while True:
                    line = f2.readline();
                    if len(line)==0:
                        break
                    else:
                        f3.write(line)