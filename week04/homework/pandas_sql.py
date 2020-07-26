import pandas as pd
import os

current_path = os.path.abspath(os.path.dirname(__file__))


if __name__ == "__main__":
    # SELECT * FROM data;
    data = pd.read_csv(current_path+'/students.csv')
    teacher_data = pd.read_csv(current_path+'/teachers.csv')
    print(data)

    # SELECT * FROM data LIMIT 10;
    print(data.head(10))

    # 3. SELECT id FROM data;  //id 是 data 表的特定一列
    print(data['id'])

    # 4. SELECT COUNT(id) FROM data;
    print(data['id'].sum())

    # 5. SELECT * FROM data WHERE id<1000 AND age>30;
    print(data[(data['id'] < 1000) & (data['age'] > 30)])

    # 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    res = pd.concat([data, teacher_data])
    res.fillna('无')

    # print(res)
    # 9. DELETE FROM table1 WHERE id=10;
    res = data.drop(data[data['id'] == 10].index)
    print(res)

    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    res = data.drop('id', axis=1)
    print(res)
