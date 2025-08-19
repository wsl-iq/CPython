import os
import sys
import glob
import time
def BuildTools():
    os.system("python setup.py build_ext --inplace")
    versionPy = f"cp{sys.version_info.major}{sys.version_info.minor}"
    pattern = f"mylib.{versionPy}-win_amd64.pyd"
    files = glob.glob(pattern)
    if files:
        old_name = files[0]
        dll_name = "mylib.dll"
        os.rename(old_name, dll_name)
        print(f"Created DLL: {dll_name}")
    else:
        print(f"File {pattern} not found")
        sys.exit(1)
    time.sleep(1)
    os.system("python dll.py")
if __name__ == "__main__":
    BuildTools()
