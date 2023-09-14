import pymysql

host="localhost"
user="root"
password="1234"
database = "test"
port = 3306

def doInsert(mid='test',mpass='pass',name='김길동',age=20,gender='남'):
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     port=port)
        cursor = connection.cursor()
        sql = f'''
                INSERT INTO member
                (id,password,NAME,age,gender)
                VALUES
                ('{mid}','{mpass}','{name}',{age},'{gender}');
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