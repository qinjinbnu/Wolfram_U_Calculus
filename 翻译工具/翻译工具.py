from functools import partial
from itertools import cycle
英 = r'C:\Users\wuyudi\Desktop\temp1.txt'
中 = r'C:\Users\wuyudi\Desktop\temp2.txt'
输出 = r'C:\Users\wuyudi\Desktop\34 - 副本.txt'

Open = partial(open, encoding='utf-8')
with Open(中) as 中文文件, Open(英) as 英文文件, Open(输出, 'w') as f:
    for i, 英文, 中文 in zip(cycle(range(4)), 英文文件, 中文文件):
        f.write(英文)
        if i == 2:
            f.write(中文)
