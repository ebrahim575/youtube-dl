import os


url = input('enter the url :')
os.system('youtube-dl --rm-cache-dir')
if '&' in url:
    url = url[0:url.find('&') + 1]

command = "youtube-dl -f bestaudio --extract-audio --embed-thumbnail --add-metadata --audio-format mp3 --audio-quality 0 " + url

os.system(command)
