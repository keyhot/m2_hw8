import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    sql = '''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def add_products(conn):
    insert_product(conn, ("Banana", 150, 3))
    insert_product(conn, ("Apple", 100, 5))
    insert_product(conn, ("Watermelon", 80, 6))
    insert_product(conn, ("Melon", 130, 1))
    insert_product(conn, ("Strawberry", 120, 15))
    insert_product(conn, ("Blueberry", 160, 10))
    insert_product(conn, ("Cherry", 110, 11))
    insert_product(conn, ("Tomato", 70, 8))
    insert_product(conn, ("Dragon Fruit", 140, 4))
    insert_product(conn, ("Cucumber", 170, 3))
    insert_product(conn, ("Pear", 150, 1))
    insert_product(conn, ("Potato", 140, 0))
    insert_product(conn, ("Carrot", 80, 5))
    insert_product(conn, ("Pineapple", 130, 8))
    insert_product(conn, ("Avocado", 90, 4))

def update_quantity(conn, product):
    sql = '''
    UPDATE products SET quantity = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, product):
    sql = '''
    UPDATE products SET price = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, product_id):
    sql = '''
    DELETE FROM products where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''
    SELECT * from products 
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)


def select_products(conn, limit):
    sql = '''
    SELECT * from products where price < ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)


def search_item(conn, search):
    search = '%' + search + '%'
    sql = '''
        SELECT * from products where product_title LIKE ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (search,))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)


db_name = r'products_db'
create_students_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0.0
)'''
connection = create_connection(db_name)
if connection is not None:
    print("Successfully connected to DB " + db_name)
    # create_table(connection, create_students_table_sql)
    # add_products(connection)
    update_quantity(connection, (4, 1))
    update_price(connection, (135, 1))
    select_all_products(connection)
    select_products(connection, 100)
    search_item(connection, "berry")
    connection.close()
    print("DONE!")