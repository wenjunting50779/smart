import websocket
import json
import time
from motor.motor import Motor


# 连接主服务器  如果连接成功，执行指令  依赖 websocket-client 第三方包


def start():
    ws = websocket.create_connection("ws://192.168.33.10:9502")
    req = {"terminal ": "smart_car"}
    ws.send(json.dumps(req))
    while True:
        time.sleep(1)
        res = ws.recv()
        ws.send('execute')
        print(res)
    ws.close()


def advance():

    """前进"""
    return ''


def retreat():
    """后退"""
    return ''


def left():
    """左转"""
    return ''


def right():
    """右转"""
    return ''


def stop():
    """停止"""
    return ''


def lock():
    """刹车"""
    return ''


#start()

def test():
    motor = Motor()
    motor.advance()
    motor.stop()
    motor.retreat()
    motor.right()
    motor.left()


test()



