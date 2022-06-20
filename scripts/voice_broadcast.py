#!/home/eric/miniconda3/envs/torch/bin/python
import rospy
from subprocess import call
from voice_broadcaster.srv import VoiceChange, VoiceChangeRequest, VoiceChangeResponse
import threading
from threading import Thread, Lock
import time
from sound_play.libsoundplay import SoundClient
import os
import subprocess

class VoiceBroadcaster:
    def __init__(self) :
        self.parent_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'resources')
        self.wav_file = 'Do.wav'
        self.wav_base = 'Do.wav'
        self.sound_server = rospy.Service('VoiceChange', VoiceChange, self.doReq)
        self.stop_flag = False
        self.change_flag = False
        self.circle_time = 0
        self.volume = 70
    def doReq(self, req):
        self.stop_flag = req.stop_flag
        self.volume = max(req.volume, 20)

        if req.change_flag:
            self.wav_file = req.wav_name
            self.circle_time = max(req.circle_time, 1)
        subprocess.run(['amixer', 'set', '-c', '1', 'Master',  str(self.volume)])
        resp = VoiceChangeResponse()
        resp.status = 0
        resp.message = 'ok'
        return resp

    def run(self):
        sound_client = SoundClient()
        rospy.sleep(1)
        while  not rospy.is_shutdown():
            if not self.stop_flag:
                print('thread is running')
                if self.circle_time:
                    sound_tmp = sound_client.waveSound(os.path.join(self.parent_path, self.wav_file), self.volume)
                    sound_tmp.play()
                    self.circle_time -= 1
                else:
                    sound_base = sound_client.waveSound(os.path.join(self.parent_path, self.wav_base), self.volume)
                    sound_base.play()
            time.sleep(1)



