import re
import os

path = "C:/Users/Tatjana Smiljnic/Desktop/Lesson07/wget-activehistory/"
newFolder = "C:/Users/Tatjana Smiljnic/Desktop/Lesson07/wget-activehistory/modified/issues/"
listOfFiles = os.listdir(path)

for f in listOfFiles:
    with open(path+f, "r", encoding="utf8") as f1:
        data = f1.read()
        # find the date: the date variable contains the given date in the format YYYY-MM-DD
        date = re.search(r'<date value="([\d-]+)"', data).group(1)
        # split the texts in articles
        splitting = re.split(r"<div3 type=\"article\"", data)
        # counter for counting... 
        counter = 0
        # path to new folder with the issue date
        newPath = newFolder + date + "/"

        # check if new path exist, if not then create it
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        # loop through the splitted text sections, clean it and write it
        for i in splitting[1:]:
            # counter for numbering
            counter += 1
            # for cleaning the header tag, we have to make the header complete again
            i = "<div 3 " + i
            # removes markup
            text = re.sub("<[^<]+>","", i)
            # creating new file path and name 
            newFile =  newPath + date + "_" + str(counter) + ".xml"
            # write everthing in a new file
            with open(newFile, "w", encoding="utf8") as f9:
                f9.write(text)