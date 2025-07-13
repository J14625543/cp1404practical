import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
        languages.append(language)
    in_file.close()
    for language in languages:
        print(language)
main()


