# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'


#       Voice Differentiation

def LoadVoiceDB(path="../voicedb"):
    from voiceid.sr import Voiceid
    from voiceid.db import GMMVoiceDB
    import logger
    try:
        db = GMMVoiceDB(str(path))
    except:
        logger.write("e", "File: voicehandler.py | Function: LoadVoiceDB | Error: Could not create db object / Could not create database in given directory!")
        return False
    logger.write("i", "File: voicehandler.py | Function: LoadVoiceDB | Info: New VoiceDatabase was created!")
    return db

def AddWaveFile(voicedb, Speaker_Name, WavFile_Path, db_path="../voicedb"):
    from voiceid.sr import Voiceid
    from voiceid.db import GMMVoiceDB
    import logger
    try:
        voicedb.add_model(WavFile_Path, Speaker_Name)
    except:
        logger.write("e", "File: voicehandler.py | Function: AddWaveFile | Error: Could not add speaker to database!")
        return False
    return True

def PrintDatabase(voicedb):
    from voiceid.sr import Voiceid
    from voiceid.db import GMMVoiceDB
    import logger
    try:
        return voicedb.get_speakers()
    except:
        logger.write("e", "File: voicehandler.py | Function: PrintDatabase | Error: Could not return or get voicedb dictionary!")
        return False

def GetSpeakers(voicedb, audiofile):
    from voiceid.sr import Voiceid
    from voiceid.db import GMMVoiceDB
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
        for c in v.get_clusters():
            cluster = v.get_cluster(c)
            print "Best Speaker: "+cluster.get_best_speaker()
            voicedb.set_maxthreads(5)
    except:
        logger.write("e", "File: voicehandler.py | Function: GetSpeakers | Error: Could not list cluster segments into cluster_dict !")
        return False
    return cluster

def CleanUp(audiofile_no_suffix, file_suffix=".wav"):
    import os
    import logger
    try:
        os.system("rm "+audiofile_no_suffix+file_suffix)
        os.system("rm "+audiofile_no_suffix+"_"+file_suffix)
        os.system("rm "+audiofile_no_suffix+"_"+".seg")
        os.system("rm "+audiofile_no_suffix+"_.c.gmm")
        os.system("rm -rf "+audiofile_no_suffix+"_")
    except:
        logger.write("e", "File: voicehandler.py | Function: CleanUp | Error: Something went wrong during cleanup!")
        return False
    return True


#       Voice Recognition

def ReadWaveFile(audiofile, google_api_key=""):
    import speech_recognition as sr
    from os import path
    WAV_FILE = path.join(path.dirname(path.realpath(__file__)), audiofile)
    r = sr.Recognizer()
    with sr.WavFile(WAV_FILE) as source:
        audio = r.record(source)
        #audio = r.listen(source)
    try:
        if google_api_key == "":
            return r.recognize_google(audio)
        else:
            return r.recognize_google(audio, key=google_api_key)
    except sr.UnknownValueError:
        return "audio=null"
        #print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        return "request=error"
        #print("Could not request results from Google Speech Recognition service; {0}".format(e))

def RecWaveFile(file_name_no_suffix):
    import os
    try:
        os.system("arecord -f cd -d 3 -t raw | lame -x -r – ../tmp/"+file_name_no_suffix+".mp3")
        os.system("mpg123 -w ../tmp/"+file_name_no_suffix+".wav ../tmp/"+file_name_no_suffix+".mp3")
    except:
        return False
    return True