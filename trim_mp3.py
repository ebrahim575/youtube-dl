import os
import rename

mac = 0
windows = 1
path = ''
if mac == 1:
    path = '/Users/ezulq/youtube-dl/'
if windows == 1:
    path = 'C:\\Users\\ezulq\\youtube-dl\\'

print('Renaming files.')
rename.main()
print('Files renamed.')

print('All files in current directory', os.listdir(path),'\n')

filename = input('Enter the file name : ')
start = input('Enter the time you would like to start the mp3 : ')
end = input('Enter the time you would like to end the mp3 : ')

print(filename)
print(start,end)

command = 'ffmpeg -i ' + path + filename + ' -ss ' + start + ' -to ' + end + ' -c copy '  + path + '_' + filename

print(command)

os.system(command)
