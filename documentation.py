from os import walk, getcwd
from time import time

backtick = "`"

start = time()
path = getcwd()

files_dict = {}
for (dir_path, dir_names, filenames) in walk(path):
    filename = list(filenames)

    for i in filename:
        if not ".swift" in i:
            print(f"Removing: {i}")
            filename.remove(i)
        else:
            files_dict[i] = dir_path
    
print("Task 1/3 complete")
print("Filtering files")

files = {}

for i, j in zip(files_dict.keys(), files_dict.values()):
    print("Filtering", i)
    with open(f"{j}/{i}", "r") as f:
        contents = f.read()

    if "// TODO: DOCS" in contents:
        files[i] = contents
    
print(f"Found {len(files)} files to create documentation.")

print("Task 2/3 complete")
md_files = {}
structs = 0
extensions = 0
enums = 0

for i, j in zip(files.keys(), files.values()):
    text = j.split("\n")
    md = f"""# `{i}`
    ## Topics"""

    for k in text:
        if "struct" in k:
            s = k.removeprefix("struct")
            s = s.removesuffix("{")
            print(s)
            structs += 1

    print(md)

print(f"{structs} Structs, {extensions} Extensions and {enums} Enums")
end = time()
print(f"Finished in {end-start} seconds")
