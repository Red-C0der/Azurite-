__author__ = 'Red_C0der'

def LoadVoiceDB(path="../voicedb"):
    #from voiceid.sr import Voiceid
    #from voiceid.db import GMMVoiceDB
    import logger
    try:
        db = GMMVoiceDB(str(path))
    except:
        logger.write("e", "File: voicehandler.py | Function: LoadVoiceDB | Error: Could not create db object / Could not create database in given directory!")
        return False
    logger.write("i", "File: voicehandler.py | Function: LoadVoiceDB | Info: New VoiceDatabase was created!")
    return db

def AddWaveFile(voicedb, Speaker_Name, WavFile_Path, db_path="../voicedb"):
    #from voiceid.sr import Voiceid
    #from voiceid.db import GMMVoiceDB
    import logger
    try:
        voicedb.add_model(WavFile_Path, Speaker_Name)
    except:
        logger.write("e", "File: voicehandler.py | Function: AddWaveFile | Error: Could not add speaker to database!")
        return False
    return True

def PrintDatabase(voicedb):
    #from voiceid.sr import Voiceid
    #from voiceid.db import GMMVoiceDB
    import logger
    try:
        return voicedb.get_speakers()
    except:
        logger.write("e", "File: voicehandler.py | Function: PrintDatabase | Error: Could not return or get voicedb dictionary!")
        return False

def GetSpeakers(voicedb, audiofile):
    #from voiceid.sr import Voiceid
    #from voiceid.db import GMMVoiceDB
    import logger
    try:
        v = Voiceid(voicedb, audiofile)
    except:
        logger.write("e", "File: voicehandler.py | Function: GetSpeakers | Error: Could not call Voiceid constructor!")
        return False
    try:
        v.extract_speakers()
    except:
        logger.write("e", "File: voicehandler.py | Function: GetSpeakers | Error: Could not extract speakers from file!")
        return False
    try:
        cluster_dict = {}
        for c in v.get_clusters():
            cluster = v.get_cluster(c)
            segments = cluster.print_segments()
            cluster_dict[cluster] = segments
    except:
        logger.write("e", "File: voicehandler.py | Function: GetSpeakers | Error: Could not list cluster segments into cluster_dict !")
        return False
    return cluster_dict