import os

mac = 0
windows = 1
path = ''
if mac == 1:
    path = '/Users/ezulq/youtube-dl/'
if windows == 1:
    path = 'C:\\Users\\ezulq\\youtube-dl\\'

start = input('Enter the time you would like to start the mp3 : ')
end = input('Enter the time you would like to end the mp3 : ')
filename = input('Enter the file name : ')
start = str(int(start.split(':')[0])*60 + int(start.split(':')[1]))
end   = str(int(end.split(':')[0])*60 + int(end.split(':')[1]))

command = 'ffmpeg -ss ' + start + ' -t ' + end + ' -i ' + path + filename + ' -acodec copy ' + path + filename + '_'

os.system(command)
