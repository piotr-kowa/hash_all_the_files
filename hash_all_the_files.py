import os
import hasher
from fileProps import *
from raiTimer import RaiTimer


class PathChanger:
    def __init__(self, path):
        self.__mainPath = os.getcwd()
        os.chdir(path)

    def __del__(self):
        os.chdir(self.__mainPath)


class FileWriter:
    def __init__(self, filename):
        self.f = open(filename, "w", newline='\n')

    def write(self, content):
        self.f.write(content)

    def __del__(self):
        self.f.close()


def get_file_info(full_file_path):
    file_props = FileProps(full_file_path)
    md5_sum = hasher.md5sum(full_file_path)
    filename = os.path.basename(full_file_path)
    return file_props.getStringRow() + md5_sum + " " + filename + "\n\n"


def create_check_sum_file_for_dir(files, dirpath):
    full_md5_file_path = os.path.join(dirpath, "_" + os.path.basename(os.path.abspath(dirpath)) + "_checksum.md5")
    print("creating: " + full_md5_file_path + " for " + str(len(files)) + " files")
    md5_sum_file = FileWriter(full_md5_file_path)
    for filename in files:
        full_file_path = os.path.join(dirpath, filename)
        md5_sum_file.write(get_file_info(full_file_path))


def filter_out_md5_files(filelist):
    return list(filter(lambda f: f[-4:] != ".md5", filelist))


def do_for_dir(files, dirpath):
    filtered_files = filter_out_md5_files(files)
    if len(filtered_files) > 0:
        create_check_sum_file_for_dir(filtered_files, dirpath)


def do_for_dir_recursively(directory):
    rai = PathChanger(directory)
    current_dir_rel_path = ".\\"
    for dirpath, dirs, files in os.walk(current_dir_rel_path):
        do_for_dir(files, dirpath)


from manual_test_dirpath import test_path

timer = RaiTimer()
do_for_dir_recursively(test_path)
