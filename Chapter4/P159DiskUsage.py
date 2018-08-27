import os

def disk_usage(path):
    total = os.path.getsize(path)

    if os.path.isdir(path):
        for filename in os.listdir(path):
            childPath = os.path.join(path, filename)
            total += disk_usage(childPath)

    print(total, path)
    return total


if __name__ == '__main__':
    disk_usage('/Users/keyuanwu/Desktop/DataStructuresAndAlgorInPython/')