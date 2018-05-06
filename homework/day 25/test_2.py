
flag = True
phone_list = [{'brand': 'huewei', 'model': 'matep10', 'price': '4999.00', 'count': '10', 'version':'8G'}, {'brand': 'apple', 'model': 'phone', 'price': '4999.00', 'count': '10', 'version': '16G'}, {'brand': 'SONY', 'model': 'Z3L55', 'price': '6999.00', 'count': '10', 'version': '128G'}]
while flag:
    print('手机信息管理系统')
    def add_phone():
        """
        添加手机信息
        phone_lists 用字典存放添加的数据类型,在添加到手机信息里
        :return:
        """
        add_brand = input('请输入添加的手机品牌:\n')
        add_model = input('请输入添加的手机型号:\n')
        add_price = float(input('请输入添加的手机价格:\n'))
        add_count = int(input('请输入添加的手机数量:\n'))
        add_version = input('请输入添加的手机版本:\n')
        phone_lists = {'brand': add_brand, 'model': add_model, 'price': add_price, 'count': add_count, 'version':add_version }
        phone_list.append(phone_lists)
        print('添加成功')


    def query_phone():
        """
        查询手机信息
        :return:
        """
        query_brand = input('请输入查询手机的品牌:\n')
        # query_model = input('请输入查询手机的型号:\n')
        # query_price = input('请输入查询手机的价格:\n')
        for phone_lists in phone_list:
            if query_brand == phone_lists.get('brand'):
                print('手机品牌{},手机型号{},手机价格{},手机数量{},手机版本{}'.format(query_brand, phone_lists.get('model'), phone_lists.get('price'), phone_lists.get('count'), phone_lists.get('version'),))
                break
            else:
                print('查无吃鸡')

    def query_all_phone():
        """
        查询所有信息
        :return:
        """
        for phone_lists in phone_list:
            if phone_lists:
                print(phone_lists)

    def up_phone():
        """
        编号就是索引长度减1
        判断手机编号的值 是否等于 索引的值
        等于就可以修改
        :return:
        """
        phone_id = int(input('请输入要修改的手机编号:\n'))
        new_price = float(input('请输入要修改的手机价格:\n'))
        if len(phone_list) > 0 and phone_id <= len(phone_list):
            for phone_lists in phone_list:
                if phone_list[phone_id - 1] == phone_lists:
                    phone_lists.update(price=new_price)
                    print('修改成功',)
                    print(phone_lists)

        else:
            print('输入的手机编号不存在,请重新输入')


    def delete():
        phone_id = int(input('请输入要删除的手机编号:\n'))
        if len(phone_list) > 0 and phone_id <= len(phone_list):
            for phone_lists in phone_list:
                if phone_list[phone_id - 1] == phone_lists:
                    phone_list.remove(phone_lists)
                    print('删除成功', )
                    print(phone_list)

        else:
            print('删除失败!!!删除的手机编号不存在,请重新输入')

    def blurry():
        brand = input('请输入要查询的数据')
        for phone_lists in phone_list:
            # for phone_lists['brand']
            # for value in phone_lists.keys():
            #     for value in values:
            if phone_lists['brand'].find(brand) != -1:
                print(phone_lists)





    choose = input('1.手机录入\n2.根据手机品牌查询手机信息\n3.查询全部手机信息\n4.根据手机编号修改手机价格\n5.根据手机编号删除手机记录\n6.退出\n')
    if choose == '1':
        add_phone()
        print(phone_list)
    elif choose == '2':
        query_phone()
    elif choose == '3':
        blurry()
    elif choose == '4':
        up_phone()
    elif choose == '5':
        delete()
    elif choose == '6':
        flag = False
        print('退出!')

    else:
        # if isinstance(choose, str):
        print('输入错误,请重新输入')
        break


# try:
#     choose = int(input())
# except:
#     print('输入错误')
















