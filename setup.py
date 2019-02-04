import os
import py_compile

import config


def __in_venv(directory):
    return os.path.join("SubroutineTest", "venv") in directory


# If the script is run, it will compile all files in its directory except itself
if __name__ == "__main__":
    # Delete old *.pyc files
    for root, dirs, files in os.walk(config.ROOT_DIR):
        # Do not touch venv folder
        if __in_venv(root):
            continue
        for filename in files:
            if filename.endswith(".pyc"):
                os.remove(os.path.join(root, filename))
    # Compile *.py files, omit setup.py
    for root, dirs, files in os.walk(config.ROOT_DIR):
        # Do not touch venv folder
        if __in_venv(root):
            continue
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("setup.py"):
                output = filename + "c"
                py_compile.compile(os.path.join(root, filename), os.path.join(root, output))
