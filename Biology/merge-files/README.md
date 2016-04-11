#merge-files

两个文件夹，其中部分文件的前缀一致，需要将对应前缀一致的文件合并起来，并且这些文件均为gz压缩文件。

limitdepth设置比对时最少需要有多少个部分一致才merge文件。

##usage

```
cd path/to/merge-files
python
>>>import merge
>>>merge.mergeFolders('dir1','dir2','output-folder',2)
```