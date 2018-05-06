students = []#储存学生信息
flga = True
while flga:
    print('添加学生!')
    choose = int(input('请根据提示选择相关操作:\n1.添加学生\n2.查找学生\n3.修改学生\n4.删除学生\n'))
    if choose == 1:
        add_name = input('输入学生姓名:\n')
        add_age = int(input('输入学生年龄;\n'))
        add_QQ = input('请输入你的QQ:\n')
        student = {'name': add_name, 'age': add_age, 'QQ': add_QQ}
        students.append(student)
        print(students)
    elif choose == 2:
        print('查询学生!')
        query_name = input('请输入查询学生姓名:\n')
        for student in students:
            if student.get('name') == query_name:
                print('学生姓名: {}, 学生年龄: {}, 学生QQ: {} '.format(query_name, student.get('age'), student.get('QQ')))
            else:
                print('查无此人')
    elif choose == 3:
        print('修改学生!')
        up_name = input('请输入要修改的学生姓名:\n')
        for student in students:
            if student.get('name') == up_name:
                new_name = input('请输入修改的学生姓名:\n')
                new_age = int(input('请输入修改的学生年龄:\n'))
                new_QQ = input('请输入修改的学生QQ:\n')
                student.update(name=new_name, age=new_age, QQ=new_QQ)
                print('修改成功')
                print('修改后学生姓名{}修改后的学生年龄{}修改后的学生QQ{}'.format(up_name, new_age, new_QQ))
    elif choose == 4:
        print('删除学生!')
        out_name = input('要删除学生姓名:\n')
        for student in students:
            if student.get('name') == out_name:
                students.remove(student)
                print(students)
    else:
        print('退出系统')
        flga = False
