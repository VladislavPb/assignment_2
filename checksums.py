import hashlib
import os

checkfile = input()  #The input file

dirname = input()    #Directory containing files to check
all_files = set(os.listdir(dirname))

for i in open(checkfile, 'r').readlines():
    args = list(map(str, i.split()))
    file_name = args[0]
    method = args[1]
    checksum = args[2]

    if file_name not in all_files:
        print(f'{file_name} NOT FOUND')
    else:
        my_file = open(f'{dirname}/{file_name}', 'rb')
        data = my_file.read()

        if method == 'md5':
            checksum2 = hashlib.md5(data).hexdigest()
        elif method == 'sha1':
            checksum2 = hashlib.sha1(data).hexdigest()
        elif method == 'sha256':
            checksum2 = hashlib.sha256(data).hexdigest()

        if checksum == checksum2:
            print(f'{file_name} OK')
        else:
            print(f'{file_name} FAIL')
