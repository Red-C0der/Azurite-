__author__ = 'Red_C0der'

def newfile(filename):
    import os
    nfile = open(str(filename), "r+")
    file.close()

def delfile(filename):
    import os

def get(val_name, filename="../settings/settings.cfg"):
    import os
    import logger
    value = ""
    file = open(filename, "r")
    for line in file:
        if ": " not in line:
            pass
        else:
            tmp = line.split(": ")
            value = tmp[1]
            index = tmp[0]
            if index == val_name:
                return value
    if value is "":
        logger.write("e", "File: cfgfileparser.py | Function: get | Error: cfgfileparser was not able to find index "+val_name+" in file "+filename+" !")
        return False

def set(val_name, new_val, filename="../settings/settings.cfg"):
    import os
    file = open(filename, 'r')
    i = 0
    for line in file:
        if val_name in line:
            lines = open(filename, 'r').readlines()
            lines[i] = val_name + ": " + new_val + "\n"
            out = open(filename, 'w')
            out.writelines(lines)
            out.close()
        i = i + 1