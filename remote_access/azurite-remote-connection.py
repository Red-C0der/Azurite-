__author__ = 'Red_C0der'

import socket
import sys
import time
import multiprocessing
import cryptographer as cr
import termcolor
from colored import fg, bg, attr, style

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
def CSPrint(state, message):
        import termcolor
        from colored import fg, bg, attr, style
        if state == "":
            print("[....] " + message)
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

CSPrint("info", "Starting Azurite Remote Connection")
CSPrint("info", "Loading Security Key")

try:
    kfile = open("keyfile.cfg", "r")
except:
    CSPrint("error", "Could not open keyfile.cfg !")
    sys.exit(0)

try:
    s_key = kfile.read()
except:
    CSPrint("error", "Could not read keyfile.cfg !")
    sys.exit(0)

CSPrint("i", "Loaded Security Key!")
CSPrint("", "Starting socket")
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    CSPrint("error", "Could not create socket object!")
    sys.exit(0)

CSPrint("info", "Please enter Server information! ( serverip;port )")

while True:
    sinfo = raw_input("=> ")
    if ";" in sinfo:
        sinfo = sinfo.split(";")
        host = sinfo[0]
        port = sinfo[1]
        break
    else:
        CSPrint("error", "Please enter Server information with ; ! ( serverip;port )")

CSPrint("", "Connecting to "+str(host)+":"+str(port))
i = 0
tmp = False
while i <= 5:
    try:
        socket.connect((host, int(port)))
        tmp = True
        break
    except:
        CSPrint("error", "Could not connect to Server ["+str(host)+":"+str(port)+"] ! Retrying in 5 sek")
        time.sleep(5)

if tmp is False:
    CSPrint("error", "Could not connect to Server ["+str(host)+":"+str(port)+"] ! Please check if server is online and internet connection is stable!")
    sys.exit(0)

sendlock = False

def listener():
    while True:
        edata = socket.recv(15360)
        print "Edata: "+str(edata)
        if edata is not None:
            ddata = cr.decrypt(s_key, edata)
            print "Got: "+ddata
            string = ddata.split(";")
            action = string[0]
            message = string[1]
            state = string[2]

            action = action.strip("[")
            action = action.strip("]")
            message = message.strip("[")
            message = message.strip("]")
            state = state.strip("[")
            state = state.strip("]")

            print "Message: "+message
            print "State: "+state
            print "Action: "+action

            if action is "recv":
                sendlock = True
            if action is "send":
                sendlock = False
            if action is not "recv" and action is not "send":
                CSPrint("error", "Received corrupted data! Data: "+str(ddata))
            else:
                if message is "":
                    CSPrint("error", "Received corrupted data! Data: "+str(ddata))
                else:
                    if state is "":
                        CSPrint("", message)
                    if state is "ok":
                        CSPrint("ok", message)
                    if state is "error":
                        CSPrint("error", message)
                    if state is "warning":
                        CSPrint("warning", message)
                    if state is "info":
                        CSPrint("info", message)
                    if state is "debug":
                        CSPrint("debug", message)
                    if state is "sys":
                        CSPrint("sys", message)


def sender():
    while True:
        send = raw_input("=> ")
        edata = cr.encrypt(s_key, send)
        if sendlock is False:
            socket.send(edata)
        else:
            CSPrint("info", "SendLock is acquired ! Please resend in a few seconds!")

listenerproc = multiprocessing.Process(target=listener())
listenerproc.start()
listenerproc.join()

sender()
