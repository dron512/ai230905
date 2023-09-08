import pymysql

host="localhost"
user="root"
password="1234"
database = "test"
port = 3306

def doInsert():
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     port=port)
        cursor = connection.cursor()
        sql = '''
                INSERT INTO member
                (NAME,age,gender)
                VALUES
                ('이길동',50,'여자');
            '''
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        connection.close()

def doSelect():
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     port=port)
        cursor = connection.cursor()
        sql = "select * from member"
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)
    except Exception as e:
        print(e)
    finally:
        connection.close()