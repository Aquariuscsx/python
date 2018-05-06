class Cars:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def move(self):
        print('开始移动!')

    def stop(self):
        print('停止移动!')

class Bike(Cars):
    def __init__(self, color, speed, kind):
        Cars.__init__(self, color, speed )
        self.kind = kind

    def repair(self):
        print('%s在修理'% self.kind)

class Roadster(Cars):
    def __init__(self, color, speed, kind):
        Cars.__init__(self,color, speed)
        self.kind = kind

    def game(self):
        print('{}在比赛'.format(self.kind))

if __name__ == '__main__':
    cars = Cars('红色', '200km/s')
    bike = Bike('黄色','20km/s', '自行车')
    roadster = Roadster('红色', '300km/s', '跑车')
    bike.repair()
    bike.stop()