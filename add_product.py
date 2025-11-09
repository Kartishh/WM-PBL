from db import get_connection

def add_product(name, url, threshold):
    conn = get_connection()
    cur = conn.cursor()

    sql = "INSERT INTO products (name, url, threshold_price) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, url, threshold))

    conn.commit()
    conn.close()
    print("Product added.")

# Example
add_product(
    "iPhone",
    "https://fakestoreapi.com/products/1",
    100
)
