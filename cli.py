##########
# IMPORT #
##########
import argparse
from os.path import exists, isfile
from parser import ParserJuniper

__author__ = "rick@gnous.eu"
__licence__ = "GPL3"

parserJuniper = ParserJuniper()
parserArg = argparse.ArgumentParser(
        description="Parse a Juniper conf file and print the series of set commands for."
        )
parserArg.add_argument("-f", "--file", nargs=1, required=True, type=str, help="The conf file.")
parserArg.add_argument("-o", "--output", nargs=1, type=str, help="The output file.")

arg = parserArg.parse_args()

inputFile = str(arg.file[0])
outputFile = None
if arg.output:
    outputFile = str(arg.output[0])
    if exists(outputFile) and isfile(outputFile):
        writeOverFile = input("The file already exists, write over it ? o/O")
        if writeOverFile.lower() != 'o':
            print("STOP EVERYTHING!!!!!!!!!!!!!")
            exit(0)
    elif exists(outputFile):
        print("The output musts be a file.")
        exit(0)

if exists(inputFile) and isfile(inputFile):
    parseResul = parserJuniper.parseFile(inputFile)    
    if outputFile:
        with open(outputFile, 'w') as file:
            file.write(parseResul)
    else:
        print(parseResul)
else:
    print("Pass an existing file.")
