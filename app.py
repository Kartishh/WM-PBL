from flask import Flask, render_template
from db import get_connection

app = Flask(__name__)


@app.route("/")
def index():
    conn = get_connection()
    cur = conn.cursor()

    # ✅ Fetch 4 values: (id, name, price, date)
    cur.execute("""
        SELECT products.id, products.name, prices.price, prices.date
        FROM prices
        JOIN products ON prices.product_id = products.id
        ORDER BY prices.date DESC
    """)

    data = cur.fetchall()
    conn.close()

    return render_template("index.html", data=data)


@app.route("/chart/<int:pid>")
def chart(pid):
    conn = get_connection()
    cur = conn.cursor()

    # ✅ product name
    cur.execute("SELECT name FROM products WHERE id = %s", (pid,))
    row = cur.fetchone()
    if row:
        name = row[0]
    else:
        name = "Unknown Product"

    # ✅ price history
    cur.execute("""
        SELECT price, date
        FROM prices
        WHERE product_id = %s
        ORDER BY date
    """, (pid,))

    rows = cur.fetchall()
    conn.close()

    prices = [float(r[0]) for r in rows]
    dates = [r[1].strftime("%Y-%m-%d %H:%M") for r in rows]

    return render_template("chart.html", name=name, prices=prices, dates=dates)


if __name__ == "__main__":
    app.run(debug=True)
