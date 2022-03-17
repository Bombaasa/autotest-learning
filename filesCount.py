import os

dirnum, filenum, exe, py = 0, 0, 0, 0
path = '/usr/lib'

for lists in os.listdir(path):
    sub_path = os.path.join(path, lists)
    print(sub_path)
    if os.path.isfile(sub_path):
        if sub_path[-4:] == ".exe":
            exe = exe + 1
        elif sub_path[-3:] == ".py":
            py = py + 1
        filenum = filenum + 1
    elif os.path.isdir(sub_path):
        dirnum = dirnum + 1

print('dirnum: ', dirnum)
print('exenum: ', exe)
print('pynum: ', py)
print('filenum: ', filenum)
