#!/usr/bin/python3

'''
unzips all of the zip files under targetDirectory into a directory with
the same name as the zip file, in the same directory as the zip file.
'''

import os
import zipfile

dir_path = os.path.dirname(os.path.realpath(__file__))

def unzip(targetDirectory):
    for root, dirs, files in os.walk(targetDirectory):
        for filename in files:
            if filename.endswith('.zip'):
                targetFile = os.path.join(root, filename)
                with zipfile.ZipFile(targetFile, 'r') as zipRef:
                    zipRef.extractall(root)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('targetDirectory', type=str, nargs='?',
        default=dir_path,
        help='path to the directory containing all of the zip files')
    args = parser.parse_args()
    unzip(args.targetDirectory)
