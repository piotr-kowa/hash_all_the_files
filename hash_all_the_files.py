import os
import hasher


class PathChanger:
    def __init__(self, path):
        self.__mainPath = os.getcwd()
        os.chdir(path)

    def __del__(self):
        os.chdir(self.__mainPath)


class FileWriter:
    def __init__(self, filename):
        self.f = open(filename, "w")

    def write(self, content):
        self.f.write(content)

    def __del__(self):
        self.f.close()


def create_check_sum_file_for_dir(files, dirpath):
    full_md5_file_path = os.path.join(dirpath, os.path.basename(os.path.abspath(dirpath)) + "_checksum.md5")
    print("creating: " + full_md5_file_path + " for " + str(len(files)) + " files")
    md5_sum_file = FileWriter(full_md5_file_path)
    for filename in files:
        full_file_path = os.path.join(dirpath, filename)
        md5_sum = hasher.md5sum(full_file_path)
        md5_sum_file.write(md5_sum + " " + filename + "\n")


def do_for_dir(files, dirpath):
    filter_out_md5_files = lambda f: f[-4:] != ".md5"
    filtered_files = list(filter(filter_out_md5_files, files))
    if len(filtered_files) > 0:
        create_check_sum_file_for_dir(filtered_files, dirpath)


def do_for_dir_recursively(directory):
    path_changer = PathChanger(directory)
    current_dir_rel_path = ".\\"
    for dirpath, dirs, files in os.walk(current_dir_rel_path):
        do_for_dir(files, dirpath)


test_path = "./data"
do_for_dir_recursively(test_path)
