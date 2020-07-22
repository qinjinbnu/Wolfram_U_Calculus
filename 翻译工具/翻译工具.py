中文文件 = open(r'C:\Users\wuyudi\Desktop\temp1.txt',
            encoding='utf-8').readlines()
英文文件 = open(r'C:\Users\wuyudi\Desktop\temp2.txt',
            encoding='utf-8').readlines()


def newfile():
    for i, j in enumerate(英文文件):
        yield j
        if i % 4 == 2:
            yield 中文文件[i]


with open(r'C:\Users\wuyudi\Desktop\34 - 副本.txt', 'w') as f:
    for k in newfile():
        f.write(k)
