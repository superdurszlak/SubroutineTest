import os
import py_compile

# If the script is run, it will compile all files in its directory except itself
if __name__ == "__main__":
    # List all files in directory
    directory = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    # Delete old *.pyc files
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for filename in files:
            if filename.endswith(".pyc"):
                os.remove(os.path.join(root, filename))
    # Compile *.py files, omit setup.py
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("setup.py"):
                output = filename + "c"
                py_compile.compile(os.path.join(root, filename), os.path.join(root, output))
