中 = r'C:\Users\wuyudi\Desktop\temp1.txt'
英 = r'C:\Users\wuyudi\Desktop\temp2.txt'
with open(中, encoding='utf-8') as 中文文件, open(英, encoding='utf-8') as 英文文件:
    def newfile():
        for i, j in enumerate(zip(英文文件, 中文文件)):
            yield j[0]
            if i % 4 == 2:
                yield j[1]

    with open(r'C:\Users\wuyudi\Desktop\34 - 副本.txt', 'w') as f:
        for k in newfile():
            f.write(k)
