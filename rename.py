
import os
folder = "/Users/ezulq/youtube-dl/"
arr = os.listdir(path=folder)
for i in range(len(arr)):
    filename = arr[i]
    
    if '.mp3' in arr[i]:
        filename = arr[i]
        for j in range(len(filename)):
            if not filename[j].isalpha():
                filename[j].replace(filename[j],'')



