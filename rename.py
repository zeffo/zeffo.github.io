from os import rename, listdir
import re

ROOT = 'assets/animals'
gex = re.compile(r'\.(.*)')
for i, file in enumerate(listdir(ROOT)):
    match = gex.search(file)
    suffix = match.groups()[0]
    rename(f"{ROOT}/{file}", f"{ROOT}/{i}.{suffix}")
