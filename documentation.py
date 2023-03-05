from os import listdir, walk
from time import time
from psutil import users

s = time()
path = f"/Users/{users()[0][0]}/Desktop/Code/CodeEdit/CodeEdit/"

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

files = []

for i, j in zip(files_dict.keys(), files_dict.values()):
    print("Filtering", i)
    with open(f"{j}/{i}", "r") as f:
        contents = f.read()

    if "// TODO: DOCS" in contents:
        files.append(contents)
    
print(f"Found {len(files)} files to create documentation.")

print("Task 2/3 complete")




e = time()
print(f"Finished in {e-s} seconds")