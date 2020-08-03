with open("读入文件", encoding='utf-8') as in_, open('输出文件', 'a') as out:
    def write_in():
        for i, j in enumerate(in_):
            if i % 5 != 3:
                yield j
    for i in write_in():
        out.write(i)
