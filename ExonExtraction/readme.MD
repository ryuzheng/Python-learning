1. 编写程序读文件tp53UnigeneExon.txt
2. 从文件中提取外显子在染色体上的位置（起始位置和终止位置），并把信息存入一个生成的新文件中。
3. 把exon对应的sequence序列写在输出文件的第四列

文件格式：

```html
exon1  start_position  end_position  exon_sequence
exon2  start_position  end_position  exon_sequence
......
```


注： 不同列用tab键分割

对文件tp53UnigeneExon.txt中内容的注释：

- 小写字母代表内含子（intron）
- 大写字母代表外显子（exon）
- 数字（如：7590914）：是所在行最后一个字母在染色体上的位置