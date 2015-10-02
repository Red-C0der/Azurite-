__author__ = 'Red_C0der'

def write(level, message, LogFile=""):
    import logging
    if LogFile == "":
        from time import gmtime, strftime
        LogName = strftime("%d-%m-%Y", gmtime())
        LogLoc = "../logs/"
        LogF = LogLoc+LogName+".log"
    else:
        LogF = LogFile
    logging.basicConfig(filename=LogF, level=logging.DEBUG, format='%(asctime)s | %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
    if level == "i":
        logging.info(message)
    if level == "w":
        logging.warning(message)
    if level == "e":
            logging.error(message)
    if level == "c":
        logging.critical(message)
    if level == "ex":
        logging.exception(message)
    if level == "d":
        logging.debug(message)
    if level != "i" and level != "w" and level != "e" and level != "c" and level != "ex" and level != "d":
        import inspect
        logging.exception("Function " + inspect.stack()[1][3] + " tried to use logger.write() with invalid logging level " + level +  " !")