with open("C:\\Users\\vaibh\\OneDrive\\Desktop\\script.py") as f, open("C:\\Users\\vaibh\\OneDrive\\Desktop\\scriptOut.py", "w") as out,open("C:\\Users\\vaibh\\OneDrive\\Desktop\\scriptOut.py", "r") as outR :
    print(out.write(f.read()))
    print(outR.read())

import os

if os.path.exists("C:/Users/vaibh/OneDrive/Desktop/scriptOut.py"):
    os.remove("C:/Users/vaibh/OneDrive/Desktop/scriptOut.py")