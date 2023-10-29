import os
from os import listdir
import tarfile
import sys

ROOT_DIR = 'D:\\05\\gz\\'


def extract_file():
    """
    The script extracts recursive *.tar.gz archives
    """
    for i in listdir(ROOT_DIR):
        file = i
        if file == 'secret-word.txt':
            sys.exit()
        elif file.endswith("tar.gz"):
            try:
                tar = tarfile.open(ROOT_DIR + file, "r:gz")
                try:
                    tar.extractall(path=ROOT_DIR)
                finally:
                    tar.close()
            finally:
                os.remove(ROOT_DIR + file)
        elif file.endswith("tar"):
            try:
                tar = tarfile.open(ROOT_DIR + file, "r:")
                try:
                    tar.extractall(path=ROOT_DIR)
                finally:
                    tar.close()
            finally:
                os.remove(file)


while True:
    extract_file()
