from microbit import *
#write your program:
import music
length=10
for freq in range(880,1760,16):
  music.pitch(freq,length)# freq为蜂鸣器频率，length为次数