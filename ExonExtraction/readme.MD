
 1.  编写程序读文件tp53UnigeneExon.txt
 2.  从文件中提取外显子在染色体上的位置（起始位置和终止位置），并把信息存入一个生成的新文件中。

文件格式：

>exon 1    start_position    end_position
exon2    start_position end_position
......

注： 不同列用tab键分割

对文件tp53UnigeneExon.txt中内容的注释：

 - 小写字母代表内含子（intron）
 - 大写字母代表外显子（exon）
 - 数字（如：7590914）：是所在行最后一个字母在染色体上的位置
