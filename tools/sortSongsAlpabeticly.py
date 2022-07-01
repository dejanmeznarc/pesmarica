import re
from collections import Counter
from datetime import datetime

pesmi = open("../src/pesmi.tex", "rt");

sortiranePesmi = open("../src/pesmi-sorted-"+datetime.now().strftime("%H_%M_%S") + ".tex", "w")


lines = pesmi.readlines();

curlineNum = 0;


songInfo = []

# get all titles
for line in lines:
    curlineNum = curlineNum + 1

    naslov_pesmi_arr = re.findall(r"\\beginsong\{(.*?)\}", line)



    for naslov_pesmi in naslov_pesmi_arr:

        sinfo = [naslov_pesmi, curlineNum]

        songInfo.append(sinfo)


    # if curlineNum > 500:
    #      break
    #



# sort them
sortedSongInfo =  sorted(songInfo, key=lambda x: x[0])
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














































