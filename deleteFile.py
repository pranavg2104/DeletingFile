import os
import time

def getLocationAndTime(location):
    store={}
    for root , directories , files in os.walk(location):
        for filename in files:
            filepath=os.path.join(root,filename)
            store[filepath]=os.stat(filepath).st_mtime
    return sorted(store.items(), key=lambda x:x[1])

def deleteFile(files):
    keep=len(files)-5
    for i in range(0,keep):
        os.remove(files[i][0])

files=getLocationAndTime("D:/Output")
deleteFile(files)
