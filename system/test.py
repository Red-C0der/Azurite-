__author__ = 'Maximilian_H'

import main
import time
import cryptographer as cr
import voicehandler as voice

voicedb = voice.LoadVoiceDB()
print ""
print ""
print ""

for i in range(20):
    print "Recording"
    voice.RecWaveFile(i)
    print "Analyzing"
    voice.GetSpeakers(voicedb, "../tmp/"+str(i)+".wav")
    times.sleep(4)
    print "Cleanup"
    voice.CleanUp(str(i))
    time.sleep(4)
    print "New File"
#voice.ReadWaveFile("voice.wav")

#print voice.GetSpeakers(voicedb, "voice.wav")
#voice.CleanUp("voice")


#main.Startup.startup()

#main.VarKeeper.s_key = main.Security.loadkey()
#print "SKey: "+str(main.VarKeeper.s_key)
#main.Security.loadthosts()
#print "THosts: "+str(main.VarKeeper.trusted_hosts)
#console = main.Multiprocessing.new(main.BG_Functions.input_system_console(), "Console")
#sock_remote_listener_dict = main.Multiprocessing.new(main.BG_Functions.socket_remote_access_listener(), "SocketRemoteAccessListener")

#main.Multiprocessing.start(console)
#main.Multiprocessing.join(console)