import requests
from datetime import datetime
from db import get_connection


def get_price(url):
    """Extract price from FakeStore product JSON."""
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return float(data["price"])
    except:
        return None


def track():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, url FROM products")
    products = cur.fetchall()

    for pid, url in products:
        print(f"\nTracking product {pid}:")
        price = get_price(url)
        print("  Price =", price)

        if price:
            cur.execute(
                "INSERT INTO prices (product_id, price, date) VALUES (%s, %s, %s)",
                (pid, price, datetime.now())
            )
            print("  Saved.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    track()
