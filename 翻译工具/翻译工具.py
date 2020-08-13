from functools import partial

英 = r'C:\Users\wuyudi\Desktop\temp1.txt'
中 = r'C:\Users\wuyudi\Desktop\temp2.txt'
输出 = r'C:\Users\wuyudi\Desktop\34 - 副本.txt'

Open = partial(open, encoding='utf-8')
中文文件, 英文文件, f = Open(中), Open(英), Open(输出, 'w')
with 中文文件, 英文文件, f:
    def newfile():
        for i, (英文, 中文) in enumerate(zip(英文文件, 中文文件)):
            yield 英文
            if i % 4 == 2:
                yield 中文
    for k in newfile():
        f.write(k)
