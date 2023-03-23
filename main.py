import smtplib
import connect
import pandas
import datetime as dt
import random

my_email = connect.ACCOUNT_EMAIL
password = connect.ACCOUNT_PASSWORD
now = dt.date.today()
NUM_EMAIL_TEMPLATES = 3
PLACEHOLDER = "[NAME]"

# TODO: 1. Open the birthdays csv
try:
    birthdays = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error opening file")
    birthday_list = []
else:
    birthday_list = birthdays.to_dict(orient="records")

for n in birthday_list:
    birthday_month = n["month"]
    birthday_day = n["day"]

    if birthday_month == now.month and birthday_day == now.day:
        print(f"{n['name']} - Match")
        letter_template = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        try:
            with open(letter_template) as letter_file:
                letter_contents = letter_file.read()
                stripped_name = n["name"].strip()
                new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(my_email, password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs="dave@dryweb.com",
                                        msg=f"Subject: Happy Birthday\n\n{new_letter}"
                                        )
                    connection.close()
        except FileNotFoundError:
            print("No file found.")
