from io import TextIOWrapper
from os import listdir
from os.path import isfile, join



def getFiles(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def openFile(path, file):
    try:
        return open(path+file, "r")
    except:
        return -1
    
def readLine(file: TextIOWrapper):
    line = file.readline()
    