import re
from collections import Counter


pesmi = open("../src/pesmi.tex", "rt")

lines = pesmi.readlines()

linecount = 0;

akordi = []

for line in lines:
    linecount = linecount + 1

    akordi_v_tej_linji = re.findall(r"\\\[([^\]]+)\]", line)

    # print(akordi_v_tej_linji)

    for akord in akordi_v_tej_linji:
        akordi = akordi + re.split(r"[/ ]", akord)

    # if linecount > 10:
    #      break


print("=====")
# print(akordi)


total = len(akordi)

frekvence = Counter(akordi)

urejeno = frekvence.most_common(50)


for akord in urejeno:
    print(f"{round(100*akord[1]/total,0)}% \t {akord[1]} \t {akord[0]}")