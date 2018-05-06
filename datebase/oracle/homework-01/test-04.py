import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'scott'
USERNAME = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'


def insert_one():
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           db=DB_NAME,
                           user=USERNAME,
                           passwd=PASSWORD,
                           charset=CHARSET)
    cursor = conn.connect()
    sql = "INSERT INTO t_users(username,password,email,phone) values('xiaoximg','12356','12345@','13385322199')"
    cursor.execute(sql)
    conn.commit()


insert_one()