import os
from sys import platform

def remove_char(filename):
    renamedStr = ''
    for i in range(len(filename)):
        if filename[i].isalpha():
            renamedStr += filename[i]
    renamedStr = renamedStr[:len(renamedStr)-2]
    renamedStr+='.mp3'
    return renamedStr

def main():
    if platform == 'win32':
        currDir = 'C:\\Users\\ezulq\\youtube-dl\\'

    elif platform == 'darwin':
        currDir = '/Users/ezulq/Desktop/'

    else:
        currDir = 'C:\\Users\\ezulq\\youtube-dl\\'

    lst = os.listdir(currDir)

    for i in range(len(lst)):

        if '.mp3' in lst[i]:
            src = currDir + lst[i]
            renamed_filename = remove_char(lst[i])
            dst = currDir + renamed_filename
            print('Renaming ',src,'to ',dst)
            os.rename(src,dst)
        else:
            continue
main()
