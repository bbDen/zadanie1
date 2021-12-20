from os import listdir
from os.path import isfile, join

file_dir = '/Users/danny/Desktop/mOD'


def file_names(file_dir):

    only_files = [f for f in listdir(file_dir)if isfile(join(file_dir,f))]
    return only_files

print(file_names(file_dir))
