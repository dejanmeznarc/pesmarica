import re
from collections import Counter


pesmi = open("../src/pesmi.tex", "rt")

lines = pesmi.readlines()

linecount = 0;

avtorji = []

for line in lines:
    linecount = linecount + 1

    avtorji_v_line = re.findall(r"by=\{(.*?)\}", line)


    for avtor in avtorji_v_line:
        avtorji = avtorji + [avtor]

    # if linecount > 10:
    #      break


print("=====")
# print(akordi)


total = len(avtorji)

frekvence = Counter(avtorji)

urejeno = frekvence.most_common(500)


for avtor in urejeno:
    print(f"{round(100*avtor[1]/total,0)}% \t {avtor[1]} \t { avtor[0]} ")