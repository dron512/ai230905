import pymysql
# import ex04

host="localhost"
user="root"
password="1234"
database = "test"
port = 3306

# ex04.doA()
'''
def doA(a,b,c):
    print(f'a={a}',f'b={b}',f'c={c}')

doA(b=20,c=30,a=10)
'''

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











