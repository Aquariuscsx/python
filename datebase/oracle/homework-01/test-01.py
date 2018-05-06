import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'scott'
USERNAME = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'


def query():
    with pymysql.connect(
            host=HOST,
            port=PORT,
            db=DB_NAME,
            user=USERNAME,
            passwd=PASSWORD,
            charset=CHARSET) as cursor:
        sql = "SELECT * FROM T_USERS WHERE username='xm'"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        # if result:
        #     userid=result[0]
        #     username=result[1]
        #     password=result[2]
        #     email=result[3]
        #     phone=result[4]
        #     is_delete = result[5]
        #     print('===========用户信息===========')
        #     print(userid, username, password, email, phone, is_delete)


def insert_one():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           db=DB_NAME,
                           user=USERNAME,
                           passwd=PASSWORD,
                           charset=CHARSET)
    cursor = conn.connect()
    sql = "INSERT INTO t_users(username,password,email,phone,is_delete) values('xiaoximg','12356','12345@','13385322199',1)"
    cursor.execute(sql)
    conn.commit()


def out_page(page, size):
    with pymysql.connect(
            host=HOST,
            port=PORT,
            db=DB_NAME,
            user=USERNAME,
            passwd=PASSWORD,
            charset=CHARSET) as cursor:
        sql = "SELECT * FROM T_USERS LIMIT{},{}".format((page - 1) * size, size)
        cursor.execute(sql)
        user = cursor.fetchall()
        print(len(user))


out_page(1, 5)
