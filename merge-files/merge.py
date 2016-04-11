def mergeFolders(folder1,folder2,folder3,limitdepth):
  import os,re,gzip
  
  # folder1=input("请输入要merge的第一个文件夹：")#folder 1
  # folder2=input("请输入要merge的第二个文件夹：")#folder 2
  # folder3=input("请输入输出的文件夹名：")#output folder
  # limitdepth=int(input("请输入最低匹配深度："))
  dir1=os.listdir(folder1)
  dir2=os.listdir(folder2)
  dir1.sort()
  dir2.sort()
            
  def mergeFiles(filename1,filename2):  
    outputfile='merge-'+re.split('\.',filename1)[0]+'+'+re.split('\.',filename2)[0]+'.'+re.split('\.',filename1)[-1]
    print(outputfile)
    if not(os.path.exists(folder3)):
      os.mkdir(folder3)
    with gzip.open (folder1+'/'+filename1,'r') as f1,gzip.open(folder2+'/'+filename2,'r')as f2,gzip.open(folder3+'/'+outputfile,'w') as f3:
      while True:
        line=f1.readline()
        if len(line)==0:
          break
        else:
          f3.write(line)
      f3.write(bytes('\n', 'UTF-8'))
      while True:
        line=f2.readline()
        if len(line)==0:
          break
        else:
          f3.write(line)
          
  def differ():
    for filename1 in dir1: 
        fn1=re.split('\W|_',filename1)
        for filename2 in dir2:
          fn2=re.split('\W|_',filename2)
          m=0
          n=0
          while m < len(fn1)-1:
            if fn1[m] != fn2[m]:
                break
            if fn1[m] == fn2[m]:
                n+=1
            m+=1
          if n>=limitdepth:
            mergeFiles(filename1,filename2)
  
  differ()
