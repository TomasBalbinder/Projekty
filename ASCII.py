

import urllib.request, urllib.parse, urllib.error

ff = urllib.request.urlopen("https://tomasbalbinderphoto.com/") 

for line in ff:
    print(line.decode().strip())