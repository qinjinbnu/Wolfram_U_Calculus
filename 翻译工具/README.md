# 下面是可以参考的流程

假设源文件为 `xx.srt`

1. 打开 `xx.srt`, 把内容复制到 docx 和 txt 里，记为 `xx.docx` 和 `xx.txt`
2. 把 `xx.docx` 拖动到 [deepl](https://www.deepl.com/translator)，得到新文件 `xx - ZH.docx`
3. 打开 `xx - ZH.docx`, 把内容复制到 `yy.txt`

> 因为 txt 读取相对方便

此时两个文件的内容应该是,注意开头不要有多余空格，每段间隔一个空行

```
1
00:00:00,000 --> 00:00:07,000
Hello, and welcome to Lesson 34 of this introduction to calculus with Wolfram U.

2
00:00:07,000 --> 00:00:12,000
The topic for this lesson is logarithmic functions.

3
```

```
1
00:00:00,000 --> 00:00:07,000
大家好，欢迎来到本次与沃尔夫兰大学合作的微积分入门第34课。

2
00:00:07,000 --> 00:00:12,000
本节课的课题是对数函数。

3
```

下载 `翻译工具.nb` , 放在 `xx.txt` ,`yy.txt` 同一目录下，把对应的文件名改掉，运行。
或 `翻译工具.py`，直接把路径写在文件里的位置，运行。
