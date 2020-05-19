import RPi.GPIO as GPIO
import time
# 获取红外避障模块的输入信号
# 设置引脚模式
GPIO.setmode(GPIO.BOARD)
# 设置引脚11 作为信号输入
GPIO.setup(11, GPIO.IN)
while (True):
    time.sleep(1)
    print(GPIO.input(11))
