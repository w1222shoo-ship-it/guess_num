import re
from collections import Counter


txt = ''
fin=open("ex.txt",encoding="utf-8")
fin.read()
# lines=fin.readlines()
# for line in lines:
#     txt = txt + line
fin.close()

print(txt)

x = re.sub(r'[，。\n!?]','',txt)
p = Counter(x)
print(p.most_common(2))


