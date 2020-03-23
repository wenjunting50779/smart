#import RPi.GPIO as GPIO


class Motor:
    """
        电机控制类
    """
    # 左边电机
    motor_left1 = 12
    motor_left2 = 16
    motor_left3 = 18
    motor_left4 = 22

    # 右边电机
    motor_right1 = 7
    motor_right2 = 11
    motor_right3 = 13
    motor_right4 = 15

    """
    设置引脚
    """
    def __init__(self):
        """
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor_left1, GPIO.OUT)
        GPIO.setup(self.motor_left2, GPIO.OUT)
        GPIO.setup(self.motor_left3, GPIO.OUT)
        GPIO.setup(self.motor_left4, GPIO.OUT)
        GPIO.setup(self.motor_right1, GPIO.OUT)
        GPIO.setup(self.motor_right2, GPIO.OUT)
        GPIO.setup(self.motor_right3, GPIO.OUT)
        GPIO.setup(self.motor_right4, GPIO.OUT)
         """
        print('set init')


    """
     前进
    """
    def advance(self):
        """
            #前面电机正转
        GPIO.output(self.motor_right1, GPIO.LOW)
        GPIO.output(self.motor_right2, GPIO.HIGH)
        GPIO.output(self.motor_left1, GPIO.LOW)
        GPIO.output(self.motor_left2, GPIO.HIGH)
        # 后面电机正转
        GPIO.output(self.motor_right3, GPIO.LOW)
        GPIO.output(self.motor_right4, GPIO.HIGH)
        GPIO.output(self.motor_left3, GPIO.LOW)
        GPIO.output(self.motor_left4, GPIO.HIGH)
        :return:
        """
        print('前进')


    def stop(self):
        """
        # 前面电机停止
        GPIO.output(self.motor_right1, GPIO.LOW)
        GPIO.output(self.motor_right2, GPIO.LOW)
        GPIO.output(self.motor_left1, GPIO.LOW)
        GPIO.output(self.motor_left2, GPIO.LOW)
        # 后面电机停止
        GPIO.output(self.motor_right3, GPIO.LOW)
        GPIO.output(self.motor_right4, GPIO.LOW)
        GPIO.output(self.motor_left3, GPIO.LOW)
        GPIO.output(self.motor_left4, GPIO.LOW)
         """
        print('停止')

    def retreat(self):
        """
        #前面电机反转
        GPIO.output(self.motor_right1, GPIO.HIGH)
        GPIO.output(self.motor_right2, GPIO.LOW)
        GPIO.output(self.motor_left1, GPIO.HIGH)
        GPIO.output(self.motor_left2, GPIO.LOW)
        # 后面电机反转
        GPIO.output(self.motor_right3, GPIO.HIGH)
        GPIO.output(self.motor_right4, GPIO.LOW)
        GPIO.output(self.motor_left3, GPIO.HIGH)
        GPIO.output(self.motor_left4, GPIO.LOW)
         """
        print('后退')

    """
        左转
    """
    def left(self):
        """
        #左侧电机反转
        GPIO.output(self.motor_left1, GPIO.HIGH)
        GPIO.output(self.motor_left2, GPIO.LOW)
        GPIO.output(self.motor_left3, GPIO.HIGH)
        GPIO.output(self.motor_left4, GPIO.LOW)
        """
        print('左转')


    """
        右转
    """
    def right(self):
        """
        #右侧电机反转
        GPIO.output(self.motor_right1, GPIO.HIGH)
        GPIO.output(self.motor_right2, GPIO.LOW)
        GPIO.output(self.motor_right3, GPIO.HIGH)
        GPIO.output(self.motor_right4, GPIO.LOW)
        """
        print('右转')





