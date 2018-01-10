import datetime

birthday = "1988-06-29"
date_format = "%Y-%m-%d"

parsed_date = datetime.datetime.strptime(birthday, date_format)

print parsed_date.strftime("%A %-m/%d/%Y")