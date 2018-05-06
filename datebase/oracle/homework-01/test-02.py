import cx_Oracle

HOST = '127.0.0.1'
PORT = 1521
DB_NAME = 'orcl'
USERNAME = 'scott'
PASSWORD = '123456'
CHARSET = 'utf8'


# def mul():
#     with pymysql.connect(
#             host=HOST,
#             port=PORT,
#             db=DB_NAME,
#             user=USERNAME,
#             passwd=PASSWORD,
#             charset=CHARSET) as cursor:
#         sql = "SELECT * FROM T_USERS"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         if result:
#             for re in result:
#                 first = result[1]
#                 last = re[2]
#
#
#             print(first)
#             print(last)


def out_page(page, size):
    with cx_Oracle.connect(
            host=HOST,
            port=PORT,
            db=DB_NAME,
            user=USERNAME,
            passwd=PASSWORD,
            charset=CHARSET) as cursor:
        sql = "SELECT * FROM T_USER LIMIT'{}','{}'".format((page - 1) * size, size)
        cursor.execute(sql)
        user = cursor.fetchall()
        print(len(user))





if __name__ == '__main__':
    out_page(1, 5)
