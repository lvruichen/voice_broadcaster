#!/home/eric/miniconda3/envs/torch/bin/python
from concurrent.futures import thread
from lib2to3.pgen2.token import VBAR
import rospy
from voice_broadcast import *
import threading
import sys
import signal

def quit(signal_num,frame):
    print ("you stop the threading")
    sys.exit()

if __name__ == '__main__':
    rospy.init_node('voice_broadcast_node',)
    vb = VoiceBroadcaster()
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        t1 = threading.Thread(target=vb.run)
        t1.setDaemon(True)
        t1.start()
        while True:
            pass
    except KeyboardInterrupt as e:
        print('you have stopped the thread')



