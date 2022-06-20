# voice_broadcaster
this is a ros package for broadcasting voice

To launch the node, run the following cmd, this will play the Do note by default
```
roslaunch voice_broadcaster voiceplay.launch  
```
rosservice call /VoiceChange "{stop_flag: True, change_flag: False, wav_name: 'Re.wav', circle_time: 5, volume: 80}" 
- stop_flag: stop playing or continue playing
- change_flag: change the music(wav_name) and replay (circle_time) times
- volume: change the volume of music

