import re
import os


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # iterate over all the entries
    for entry in listOfFile:
        # create full path
        fullPath = os.path.join(dirName, entry)
        # if entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

matches = []
allMatches = []

# goes through files
for file in getListOfFiles(r"C:\Users\nncic\Desktop\FrontEnd\src\app\modules\admin"):
    textFile = open(file)
    # reg = re.compile("\w+(?=\s?\|\s?translate)")
    reg = re.compile("\w+(?=\s?\|\s?translate)")
    # search for phrase in file
    for line in textFile:
        matches += reg.findall(line)
    print(file)
    print(matches)
    allMatches += matches
    matches.clear()
    textFile.close()

print(allMatches)
