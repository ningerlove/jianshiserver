import  pymysql

class TestingConfig:
    MYSQL_LOCAL_HOST = 'localhost'#'127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB_NAME = 'jianshi'
    TESTING = True



def _conn(cursorclass=pymysql.cursors.Cursor):
    return pymysql.connect(host=TestingConfig.MYSQL_LOCAL_HOST,
                           user=TestingConfig.MYSQL_USER,
                           password=TestingConfig.MYSQL_PASSWORD,
                           db=TestingConfig.MYSQL_DB_NAME,
                           charset='utf8mb4',
                           cursorclass=cursorclass)

conn = _conn(pymysql.cursors.DictCursor)