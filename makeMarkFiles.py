#!/usr/bin/python3

'''
Makes a mark file for every folder under the targetDirectory (i.e. makes
one for each student). (Optional) It takes a template file as an argument 
using --templateFile and a name for each file using --markFileName.
'''

import os
from shutil import copyfile

dir_path = os.path.dirname(os.path.realpath(__file__))

def makeMarkFiles(targetDirectory, templateFile, markFileName):
    for root, dirs, files in os.walk(targetDirectory):
        for dirname in dirs:
            if dirname.endswith('_assignsubmission_file_'):
                markFilePath = os.path.join(root, dirname, markFileName)
                if templateFile is not None:
                    copyfile(templateFile, markFilePath)
                else:
                    open(markFilePath, 'a+').close()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('targetDirectory', type=str, nargs='?',
        default=dir_path,
        help='path to the directory containing all of the zip files')
    parser.add_argument('--templateFile', type=str, nargs='?',
        default=None,
        help='path to the marking template file')
    parser.add_argument('--markFileName', type=str, nargs='?',
        default='mark',
        help='path to the marking template file')
    args = parser.parse_args()
    makeMarkFiles(args.targetDirectory, args.templateFile, args.markFileName)
