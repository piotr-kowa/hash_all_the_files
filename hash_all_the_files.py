import os
import hasher
from fileProps import *
from raiMemoryMeasure import RaiMemoryMeasure
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


def get_file_info(full_file_path, dirpath):
    file_props = FileProps(full_file_path)
    md5_sum = hasher.md5sum(full_file_path)
    filename = os.path.relpath(full_file_path, dirpath)
    return file_props.getStringRow() + md5_sum + " " + filename + "\n\n"


def filter_out_md5_files(filelist):
    return list(filter(lambda f: f[-4:] != ".md5", filelist))


def create_check_sum_file_for_dir(files, dirpath):
    files = filter_out_md5_files(files)
    if len(files) < 1:
        return

    full_md5_file_path = os.path.join(dirpath, "_" + os.path.basename(os.path.abspath(dirpath)) + "_checksum.md5")
    print("creating: " + full_md5_file_path + " for " + str(len(files)) + " files")

    md5_sum_file = FileWriter(full_md5_file_path)
    for filename in files:
        full_file_path = os.path.join(dirpath, filename)
        md5_sum_file.write(get_file_info(full_file_path, dirpath))


def do_for_dir_recursively(directory):
    rai_dir = PathChanger(directory)
    rai_timer = RaiTimer()
    rai_memory = RaiMemoryMeasure()

    current_dir_rel_path = ".\\"
    for dirpath, dirs, files in os.walk(current_dir_rel_path):
        create_check_sum_file_for_dir(files, dirpath)
        print("dirpath:: ", dirpath)
        print("dirs: ", dirs)
        print("files: ", files[:5])
        print("\n\n")


from manual_test_dirpath import test_path

do_for_dir_recursively(test_path)
RaiMemoryMeasure()


