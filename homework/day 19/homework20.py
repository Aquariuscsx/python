class Stud:
    total = 0  # 总分
    nums = 0  # 总人数
    student = [{'no': 1, 'name': 'xm', 'grade': 80},
               {'no': 2, 'name': 'xm', 'grade': 80},
               {'no': 3, 'name': 'xm', 'grade': 90},
               {'no': 4, 'name': 'xm', 'grade': 20},
               {'no': 5, 'name': 'xm', 'grade': 35}]

    def __init__(self, no, name, grade):
        self.no = no
        self.name = name
        self.grade = grade

    @classmethod
    def totals(cls):
        for deg in cls.student:
            for nos in deg:
                if nos == 'no':
                    cls.nums += 1
        print(cls.nums)

    @classmethod
    def avg(cls):
        for deg in cls.student:
            for degs in deg.values():
                if degs == deg.get('grade'):
                    cls.total += degs
        print(cls.total)

    @classmethod
    def show(cls):
        print(cls.total / cls.nums)


if __name__ == '__main__':
    Stud.totals()
    Stud.avg()
