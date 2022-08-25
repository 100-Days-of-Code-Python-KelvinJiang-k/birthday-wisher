# -------------------------- Extra Hard Starting Project -------------------------- #
import pandas
import smtplib
import random
import datetime as dt
import os

EMAIL = "N/A"
PASSWORD = "N/A"
EMAIL_SMTP = "smtp.gmail.com"

birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="records")

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

for birthday in birthday_dict:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        name = birthday["name"]

        letter_directory = os.getcwd() + "/letter_templates"
        letter_file = random.choice(os.listdir(letter_directory))

        with open("letter_templates/" + letter_file, "r") as letter:
            letter_template = letter.read()
        completed_letter = letter_template.replace("[NAME]", name)

        with smtplib.SMTP(EMAIL_SMTP, 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=birthday["email"],
                                msg=f"Subject: Happy Birthday!\n\n{completed_letter}")


