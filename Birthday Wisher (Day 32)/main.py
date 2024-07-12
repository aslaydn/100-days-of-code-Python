# SMTP: Simple Mail Transfer Protocol
import smtplib 

my_email = "aaydinnasli@gmail.com"
password = "Aslaydn123."

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #transport layer security
connection.login(user=my_email)