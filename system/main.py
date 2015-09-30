# coding=utf-8
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Name: Azurite                                                               |
#  |   Version: 0.0.2                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0776                                                            |
#  |   GitHub-Page: http://red-c0der.github.io/Project-Azurite                     |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/

class VarKeeper:
    version = "0.0.2"
    s_key = ""
    trusted_hosts = {}
    host = "127.0.0.1"
    bg_processes = {}

    current_bootmode = ""

    current_user = "super"

    # Console
    console_currdir = "system"


class Output:
    def CPrint(text, fgc=500, bgc=500, attrc="", newline=True):
        from colored import fg, bg, attr, style
        import sys
        if newline is True:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        print(fg(fgc) + text + style.RESET)
                    else:
                        print(fg(fgc) + attr(attrc) + text + style.RESET)
                else:
                    if attrc == "":
                        print(fg(fgc) + bg(bgc) + text + style.RESET)
                    else:
                        print(fg(fgc) + bg(bgc) + attr(attrc) + text + style.RESET)
            else:
                if bgc != 500:
                    if attrc == "":
                        print(bg(bgc) + text + style.RESET)
                    else:
                        print(bg(bgc) + attr(attrc) + text + style.RESET)
        else:
            if fgc != 500:
                if bgc == 500:
                    if attrc == "":
                        sys.stdout.write(fg(fgc) + text + style.RESET)
                    else:
                        sys.stdout.write(fg(fgc) + attr(attrc) + text + style.RESET)
                else:
                    if attrc == "":
                        sys.stdout.write(fg(fgc) + bg(bgc) + text + style.RESET)
                    else:
                        sys.stdout.write(fg(fgc) + bg(bgc) + attr(attrc) + text + style.RESET)
            else:
                if bgc != 500:
                    if attrc == "":
                        sys.stdout.write(bg(bgc) + text + style.RESET)
                    else:
                        sys.stdout.write(bg(bgc) + attr(attrc) + text + style.RESET)
    def CSPrint(self, state, message):
        import termcolor
        from colored import fg, bg, attr, style
        if state == "":
            print("[" + termcolor.colored("....", "cyan", attrs=["bold"]) + "] " + message)
        if state == "ok":
            print("[ " + termcolor.colored("OK", "green", attrs=["bold"]) + " ] " + termcolor.colored(message, "green", attrs=["bold"]))
        if state == "error":
            print("[" + termcolor.colored("ERROR", "red", attrs=["blink", "bold"]) + "] " + termcolor.colored(message, "red", attrs=["bold"]))
        if state == "warning":
            # 208
            print("[" + fg(241) + attr("bold") + attr("blink") + "WARNING" + style.RESET + "] " + fg(241) + attr("bold") + message + style.RESET)
        if state == "info":
            print("[" + termcolor.colored("INFO", "cyan", attrs=["bold"]) + "] " + termcolor.colored(message, "cyan", attrs=["bold"]))
        if state == "debug":
            print("[" + termcolor.colored("DEBUG", "magenta", attrs=["bold"]) + "] " + termcolor.colored(message, "magenta", attrs=["bold"]))
        if state == "sys":
            print("[" + termcolor.colored("SYSTEM", "blue", attrs=["bold"]) + "] " + termcolor.colored(message, "blue", attrs=["bold"]))


class Startup:
    
    def startup(self):
        import logger
        import time
        lloc = "File: main.py | Class: Startup | Function: startup | "
        self.version_string = "       |   Version: " + VarKeeper.version + ""
        for i in range(67 - len(VarKeeper.version)):
            self.version_string = self.version_string + " "
        self.version_string = self.version_string + "|"
        self.curruser_string = "       |   Current User: " + VarKeeper.current_user + ""
        for i in range(62 - len(VarKeeper.current_user)):
            self.curruser_string = self.curruser_string + " "
        self.curruser_string = self.curruser_string + "|"
        self.time = time.strftime("%H:%M:%S") + " | " + time.strftime("%d/%m/%Y")
        self.time_string = "       |   Current Time: " + self.time
        for i in range(62 - len(self.time)):
            self.time_string = self.time_string + " "
        self.time_string = self.time_string + "|"
        logger.write("i",  "")
        logger.write("i",  "")
        logger.write("i",  "")
        logger.write("i",  "")
        logger.write("i",  "        /=============================================================================\ ")
        logger.write("i",  "       |                                                                               |")
        logger.write("i",  "       |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |")
        logger.write("i",  "       |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |")
        logger.write("i",  "       |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |")
        logger.write("i",  "       |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |")
        logger.write("i",  "       |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |")
        logger.write("i",  "       |                                                                               |")
        logger.write("i",  "       |       _                    _ _                                                |")
        logger.write("i",  "       |      / \    _____   _ _ __(_) |_ ___                                          |")
        logger.write("i",  "       |     / _ \  |_  / | | | '__| | __/ _ \                                         |")
        logger.write("i",  "       |    / ___ \  / /| |_| | |  | | ||  __/                                         |")
        logger.write("i",  "       |   /_/   \_\/___|\__,_|_|  |_|\__\___|                                         |")
        logger.write("i",  "       |                                                                               |")
        logger.write("i",  "" + self.version_string)
        logger.write("i",  "       |                                                                               |")
        logger.write("i", "" + self.time_string)
        logger.write("i",  "       |                                                                               |")
        logger.write("i",  "" + self.curruser_string)
        logger.write("i",  "       |                                                                               |")
        logger.write("i",  "        \=============================================================================/ ")
        logger.write("i",  "")
        logger.write("i",  "")
        logger.write("i",  "")
        logger.write("i",  "")
        print ""
        print ""
        print ""
        print ""
        print "        /=============================================================================\ "
        print "       |                                                                               |"
        print "       |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |"
        print "       |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |"
        print "       |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |"
        print "       |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |"
        print "       |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |"
        print "       |                                                                               |"
        print "       |       _                    _ _                                                |"
        print "       |      / \    _____   _ _ __(_) |_ ___                                          |"
        print "       |     / _ \  |_  / | | | '__| | __/ _ \                                         |"
        print "       |    / ___ \  / /| |_| | |  | | ||  __/                                         |"
        print "       |   /_/   \_\/___|\__,_|_|  |_|\__\___|                                         |"
        print "       |                                                                               |"
        print "" + self.version_string
        print "       |                                                                               |"
        print "       |                                                                               |"
        print "" + self.time_string
        print "       |                                                                               |"
        print "" + self.curruser_string
        print "       |                                                                               |"
        print "        \=============================================================================/ "
        print ""
        print ""
        print ""
        print ""
        print "Enter BootMode:"
        print "  [N]ormal     | Enters a normal system mode with everything being active!"
        print "  [S]afe       | Disables all processes and protocols which could be a potential security issue!"
        print "  [D]ebug      | Returns most system values and writes every value into the log file!"
        print ""

        try:
            while True:
                uinput = raw_input("N / S / D  => ")
                uinput = uinput
                if uinput is "n":
                    VarKeeper.current_bootmode = "n"
                    logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                    break
                else:
                    if uinput is "N":
                        VarKeeper.current_bootmode = "n"
                        logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                        break
                    else:
                        if uinput is "s":
                            VarKeeper.current_bootmode = "s"
                            logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                            break
                        else:
                            if uinput is "S":
                                VarKeeper.current_bootmode = "s"
                                logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                                break
                            else:
                                if uinput is "d":
                                    VarKeeper.current_bootmode = "d"
                                    logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                                    break
                                else:
                                    if uinput is "D":
                                        VarKeeper.current_bootmode = "d"
                                        logger.write("i", lloc+"User entered BootMode: "+VarKeeper.current_bootmode)
                                        break
                                    else:
                                        print uinput + " is not a valid option!"
        except:
            logger.write("e", lloc+"Something went wrong while ")

        if VarKeeper.current_bootmode is "n":
            Startup.boot_normal()
        else:
            if VarKeeper.current_bootmode is "s":
                Startup.boot_safe()
            else:
                if VarKeeper.current_bootmode is "d":
                    Startup.boot_debug()
                else:
                    logger.write("ex", lloc+"Fatal Fail: Could not continue boot into BootMode!")
    #Security.loadthosts()

    def boot_normal(self):
        import logger
        import sys
        import time
        lloc = "File: main.py | Class: Startup | Function: boot_normal | "
        print ""
        Output.CSPrint("", "Booting into Normal Mode")
        Output.CSPrint("", "Loading security key")

        try:
            VarKeeper.s_key = Security.loadkey()
        except:
            logger.write("e", lloc+"Could not load security key!")
            Output.CSPrint("warning", "Could not load security key! Continue anyways? [y/n]")
            uinput = raw_input("y / n => ")
            if uinput is "y":
                logger.write("w", lloc+"!! Continuing without security key! Nothing will be encrypted or decrypted !!")
                Output.CSPrint("warning", "!! Continuing without security key! Nothing will be encrypted or decrypted !!")
            else:
                if uinput is "Y":
                    logger.write("w", lloc+"!! Continuing without security key! Nothing will be encrypted or decrypted !!")
                    Output.CSPrint("warning", "!! Continuing without security key! Nothing will be encrypted or decrypted !!")
                else:
                    if uinput is "n":
                        logger.write("w", lloc+"Retrying loading security key 5 times. After that system will shutdown!")
                        Output.CSPrint("i", "Retrying loading security key 5 times. After that system will shutdown!")
                        finished = False
                        for i in range(5):
                            if VarKeeper.s_key is not "":
                                break
                            self.r_count = 5 - i
                            try:
                                VarKeeper.s_key = Security.loadkey()
                            except:
                                logger.write("w", lloc+"Failed loading key again! Retrying " + str(self.r_count) + " more times!")
                                Output.CSPrint("error", "Failed loading key again! Retrying " + str(self.r_count) + " more times!")
                                time.sleep(3)
                            if VarKeeper.s_key is not "":
                                finished = True
                        if VarKeeper.s_key is not "":
                            Output.CSPrint("ok", "Successfully loaded security key!")
                        else:
                            Output.CSPrint("error", "Could not load security key! Quitting system!")
                            sys.exit(0)
                    else:
                        if uinput is "N":
                            logger.write("w", lloc+"Retrying loading security key 5 times. After that system will shutdown!")
                            Output.CSPrint("i", "Retrying loading security key 5 times. After that system will shutdown!")
                            finished = False
                            for i in range(5):
                                if VarKeeper.s_key is not "":
                                    break
                                self.r_count = 5 - i
                                try:
                                    VarKeeper.s_key = Security.loadkey()
                                except:
                                    logger.write("w", lloc+"Failed loading key again! Retrying " + str(self.r_count) + " more times!")
                                    Output.CSPrint("error", "Failed loading key again! Retrying " + str(self.r_count) + " more times!")
                                    time.sleep(3)
                                if VarKeeper.s_key is not "":
                                    finished = True
                            if VarKeeper.s_key is not "":
                                Output.CSPrint("ok", "Successfully loaded security key!")
                            else:
                                Output.CSPrint("error", "Could not load security key! Quitting system!")
                                sys.exit(0)
        Output.CSPrint("ok", "Successfully loaded security key!")
        Output.CSPrint("", "Loading trusted hosts")

        try:
            Security.loadthosts()
        except:
            logger.write("e", lloc+"Could not load trusted hosts!")
            Output.CSPrint("warning", "Could not load trusted hosts! Continue anyways? [y/n]")
            uinput = raw_input("y / n => ")
            if uinput is "y":
                logger.write("w", lloc+"!! Continuing without trusted hosts! Hosts identify can't be proofed when connected !!")
                Output.CSPrint("warning", "!! Continuing without trusted hosts! Hosts identify can't be proofed when connected !!")
            else:
                if uinput is "Y":
                    logger.write("w", lloc+"!! Continuing without trusted hosts! Hosts identify can't be proofed when connected !!")
                    Output.CSPrint("warning", "!! Continuing without trusted hosts! Hosts identify can't be proofed when connected !!")
                else:
                    if uinput is "n":
                        logger.write("w", lloc+"Retrying loading trusted hosts 5 times. After that system will shutdown!")
                        Output.CSPrint("i", "Retrying loading trusted hosts 5 times. After that system will shutdown!")
                        finished = False
                        for i in range(5):
                            if VarKeeper.trusted_hosts is not {}:
                                break
                            self.r_count = 5 - i
                            try:
                                Security.loadthosts()
                            except:
                                logger.write("w", lloc+"Failed loading trusted hosts! Retrying " + str(self.r_count) + " more times!")
                                Output.CSPrint("error", "Failed loading trusted hosts! Retrying " + str(self.r_count) + " more times!")
                                time.sleep(3)
                            if VarKeeper.trusted_hosts is not {}:
                                finished = True
                        if VarKeeper.trusted_hosts is not {}:
                            Output.CSPrint("ok", "Successfully loaded trusted hosts!")
                        else:
                            Output.CSPrint("error", "Could not load trusted hosts! Quitting system!")
                            sys.exit(0)
                    else:
                        if uinput is "N":
                            logger.write("w", lloc+"Retrying loading trusted hosts 5 times. After that system will shutdown!")
                            Output.CSPrint("i", "Retrying loading trusted hosts 5 times. After that system will shutdown!")
                            finished = False
                            for i in range(5):
                                if VarKeeper.trusted_hosts is not {}:
                                    break
                                self.r_count = 5 - i
                                try:
                                    Security.loadthosts()
                                except:
                                    logger.write("w", lloc+"Failed loading trusted hosts! Retrying " + str(self.r_count) + " more times!")
                                    Output.CSPrint("error", "Failed loading trusted hosts! Retrying " + str(self.r_count) + " more times!")
                                    time.sleep(3)
                                if VarKeeper.trusted_hosts is not {}:
                                    finished = True
                            if VarKeeper.trusted_hosts is not {}:
                                Output.CSPrint("ok", "Successfully loaded trusted hosts!")
                            else:
                                Output.CSPrint("error", "Could not load trusted hosts! Quitting system!")
                                sys.exit(0)
        Output.CSPrint("ok", "Successfully loaded trusted hosts!")

    def boot_safe(self):
        import logger
        lloc = "File: main.py | Class: Startup | Function: boot_safe | "
        Output.CSPrint("", "Booting into Safe Mode")

    def boot_debug(self):
        import logger
        lloc = "File: main.py | Class: Startup | Function: boot_debug | "
        Output.CSPrint("", "Booting into Debug Mode")


class Multiprocessing:

    def start(self, proc_dict):
        import logger as logger
        import multiprocessing
        proc = proc_dict["proc_object"]
        name = proc_dict["name"]
        security_level = proc_dict["security_level"]
        running_rights = proc_dict["running_rights"]
        try:
            proc.start()
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: start | Could not start proc object!")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: start | Successfully started proc object!")
        procpid = proc.pid
        try:
            tmp = {"name": name, "security_level":security_level, "running_rights":running_rights}
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: start | Could not create tmp dictionary!")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: start | Created tmp dictionary!")
        try:
            VarKeeper.bg_processes[procpid] = tmp
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: start | Could not add proc to Class: VarKeeper | List: bg_processes !")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: start | Added tmp to Class: VarKeeper | List: bg_processes !")
        return True

    def join(self, proc_dict):
        import logger as logger
        import multiprocessing
        proc = proc_dict["proc_object"]
        try:
            proc.join()
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: join | Could not join proc object!")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: join | Successfully joined proc object!")
        return True

    def new(self, function, name, security_level=0, running_rights="norm"):
        import logger as logger
        import multiprocessing
        import time
        try:
            proc = multiprocessing.Process(target=function)
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: new | Could not create proc object!")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: new | Successfully created proc object!")
        try:
            retdict = {"proc_object": proc, "name": name, "security_level":security_level, "running_rights":running_rights}
        except:
            logger.write("e", "File: main.py | Class: Multiprocessing | Function: new | Could not create retdict dictionary!")
            return False
        logger.write("i", "File: main.py | Class: Multiprocessing | Function: new | Created retdict dictionary!")

        return retdict

    def kill(self, name="", pid=0):
        loggerloc = "File: main.py | Class: Multiprocessing | Function: kill | "
        import logger as logger
        import os
        import signal
        import psutil
        import time
        searchfor = None
        if name is not "" and pid is not 0:
            logger.write("ex", loggerloc+"Argument exception: name is not Empty and pid is not Empty !")
            return False
        if name is "" and pid is 0:
            logger.write("ex", loggerloc+"Argument exception: name is Empty and pid is Empty !")
            return False

        if name is not "":
            searchfor = "name"
        if pid is not 0:
            searchfor = "pid"
        if searchfor is "name":
            logger.write("i", loggerloc+"Searching in Class: VarKeeper | List: bg_processes for "+name)
        if searchfor is "pid":
            logger.write("i", loggerloc+"Searching in Class: VarKeeper | List: bg_processes for "+pid)
        for item in VarKeeper.bg_processes:
            tmp = VarKeeper.bg_processes[item]
            if searchfor is "name":
                if tmp["name"] is name:
                    procpid = item
                    logger.write("i", loggerloc+"Got Process PID: "+str(procpid))
                    try:
                        p = psutil.Process(pid)
                        p.terminal()
                    except:
                        time.sleep(1.3)
                        try:
                            p = psutil.Process(pid)
                            p.terminal()
                        except:
                            logger.write("e", loggerloc+"Could not kill Process: "+str(procpid))
                            return False
                    logger.write("i", loggerloc+"Successfully killed Process: "+str(procpid))
                    try:
                        VarKeeper.bg_processes.pop(procpid, None)
                    except:
                        logger.write("e", loggerloc+"Could not remove Process from Class: VarKeeper | List: bg_processes !")
                        return False
                    return True
            if searchfor is "pid":
                if item is pid:
                    try:
                        p = psutil.Process(pid)
                        p.terminal()
                    except:
                        time.sleep(0.3)
                        try:
                            p = psutil.Process(pid)
                            p.terminal()
                        except:
                            logger.write("e", loggerloc+"Could not kill Process: "+str(pid))
                            return False
                    logger.write("i", loggerloc+"Successfully killed Process: "+str(pid))
                    try:
                        VarKeeper.bg_processes.pop(pid, None)
                    except:
                        logger.write("e", loggerloc+"Could not remove Process from Class: VarKeeper | List: bg_processes !")
                        return False
                    return True
        if name is not "":
            logger.write("e", loggerloc+"Could not find name: "+name+" in Class: VarKeeper | List: bg_processes !")
            return False
        if pid is not "":
            logger.write("e", loggerloc+"Could not find pid: "+str(pid)+" in Class: VarKeeper | List: bg_processes !")
            return False


class Security:

    def savekey(self, key):
        print "Skey: "+key
        import logger as logger
        loggerloc = "File: main.py | Class: Security | Function: savekey | "
        logger.write("i", loggerloc+"Start saving security key!")
        try:
            keyfile = open("../settings/keyfile.cfg", "w")
        except:
            logger.write("e", loggerloc+"Could not open /setting/keyfile.cfg !")
            return False
        try:
            keyfile.write(str(key))
        except:
            logger.write("e", loggerloc+"Could not write key to file /setting/keyfile.cfg !")
            return False
        keyfile.close()
        logger.write("i", loggerloc+"Written key to file /setting/keyfile.cfg")
        return True

    def loadkey(self):
        import logger as logger
        loggerloc = "File: main.py | Class: Security | Function: loadkey | "
        logger.write("i", loggerloc+"Start loading security key!")
        try:
            keyfile = open("../settings/keyfile.cfg", "r")
        except:
            logger.write("e", loggerloc+"Could not open /setting/keyfile.cfg !")
            return False
        try:
            key = keyfile.read()
        except:
            logger.write("e", loggerloc+"Could not read file /setting/keyfile.cfg !")
            return False
        logger.write("i", loggerloc+"Loaded key from file /setting/keyfile.cfg")
        return key

    def newkey(self):
        import logger as logger
        import cryptographer as cr
        loggerloc = "File: main.py | Class: Security | Function: newkey | "
        logger.write("i", loggerloc+"Generating new security key!")
        try:
            key = cr.newkey()
        except:
            logger.write("e", loggerloc+"Could not generate new key!")
            return False
        return key

    def loadthosts(self):
        import logger as logger
        loggerloc = "File: main.py | Class: Security | Function: loadthosts | "
        logger.write("i", loggerloc+"Start loading trusted hosts!")
        try:
            keyfile = open("../settings/trusted_hosts.cfg", "r")
        except:
            logger.write("e", loggerloc+"Could not open /setting/trusted_hosts.cfg !")
            return False
        try:
            for line in keyfile:
                list = line.split(":")
                ip = list[0]
                name = list[1]
                VarKeeper.trusted_hosts[ip] = name
        except:
            logger.write("e", loggerloc+"Could not loop through thosts file | or | Could not add host with name to Class: VarKeeper | Dictionary: trusted_hosts !")
            return False
        logger.write("i", loggerloc+"Successfully loaded trusted hosts from file!")


class Handler:

    def socket_remote_access_command_handler(self, recv_data, conn, s_key):
        import main
        import logger
        import cryptographer as cr
        loggerloc = "File: main.py | Class: Handler | Function: socket_remote_access_command_handler | "
        tmp = str(recv_data)
        recv_data = tmp
        recv_data = recv_data.split(";")
        sender = recv_data[0]
        command = recv_data[1]
        args = recv_data[2]
        sender = sender.strip("[")
        sender = sender.strip("]")
        command = command.strip("[")
        command = command.strip("]")
        args = args.strip("[")
        args = args.strip("]")
        args = args.split(", ")
        logger.write("i", loggerloc+"Successfully split received data! Sender: "+str(sender)+" | Command: "+str(command)+" | Args: "+str(args))

        if command is "test":
            main.Output.CSPrint("info", "Recv Data: ["+str(sender)+":"+str(command)+":"+str(args))
            etext = cr.encrypt(s_key, "[send];[Successfully sent test!];[debug]")
            conn.send(etext)

    def socket_remote_access_connection_handler(self, conn, s_key):
        import logger
        import cryptographer as cr
        import main
        loggerloc = "File: main.py | Class: Handler | Function: socket_remote_access_connection_handler | "
        logger.write("i", loggerloc+"Started new connection handler!")
        logger.write("i", loggerloc+"Waiting for client to authenticate!")
        authenticated = False
        text = "[send];[Please authenticate with username:password !];[info]"
        text = cr.encrypt(s_key, text)
        conn.send(text)
        while authenticated is False:
            edata = conn.recv(15360)
            if edata is "123":
                authenticated = True
        while True:
            edata = conn.recv(15360)
            logger.write("i", loggerloc+"Received data! Decrypting it! Data: "+str(edata))
            try:
                ddata = cr.decrypt(s_key, edata)
            except:
                logger.write("e", loggerloc+"Could not decrypt data: "+str(edata))
                conn.send("[send];[Server was not able to decrypt sent data!];[error]")
            logger.write("i", loggerloc+"Handing over decrypted data to socket_remote_access_command_handler! Data: "+str(ddata))
            Handler.socket_remote_access_command_handler(ddata, conn, VarKeeper.s_key)


class BG_Functions:

    def input_system_console(self):
        import termcolor
        import time
        self.version_string = "       |   Version: " + VarKeeper.version + ""
        for i in range(67 - len(VarKeeper.version)):
            self.version_string = self.version_string + " "
        self.version_string = self.version_string + "|"
        self.curruser_string = "       |   Current User: " + VarKeeper.current_user + ""
        for i in range(62 - len(VarKeeper.current_user)):
            self.curruser_string = self.curruser_string + " "
        self.curruser_string = self.curruser_string + "|"
        self.time = time.strftime("%H:%M:%S") + " | " + time.strftime("%d/%m/%Y")
        self.time_string = "       |   Current Time: " + self.time
        for i in range(62 - len(self.time)):
            self.time_string = self.time_string + " "
        self.time_string = self.time_string + "|"
        print ""
        print ""
        print ""
        print ""
        print "        /=============================================================================\ "
        print "       |                                                                               |"
        print "       |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |"
        print "       |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |"
        print "       |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |"
        print "       |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |"
        print "       |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |"
        print "       |                                                                               |"
        print "       |       _                    _ _                                                |"
        print "       |      / \    _____   _ _ __(_) |_ ___                                          |"
        print "       |     / _ \  |_  / | | | '__| | __/ _ \                                         |"
        print "       |    / ___ \  / /| |_| | |  | | ||  __/                                         |"
        print "       |   /_/   \_\/___|\__,_|_|  |_|\__\___|                                         |"
        print "       |                                                                               |"
        print "" + self.version_string
        print "       |                                                                               |"
        print "       |                                                                               |"
        print "" + self.time_string
        print "       |                                                                               |"
        print "" + self.curruser_string
        print "       |                                                                               |"
        print "        \=============================================================================/ "
        print ""
        print ""
        print ""
        print ""
        while True:
            user_input = raw_input("Azurite:"+VarKeeper.console_currdir + " " + VarKeeper.current_user + "$ ")

    def socket_remote_access_listener(self, host="127.0.0.1", port=23778, maxconns=3):
        import logger as logger
        import socket
        loggerloc = "File: main.py | Class: BG_Functions | Function: socket_remote_access_listener | "
        logger.write("i", loggerloc+"Starting socket_remote_access_listener!")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            logger.write("e", loggerloc+"Could not create sock object!")
            return False
        logger.write("i", loggerloc+"Created sock object!")
        try:
            sock.bind((host, port))
        except socket.error as msg:
            logger.write("e", loggerloc+"Could not bind socket! ERROR Code: "+str(msg[0])+" Message: "+str(msg[1]))
            return False
        logger.write("i", loggerloc+"Bound socket!")
        try:
            sock.listen(maxconns)
        except:
            logger.write("e", loggerloc+"Socket is not listening!")
            return False
        logger.write("i", loggerloc+"Socket is now listening!")
        while True:
            conn, addr = sock.accept()
            logger.write("w", loggerloc+"Socket connection from: "+addr[0]+':'+str(addr[1]))
            Multiprocessing.new(Handler.socket_remote_access_connection_handler(conn, VarKeeper.s_key), "SocketConn["+str(addr[0])+":"+str(addr[1])+"]", security_level=3,running_rights="sockconn")


class Azurite_Script:
    # !!
    # !! FINISH run function
    # !!
    def run(self, location):
        import logger as logger
        import os
        import psutil
        import sys
        loggerloc = "File: main.py | Class: Azurite_Script | Function: run | "
        logger.write("i", loggerloc+"Running Script: "+location)
        try:
            script = open(location, "r")
        except:
            logger.write("e", loggerloc+"Could not open script "+location+" in reading mode!")
            return False

        for line in script:
            if line is "":
                pass
            else:
                if line[0] is "#":
                    pass
                else:
                    pass


VarKeeper = VarKeeper()
Output = Output()
Startup = Startup()
Multiprocessing = Multiprocessing()
Security = Security()
Handler = Handler()
BG_Functions = BG_Functions()
Azurite_Script = Azurite_Script()



# !!
# !!     Testing! Remove bottom later     !!
# !!


#def test1(e):
#    for i in range(7):
#        print e
#
#def test2(e):
#    for i in range(7):
#        print e
#
#Multiprocessing.new(test1("Proc 1"), "Test1", security_level=1, running_rights="super")
#Multiprocessing.new(test2("Proc 2"), "Test2", security_level=1, running_rights="super")
#print VarKeeper.bg_processes
#
#import time
#time.sleep(2)
#Multiprocessing.kill(name="Test1")
#print VarKeeper.bg_processes
#Multiprocessing.kill(name="Test2")
#print VarKeeper.bg_processes