import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'shopping'
USER = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'

class User:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance


class Shop:
    def __init__(self, shoptitle):
        self.shoptitle = shoptitle


class SHopDetail:
    def __init__(self, shopname, shopprice, shoptitle, shopcount):
        self.shopname = shopname
        self.shopprice = shopprice
        self.shoptitle = shoptitle
        self.shopcount = shopcount


# 通过用户名查询用户 再判断密码
def login():
    # 打开与数据库的链接
    with pymysql.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         charset=CHARSET,
                         db=DB_NAME) as cursor:  # 游标
        user = input('请输入用户名:')
        passwd = input('请输入密码:')
        sql = "SELECT * FROM t_user WHERE username = '{}'".format(user)
        cursor.execute(sql)  # 执行sql语句
        result = cursor.fetchone()  # 返回一条记录 以元组形式
        if result:
            if result[2] == passwd:
                print('登陆成功!')
            else:
                print('密码错误!!')

        else:
            print('此用户不存在')

    # 首先查询用户是否存在
    # 如果存在就提示 账号已存在
    # insert into


def register():
    # 创建事务conn
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    # 创建游标
    cursor = conn.cursor()
    user = input('请输入用户名:')
    passa = input('请输入密码:')
    sql = "SELECT * FROM t_user"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        if result[1] == user:
            print('输入的用户已存在')
        else:
            sql2 = "INSERT INTO t_user(username, password) VALUES('{}','{}')".format(user, passa)
            cursor.execute(sql2)
            conn.commit()
            print('注册成功')


def add_shop():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO messages(shopname,shopprice,shoptitle,shopcount,SHOPID) VALUES(%s,%s,%s,%s,%s)"
        li = []
        # 循环添加的次数
        for i in range(1):
            # 添加的商品信息
            # 最后的商品id 按种类输出
            li.append(('酸奶', 29, '帮助消化', 20, 3))
            li.append(('油条', 29, '帮助消化', 20, 3))
        conn.begin()  # 开启事务
        # 执行事务
        cursor.executemany(sql, li)
        conn.commit()
    except:
        conn.rollback()
        print('异常')
    finally:
        cursor.close()
        conn.close()


def show_shop():
    """
    # select * from shop
    # shop_id  作为外键
    :param self:
    :return:
    """
    with pymysql.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         charset=CHARSET,
                         db=DB_NAME) as cursor:
        # 通过商品id 查找 只能查找该id对应的商品信息
        shop_id = input('商品id:')
        sql = "SELECT * FROM messages WHERE SHID = {}".format(shop_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        # 显示详细的信息
        if result:
            name = result[1]
            price = result[2]
            title = result[3]
            count = result[4]
        print('商品名称: {}\n商品价格: {}\n商品信息: {}\n商品库存: {}'.format(name, price, title, count))


def show_shopping():
    with pymysql.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         charset=CHARSET,
                         db=DB_NAME) as cursor:
        shop_id = input('点击商品id')
        sql = "SELECT * FROM messages WHERE SHOPID = {}".format(shop_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)


def show_shop_car():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    sql = "SELECT * FROM t_user WHERE username = '{}'".format(user)
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchone()  # 返回一条记录 以元组形式
    if result:
        if result[2] == passwd:
            shop_id = input('输入选择商品编号:')
            sql1 = "SELECT * FROM messages WHERE shId = {}".format(shop_id)
            cursor.execute(sql1)
            result = cursor.fetchall()
            print(result)
        else:
            print('密码错误!!')

    else:
        print('此用户不存在')


def add_shop_car():
    """
     #     添加商品到购物车
    :param userid:
    :param shop_id:
    :param count:
    :return:
    """
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    sql = "SELECT * FROM t_user WHERE username = '{}'".format(user)
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchone()  # 返回一条用户记录 以元组形式
    if result:
        # 验证用户密码 正确就执行下一步
        if result[2] == passwd:
            # 通过user 得到userid
            sql_show = "SELECT USERID FROM t_user WHERE username ='{}'".format(user)
            cursor.execute(sql_show)
            result = cursor.fetchone()
            userid = result[0]
            # 选择要购买的商品加入购物车
            shid = input('输入要加入的商品编号:')
            # 通过商品的id 得到商品的名字和价格
            sql_shop_id = "SELECT shopname,shopprice FROM messages WHERE shId = {}".format(shid)
            cursor.execute(sql_shop_id)
            results = cursor.fetchone()
            #  返回的是商品名称和价格 的一个元组, 因为返回的数据是元组,根据下标去取
            shopname = results[0]
            price = results[1]
            # 得到加入购物车的数量
            count = int(input('输入要添加的数量:'))
            # 实现添加功能
            sql_add = "INSERT INTO shop_cart(SHOPNAME,PRICE,count,SHID,USERID) VALUES('{}',{},{},{},{})".format(
                shopname, price, count, shid, userid)
            cursor.execute(sql_add)
            conn.commit()
        else:
            print('密码错误!!')

    else:
        print('无用户,请先注册')



def total():
    """
      # 结算
    :param self:
    :return:
    """
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           passwd=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)
    cursor = conn.cursor()
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    sql = "SELECT * FROM t_user WHERE username = '{}'".format(user)
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchone()  # 返回一条记录 以元组形式
    if result:
        if result[2] == passwd:
            sql_userid = "SELECT userid FROM t_user WHERE username = '{}'".format(user)
            cursor.execute(sql_userid)
            result = cursor.fetchone()
            userid = result[0]
            #取去该用户的购物车商品的价格和数量
            sql_account = "SELECT price,count FROM shop_cart WHERE USERID = {}".format(userid)
            cursor.execute(sql_account)
            results = cursor.fetchall()
            last_total = 0#该用户所有商品的结算金额
            if results:
                for result in results:
                    price = result[0]
                    count = result[1]
                    total = price * count
                    last_total += total
                    sql_charge = "SELECT balance FROM t_user WHERE USERID = '{}'".format(user)
                    cursor.execute(sql_charge)
                    balance = cursor.fetchone()#建表余额记得设计成和金额同类型
                    if balance > last_total:
                        balance -= last_total
                        print('余额为:{}'.format(balance))
                    else:
                        print('余额不足')
                print(last_total)
        else:
            print('密码错误!!')
    else:
        print('没有商品信息')
