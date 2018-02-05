#!/usr/bin/python3

'''
Utility to aid uploading marks. It traverses the contents of
assignmentDirectory, and whenever it finds a mark file, it moves the contents of
the mark file into the user's clipboard so that they can paste it on CULearn.

This utility is intended to be a stopgap until I get fully automatic uploading
to CULearn working.
'''

import os

try:
    import pyperclip
except ModuleNotFoundError as error:
    print(error)
    print('This utility requires pyperclip to function.')
    exit()

def fetchMarks(assignmentDirectory):
    for root, dirs, files in os.walk(assignmentDirectory):
        if 'mark' in files:
            print(root, end='')
            with open(os.path.join(root, 'mark'), 'r') as markFile:
                pyperclip.copy(markFile.read())
            input() # wait until user presses the enter key

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('assignmentDirectory', type=str,
        help='path to the directory containing all of the marked assignments')
    args = parser.parse_args()
    fetchMarks(args.assignmentDirectory)
