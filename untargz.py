import os
from os import listdir
import tarfile
import sys

root = 'D:\\05\\gz\\'


def extract_file():
    for i in listdir(root):
        file = i
        if file == 'secret-word.txt':
            sys.exit()
        elif file.endswith("tar.gz"):
            try:
                tar = tarfile.open(root + file, "r:gz")
                try:
                    tar.extractall(path=root)
                finally:
                    tar.close()
            finally:
                os.remove(root + file)
        elif file.endswith("tar"):
            try:
                tar = tarfile.open(root + file, "r:")
                try:
                    tar.extractall(path=root)
                finally:
                    tar.close()
            finally:
                os.remove(file)


while True:
    extract_file()
