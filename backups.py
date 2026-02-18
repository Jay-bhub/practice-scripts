from pathlib import Path
import datetime
import zipfile

paths = [
    # Enter paths to compress
    
]

with zipfile.ZipFile('Archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZip:
    for i in paths:
        for j in i.iterdir():
            myZip.write(j)
