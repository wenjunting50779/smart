import RPi.GPIO as GPIO
import time
# 超声波测距脚本
# 设置引脚编码方式
GPIO.setmode(GPIO.BOARD)
# 设置31引脚为输出
GPIO.setup(31, GPIO.OUT)
# 设置31引脚为输入
GPIO.setup(33, GPIO.IN)

# 输出1us的高电平信号
GPIO.output(31, True)
time.sleep(0.00001)  # 1us
GPIO.output(31, False)

# 监听ECHO口输出信息，如果是低电平则忽略，反之记录高电平开始的时间
while GPIO.input(33) == 0:
    pass
start = time.time()

# 如果是高电平则忽略，反之记录高电平结束的时间
while GPIO.input(33) == 1:
    pass
end = time.time()

# 计算距离
distance = round((end - start) * 343 / 2 * 100)

print(distance)
