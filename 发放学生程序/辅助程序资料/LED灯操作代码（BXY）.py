from microbit import *
#write your program: 
# 呼吸灯案例
while True:
  pin14.write_digital(1)   # pin14口置高电平，LED灯亮
  sleep(1000)
  pin14.write_digital(0)   # pin14口置低电平，LED灯灭
  sleep(1000)