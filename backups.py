from pathlib import Path
import datetime
import zipfile

timestamp = datetime.datetime.now().strftime("%Y-%M-%D")
archive_name = f'Archive{timestamp}.zip'

paths = [
    # Enter paths to compress
    
]

with zipfile.ZipFile('Archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as myZip:
    for i in paths:
        for j in i.iterdir():
            myZip.write(j)
