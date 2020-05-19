# -*-coding:utf-8-*-
# 树莓派远程控制小车
import RPi.GPIO as GPIO
import websocket
import json
import threading
import time

action = 'stop'


def socket_client():
    ws = websocket.create_connection("ws://192.168.33.10:9511")
    req = {"terminal": "smart_car"}
    ws.send(json.dumps(req))
    while True:
        res = ws.recv()
        res = json.loads(res)
        if res.__contains__('action') and res.__contains__('err_code') and res['err_code'] == 0:
            print(res['action'])
            global action
            action = res['action']
            if res['action'] == 'back':
                GPIO.output(35, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                speed(30)
            elif res['action'] == 'forward':
                GPIO.output(37, GPIO.LOW)
                GPIO.output(35, GPIO.HIGH)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                speed(30)
            elif res['action'] == 'stop':
                speed(0)
            elif res['action'] == 'right':
                GPIO.output(35, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(18, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                speed(40)
            elif res['action'] == 'left':
                GPIO.output(35, GPIO.HIGH)
                GPIO.output(37, GPIO.LOW)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(15, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                speed(40)
            else:
                print('error')

    ws.close()


def check():
    while True:
        global action
        distance = Measure()
        if (distance < 10 or GPIO.input(3) == 0) and action == 'forward':
            speed(0)
        elif action == 'forward' and 10 < distance < 30:
            speed(20)
        else:
            pass


# 多线程执行
class EventThread(threading.Thread):
    def run(self):
        print('thread')
        socket_client()


class CheckThread(threading.Thread):
    def run(self):
        print('check')
        check()


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    #
    GPIO.setup(3, GPIO.IN)
    # 超声模块
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.IN)
    print('init...')


def Measure():
    # send
    GPIO.output(31, True)
    time.sleep(0.00001)  # 1us
    GPIO.output(31, False)

    # start recording
    while GPIO.input(33) == 0:
        pass
    start = time.time()

    # end recording
    while GPIO.input(33) == 1:
        pass
    end = time.time()

    # compute distance
    distance = round((end - start) * 343 / 2 * 100)
    return distance


# exit
def upload():
    GPIO.output(11, GPIO.LOW)
    GPIO.cleanup()
    print('exit...')


def speed(s):
    p.ChangeDutyCycle(s)


#   初始化引脚
init()

# 初始速度
p = GPIO.PWM(11, 100)
p.start(0)

eventThread = EventThread()
eventThread.start()

checkThread = CheckThread()
checkThread.start()
