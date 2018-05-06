import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'shopping'
USER = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'


class User:
    HOST = '127.0.0.1'
    PORT = 3306
    DB_NAME = 'shopping'
    USER = 'root'
    PASSWORD = 'root'
    CHARSET = 'utf8'
    __DEFAULT = 'file.txt'
    __CONF = []

    @classmethod
    def get_config(cls):
        conn = pymysql.connect(host=cls.HOST,
                               port=cls.PORT,
                               db=cls.DB_NAME,
                               user=cls.USER,
                               passwd=cls.PASSWORD,
                               charset=cls.CHARSET
                               )
        cursor = conn.cursor()
        return conn, cursor

    @classmethod
    def file_config(cls, file=None):
        if file is None:
            file = cls.__DEFAULT

        with open('file', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                cls.__CONF.append(line.strip('\n').split(':')[1])


class User_manage:

    def __init__(self, userid, username, password, balance):
        self.userid = userid
        self.username = username
        self.password = password
        self.balance = balance

    @classmethod
    def find_shop_all(cls, sql):
        """
        查询
        :param sql:
        :return:
        """
        test = User.get_config()
        test[1].execute(sql)
        return test[1].fetchall()

    @classmethod
    def login(cls, sql):
        """
        登陆
        :param sql:
        :return:
        """
        test = User.get_config()
        test[1].execute(sql)
        return test[1].fetchone()

    @classmethod
    def register(cls, *args):
        """
        注册
        :param args:
        :return:
        """
        test = User.get_config()
        test[1].execute(sql)
        if test[1].fetchone():
            print('用户已存在')
        else:
            # test[1].execute(sql_user)
            test[0].commit()
            print('注册成功')


class SHOP:
    def __init__(self, shid, shopname, price, userid, count):
        self.shid = shid
        self.shopname = shopname
        self.price = price
        self.userid = userid
        self.count = count

    @classmethod
    def add_shop(cls, sql):
        """
        添加
        :param sql:
        :return:
        """
        test = User.get_config()
        test[1].execute(sql)
        test[0].commit()
        return

    @classmethod
    def show_shop(cls, sql):
        """
        点击查看
        :param sql:
        :return:
        """
        User.get_config()
        User_manage.login(sql)




if __name__ == '__main__':
    # 查询
    # sql = "SELECT * FROM messages"
    # print(User.find_shop_all(sql))#查询

    # 登陆
    # user = input('用户名:')
    # passwd = input('密码:')
    # sql = "SELECT * FROM t_user WHERE username ='{}'".format(user)
    # result = User.login(sql)
    # if result:
    #     if result[2] == passwd:
    #         print('登陆成功')
    #     else:
    #         print('密码错误')
    # else:
    #     print('用户不存在')

    # 注册
    user = input('用户名:')
    passwd = input('密码:')
    sql = "SELECT * FROM t_user WHERE username ='{}'".format(user)
    sql_user = "INSERT INTO t_user(username, PASSWORD) VALUES('{}','{}')".format(user, passwd)
    User_manage.register(sql, sql_user)

    # 添加
    # sql = "INSERT INTO messages(shopname,shopprice,shoptitle,shopcount,SHOPID) VALUES('{}',{},'{}',{},{})"
    # .format('小龙虾',45,'特惨',5, 1)
    # SHOP.add_shop(sql)

    # 点击获取商品信息
    # user = input('用户名:')
    # passwd = input('密码:')
    # sql = "SELECT * FROM t_user WHERE username ='{}'".format(user)
    # result = SHOP.show_shop(sql)
    # if result:
    #     if result[2] == passwd:
    #         shid = input('选择查看的商品:')
    #         sql_show = "SELECT * FROM messages WHERE shId ={}".format(shid)
    #         User.get_config()[1].execute(sql_show)
    #         User.get_config()[1].fetchone()
    #
    #
    #
    #     else:
    #         print('密码错误')
    # else:
    #     print('用户不存在')
    name = User.get_config()
    print(name[0])
