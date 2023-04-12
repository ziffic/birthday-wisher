import smtplib
import connect
<<<<<<< HEAD
=======
import pandas
>>>>>>> ac608368b3150b8a258a8223850825c69deebc4f
import datetime as dt
import random

my_email = connect.ACCOUNT_EMAIL
password = connect.ACCOUNT_PASSWORD
<<<<<<< HEAD

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
=======
now = dt.date.today()
NUM_EMAIL_TEMPLATES = 3
PLACEHOLDER = "[NAME]"

try:
    birthdays = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Error opening file")
    birthday_dic = []
else:
    birthday_dic = birthdays.to_dict(orient="records")

for n in birthday_dic:
    birthday_month = n["month"]
    birthday_day = n["day"]

    if birthday_month == now.month and birthday_day == now.day:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        try:
            with open(file_path) as letter_file:
                letter_contents = letter_file.read()
                new_letter = letter_contents.replace(PLACEHOLDER, n["name"].strip())

                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(my_email, password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=n["email"],
                                        msg=f"Subject: Happy Birthday\n\n{new_letter}"
                                        )
                    connection.close()
        except FileNotFoundError:
            print("No file found.")
>>>>>>> ac608368b3150b8a258a8223850825c69deebc4f
