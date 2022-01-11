import os


def find_files(suffix, path):
    path_list = []
    _find_files(suffix, path, path_list)

    return path_list


def _find_files(suffix, path, path_list):

    if os.path.isdir(path):
        for directory in os.listdir(path):
            _find_files(suffix, os.path.join(path, directory), path_list)

    if os.path.isfile(path):
        if path.endswith(suffix):
            path_list.append(path)


### TEST CASES ###

print(find_files('.c', 'testdir'))
# ['testdir\\subdir1\\a.c', 'testdir\\subdir3\\subsubdir1\\b.c', 'testdir\\subdir5\\a.c', 'testdir\\t1.c']

print(find_files('.d', 'testdir'))
# []

print(find_files('.c', ''))
# []
