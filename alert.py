from db import get_connection
import smtplib
from email.mime.text import MIMEText

# ---- CHANGE THESE ----
EMAIL = "orekithehyouka25@gmail.com"
PASSWORD = "fdxaeidhgletakyq"   # App password for Gmail
TO = "hachimanthegoat25@gmail.com"
# ----------------------

def send_alert(product, price):
    msg = MIMEText(f"Price dropped!\n\n{product} is now only ${price}.")
    msg["Subject"] = "⚠ Price Alert!"
    msg["From"] = EMAIL
    msg["To"] = TO

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)
        print("✅ Alert sent!")
    except Exception as e:
        print("❌ Error sending email:", e)


def check_alerts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT products.name,
               products.threshold_price,
               prices.price
        FROM prices
        JOIN products ON products.id = prices.product_id
        ORDER BY prices.date DESC
    """)

    rows = cur.fetchall()
    conn.close()

    for name, threshold, price in rows:
        if price <= threshold:
            print(f"⚠ Threshold reached for {name}: {price}")
            send_alert(name, price)


if __name__ == "__main__":
    check_alerts()
