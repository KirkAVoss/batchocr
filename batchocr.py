from subprocess import call

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
args = parser.parse_args()

for file in args.file:
    call(['ocrmypdf',str(file),'OCRed_' + str(file)])
