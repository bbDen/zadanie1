from os import listdir
from os.path import isfile, join

file_dir = '/Users/danny/Desktop/mOD'

only_files = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]


def get_extension(file):
    if isinstance(file, str):
        if '.' in file:
            print(file.split(".")[-1])
        else:
            return "Невозможно определить расширение файла"
    else:
        return 'Вы передали неверное значение'


print(get_extension(only_files[0]))
