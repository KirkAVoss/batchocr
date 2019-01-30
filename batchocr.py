from subprocess import call

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

for file in args.file:
    #print(file,str(file),file.name)
    print("Processing:",file.name)
    call(['ocrmypdf','-q',str(file.name),'OCRed_' + str(file.name)])
