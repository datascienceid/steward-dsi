import pymysql


def conn(config):
    host_db = config.get('HOST')
    user_db = config.get('USER')
    pass_db = config.get('PASS')
    name_db = config.get('DBNAME')

    connection = pymysql.connect(host=host_db,
                                 user=user_db,
                                 password=pass_db,
                                 db=name_db,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
