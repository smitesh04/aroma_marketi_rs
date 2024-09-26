import pymysql

class DbConfig():
    con = pymysql.Connect(host='localhost', user='root', password='actowiz', database='aroma_marketi_rs')
    cur = con.cursor(pymysql.cursors.DictCursor)
    data_table = 'data'
    data_with_duplicates_table = 'data_with_duplicates'

    qr = f'''
        CREATE TABLE IF NOT EXISTS {data_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) DEFAULT NULL,
            url VARCHAR(255) DEFAULT NULL,
            sku VARCHAR(255) DEFAULT NULL,
            brand VARCHAR(255) DEFAULT NULL,
            product_type VARCHAR(255) DEFAULT NULL,
            currency VARCHAR(255) DEFAULT NULL,
            price VARCHAR(255) DEFAULT NULL,
            mrp VARCHAR(255) DEFAULT NULL,
            country VARCHAR(255) DEFAULT NULL,
            quantity VARCHAR(255) DEFAULT NULL,
            pagesave VARCHAR(255) DEFAULT NULL,
            image VARCHAR(255) DEFAULT NULL,
            UNIQUE KEY `image` (`image`))
    '''

    cur.execute(qr)
    con.commit()

    qr = f'''
            CREATE TABLE IF NOT EXISTS {data_with_duplicates_table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) DEFAULT NULL,
                url VARCHAR(255) DEFAULT NULL,
                sku VARCHAR(255) DEFAULT NULL,
                brand VARCHAR(255) DEFAULT NULL,
                product_type VARCHAR(255) DEFAULT NULL,
                currency VARCHAR(255) DEFAULT NULL,
                price VARCHAR(255) DEFAULT NULL,
                mrp VARCHAR(255) DEFAULT NULL,
                country VARCHAR(255) DEFAULT NULL,
                quantity VARCHAR(255) DEFAULT NULL,
                pagesave VARCHAR(255) DEFAULT NULL,
                image VARCHAR(255) DEFAULT NULL)
        '''

    cur.execute(qr)
    con.commit()