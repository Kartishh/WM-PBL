from db import get_connection

def add_product(name, url, threshold):
    conn = get_connection()
    cur = conn.cursor()

    sql = "INSERT INTO products (name, url, threshold_price) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, url, threshold))

    conn.commit()
    conn.close()

def bulk_add():
    conn = get_connection()
    cur = conn.cursor()

    pid = 1
    for i in range(1, 101):   # 1–100 products
        url = f"https://fakestoreapi.com/products/{(i % 20) + 1}"
        name = f"Product {i}"
        threshold = 200   # you can vary this

        cur.execute(
            "INSERT INTO products (name, url, threshold_price) VALUES (%s, %s, %s)",
            (name, url, threshold),
        )

    conn.commit()
    conn.close()
    print("100 products inserted.")

if __name__ == "__main__":
    bulk_add()
