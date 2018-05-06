
print('全国高等学生管理系统')
print('1,添加\n')
print('2,查询\n')
print('3,修改\n')
print('4,删除\n')
print('退出\n')
dict = {}#建立空字典
flag = True
students = []
while flag:
    choose = int(input('请根据提示选择相关的操作:\n'))
    if choose == 1:
        print('添加学生')
        add_name = input('请输入学生姓名:\n')
        add_age = int(input('请输入学生年龄:\n'))
        add_qq = input('请输入学生QQ:\n')
        student = {'name':add_name,'age': add_age,'qq': add_qq}
        students.append(student)
    elif choose == 2:
        print('查询学生')
        query_name = input('请输入查询学生姓名:')
        for student in students:
            if student.get('name') == query_name:
                print('学生姓名: {}\n学生年龄\n{}学生qq{}\n'.format(query_name,student.get('age'),student.get('qq')))#get 就是获取value的值
            else:
                print('查无此人')
                flag = False
    elif choose == 3:
        print('修改学生:')
        alter_name = input('请输入要修改的学生姓名')
        for student in students:
            if student.get('name') == alter_name:
                new_name = input('请输入新的学生姓名:')
                new_age = int(input('请输入新的学生年龄:'))
                new_qq = input('请输入新的学生qq:')
                student.update(name = new_name,age = new_age,qq = new_qq)
                print('修改成功')
                print('修改完成!\n学生姓名:new_name\n学生年龄:new_name\n学生qq:new_name\n')
            else:
                print('查无此人')
    elif choose == 4:
        for student in students:
            print('删除学生')
            telete_name = input('请输入要删除的学生姓名:')
            if student.get('name') == telete_name:
                del student['telete_name,student.get(age),student.get(qq)']
                print('删除成功!')
            else:
                print('修改的用户不存在')
    else:
        print('退出系统')
        flag = False

