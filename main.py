import os


source = "target"


def walkFiles():
    global counter
    for something in os.walk(source):
        print something

if (__name__ =='__main__'):
    walkFiles()
