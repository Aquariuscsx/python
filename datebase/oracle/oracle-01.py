import pymysql


HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'scott'
USER = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'
try:
    conn = pymysql.connect(host=HOST,
                           port=PORT,
                           user=USER,
                           password=PASSWORD,
                           charset=CHARSET,
                           db=DB_NAME)



    cursor = conn.cursor()
    sql = 'SELECT * FROM emp '
    cursor.execute(sql)
    results = cursor.fetchall()
    print(type(results))
    for rs in results:
        uid = rs[0]
        uname = rs[1]
        email = rs[2]
        phone = rs[3]
        print(uid)
except:
    print('链接失败')
finally:
    if cursor:
        cursor.close()
    elif conn:
        conn.close()
