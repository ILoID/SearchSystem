import os, fnmatch

# def find_all(name, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             result.append(os.path.join(root, name))
#     return result


def find(pattern, path):
    results = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                results.append(os.path.join(root, name))
    return results


def to_readable(list):
    print('\nThis is what i could find:\n')
    for item in list:
        print(item)


def main():
    filename = input('Please input a filename or pattern to search for.\n')
    directory = input('Please input the directory to be searched in.\n')
    to_readable(find(filename, directory))


main()