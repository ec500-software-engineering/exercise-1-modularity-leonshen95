import random

class heart_rateSensor(object):
    @staticmethod
    def get_heart_rate():
        return random.randint(70,140)

class heart_o2Sensor(object):
    @staticmethod
    def get_heart_o2():
        return random.randint(0,100)

class body_tempSensor(object):
    @staticmethod
    def get_body_temp():
        return  random.randint(30,40)
