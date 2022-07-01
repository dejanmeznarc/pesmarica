import re
from collections import Counter
from datetime import datetime

pesmi = open("../src/pesmi.tex", "rt");

sortiranePesmi = open("../src/pesmiSortirane" ".tex", "w")


lines = pesmi.readlines();

curlineNum = 0;


songInfo = []

# get all titles
for line in lines:
    curlineNum = curlineNum + 1

    naslov_pesmi_arr = re.findall(r"\\beginsong\{(.*?)\}", line)

    posebni_naslov = re.findall(r"dejanspecialtitle=\"(.*?)\"", line)



    for naslov_pesmi in naslov_pesmi_arr:

        sinfo = []

        if(len(posebni_naslov) > 0):
            sinfo = [posebni_naslov[0] + " - (" + naslov_pesmi + ")", curlineNum]
        else:
            sinfo = [naslov_pesmi, curlineNum]

        songInfo.append(sinfo)


    # if curlineNum > 500:
    #      break
    #



# sort them
sortedSongInfo =  sorted(songInfo, key=lambda x: x[0], reverse=True)
print(sortedSongInfo)







# go to each song seppratly and get the end



for sortSong in sortedSongInfo:
    sortiranePesmi.write("\n\n% ==================== \n")
    curlineNum = 0
    for line in lines:
        curlineNum = curlineNum + 1

        if curlineNum >= sortSong[1]:
            sortiranePesmi.write(line)
            # TODO: print to other file
            if len(re.findall(r"\\endsong", line)) > 0:
                break














































