import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'vidian670',
    'db': 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )

        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            cur.close()
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        conn.close()


if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(f'result={result}')
