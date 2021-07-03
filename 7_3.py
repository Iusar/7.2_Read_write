import os
from pathlib import Path
from pprint import pprint

#summary_file = open("Общий.txt", "w+")
all_files = []
files = ['1.txt','2.txt','3.txt']

def sort_list(file_list):
    files_dict = {}
    sorted_list = []
    for file in file_list:
        with open(file, "r", encoding="utf-8") as text_file:
            for line_index, line in enumerate(text_file):
                pass
        files_dict[line_index+1] = file

    sorted_dict = sorted(files_dict.items())

    return sorted_dict

def unite_files(file_list):
    with open("Общий.txt", 'a+') as summary_file:
        for file in file_list:
            summary_file.write('\n')
            summary_file.write(file[1])
            summary_file.write('\n')
            summary_file.write(str(file[0]))
            summary_file.write('\n')
            with open(file[1], "r", encoding="utf-8") as text_file:
                for line in text_file:
                    summary_file.write(line)

    pass

unite_files(sort_list(files))
