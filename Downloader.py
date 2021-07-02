import re
import requests as rq
import shutil

website = "https://play.pokemonshowdown.com/sprites/"
branches = ["gen5ani/", "gen5/"]
savePaths = ["sprites/front/animated/", "sprites/front/static/"]

rFile = open("indices.html", "r")

for line in rFile:

    ln = re.search("(?:<td><a href=\"(?P<path>(?P<name>[^-\s]+)-?(?P<form>(?<=-).+|(?!-))(?P<fileType>\.(?:gif)|(?:png)))\">(?P=path)<\/a><\/td>)", line)

    if not ln:
        continue
    
    path = ln.group("path")
    name = ln.group("name")
    form = ln.group("form")
    fileType = ln.group("fileType")
    
    print(ln)
    print(path)
    print(name)
    print(form)

    if "gif" in fileType:
        i = 0
    elif "png" in fileType:
        i = 1
    else:
        print("ERROR! FileType not found!")
        
    url = website + branches[i] + path
    saveTo = savePaths[i] + path
    response = rq.get(url, stream=True)
                            
    with open(saveTo, 'wb') as outFile:
        shutil.copyfileobj(response.raw, outFile)

rFile.close()
