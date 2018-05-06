class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade

class Worker(Person):
    def __init__(self, name, age, salary,job_content):
        Person.__init__(self, name, age)
        self.salary = salary
        self.job_content = job_content

    def show(self):
        print(self.name, self.age, self.salary,self.job_content)

if __name__ == '__main__':
    person = Person('李鹏', '38岁')
    student = Student('周勇', '48岁', 60)
    worker = Worker('王震', '25岁', '工资:1888', '工作:搬水泥')
    worker.show()