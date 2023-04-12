import smtplib
import connect
import datetime as dt
import random

my_email = connect.ACCOUNT_EMAIL
password = connect.ACCOUNT_PASSWORD

now = dt.datetime.now()
weekday = now.weekday()

# Check if today matches the day to send message
if weekday == 3:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dave@dryweb.com",
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )

        connection.close()
