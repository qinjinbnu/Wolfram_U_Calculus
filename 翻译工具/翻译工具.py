中文文件 = open(r'C:\Users\wuyudi\Desktop\新建文本文档 (3).txt',
            encoding='utf-8').readlines()
英文文件 = open(r'C:\Users\wuyudi\Desktop\34.txt',
            encoding='utf-8').readlines()


def newfile():
    for i, j in enumerate(英文文件):
        yield j
        if i % 4 == 2:
            yield 中文文件[i]


with open(r'C:\Users\wuyudi\Desktop\34 - 副本.txt', 'w') as f:
    f.write(newfile())
