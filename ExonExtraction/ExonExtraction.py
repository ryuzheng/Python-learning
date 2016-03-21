filename=input("请输入文件名：")
with open(filename,'r')as file:
    for line in file:
        for x in line:
            if x.isupper() and (x-1).islower():
                startposition=
            if x.islower() and (x+1).isupper():
                stopposition=
                print ...
