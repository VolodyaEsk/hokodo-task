import os
from pprint import pprint


def print_directory_contents(path):
    pprint(get_file_paths(path))


def get_file_paths(path):
    paths = []

    if os.path.isfile(path):
        paths.append(os.path.abspath(path))
        return paths
    else:
        for item in os.listdir(path):
            path_ = get_file_paths(os.path.join(path, item))
            if path_:
                paths.extend(path_)

    return paths


if __name__ == "__main__":
    print_directory_contents("../tests")
