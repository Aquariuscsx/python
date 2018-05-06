# import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'shopping'
USER = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'


def login():
    with pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            passwd=PASSWORD,
            charset=CHARSET,
            db=DB_NAME) as cursor:
        users = input('请输入用户名:')
        pwd = input('请输入密码:')
        sql = "SELECT * FROM t_user WHERE username='{}'".format(users)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            if result[2] == pwd:
                print('登陆成功')
            else:
                print('密码错误')
        else:
            print('链接失败')


def add_shop():
    """
    单挑添加
    :return:
    """
    try:
        conn = pymysql.connect(host=HOST,
                               port=PORT,
                               user=USER,
                               passwd=PASSWORD,
                               charset=CHARSET,
                               db=DB_NAME)
        cursor = conn.cursor()

        sql = "INSERT INTO message(shopname,shopprice,shoptitle,shopcount) VALUES('地瓜干', '10','不一样得味道', 10)"
        cursor.execute(sql)
        conn.commit()

    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def show():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    sql = "SELECT m.shopname,m.shopprice,m.shId,t.USERID from messages m,t_user t,shop_cart s where m.SHID = s.SHID and t.USERID = s.USERID"
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        shopname = result[0]
        shopprice = result[1]
        shoptitle = result[2]
        shopcount = result[3]
        # sql_add = "INSERT INTO shop_cart(SHOPNAME,price,shid,userid) VALUES(%s,%s,%s,%s)".format(shopname, shopprice,
        #                                                                                          shoptitle, shopcount)
        # cursor.execute(sql_add)
        # result = cursor.fetchone()
        # conn.commit()

        print(results)


show()


def show_shop():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    news = input('查询得商品名称')
    sql = "SELECT * FROM message m WHERE m.shopname = '{}'".format(news)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        for name in result:
            if name == news:
                print(result)
                break

            else:
                print('输出错误')

    else:
        print('不存在')


def shop_cart():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    username = input('yh')
    passwd = input('mm')
    sql = "SELECT * FROM t_user uasename = '{}'".format(username)
    cursor.execute(sql)
    result = cursor.fetchall()
    li = []
    if result:
        if result[2] == passwd:
            print('登陆成功')
            print('请选择你要购买的商品')
            sql = "SELECT * FROM message"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                shopname = result[0]
                shopprice = result[1]
                shoptitle = result[2]
                shopcount = result[3]
                print('商品名称:{},商品价格:{},商品描述:{},商品数量:{}'.format(shopname, shopprice, shoptitle, shopcount))
                shopcart = {'名称': shopname, '价格': shopprice}
                li.append(shopcart)
                print(li)
                pass

        else:
            print('密码错误')
    else:
        print('链接失败')

# if __name__ == '__main__':
# login()  # denglu  yh:xm, mima:123456
# add_shop()  # tianjai
# show()  # 显示
# show_shop()  # 查询 yh:xm
# shop_cart()  # yh:xm mm:123456
