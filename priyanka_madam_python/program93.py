# checking the file and then deleting the file

import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("the file dosen't exist")