import pymysql

HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'scott'
USER = 'root'
PASSWORD = 'root'
CHARSET = 'utf8'


class DbUtils:
    __DEFAULT_FILE = 'init'
    __conf = []

    def get_conn(self):
        """
        获取connection 对象
        :return:
        """
        conn = pymysql.connect()
        return conn

    @classmethod
    def init_config(cls, path=None):
        if path is None:
            path = cls.__DEFAULT_FILE

        with open(path, 'r', encoding='utf-8') as f:
            conf = []
            for line in f.readlines():
                conf.append(line.strip('\n').split(':'))


if __name__ == '__main__':
    DbUtils.init_config()
