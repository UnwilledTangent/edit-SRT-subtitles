# open file copy
# every line with "-->"
# copy 18th character until 29th character of the 1st "-->" line
# paste it on the 1st till 12th character of 2nd "-->" line
# rinse and repeat until you hit end of file

secondTiming = ""

# change the below 2 lines
with open("Lycoris.Recoil.S01E01.WEBRip.Netflix.ja[cc] - Copy.srt", "r", encoding="utf-8") as readFile:
    with open("LycorisRecoilE01EditedSubtitles.srt", "w", encoding="utf-8") as writeFile:
        currentLine = readFile.readline()

        while currentLine != "":
            if "-->" in currentLine:
                # suppose this is the 2nd "-->" line onwards
                if secondTiming != "":
                    # paste 2ndTiming onto 1st till 12th character
                    currentLine = currentLine[12:]
                    currentLine = secondTiming + currentLine

                secondTiming = currentLine[17:29]

            writeFile.write(currentLine)
            currentLine = readFile.readline()

readFile.close()
writeFile.close()
