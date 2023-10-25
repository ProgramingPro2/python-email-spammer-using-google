#Enter email and password upon first use
#also enter the file path of the message.txt file
#finaly go to https://myaccount.google.com/lesssecureapps and turn on less secure apps
#you are set to go ;)

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set up the SMTP server
smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_server.starttls()

# Login to your Google account, enter email and password
smtp_server.login("EMAIL", "PASSWORD")

email = str(input("Enter recipitent email address: "))
subject = str(input("Enter subject: "))
fromEmail = str(input("Enter your email address: "))

#enter the file path of the message.txt file or it will not work, also make sure to put your message in the file
messageFilePath = "C:\\Users\\USER\\OneDrive\\Desktop\\message.txt"

for i in range(0, int(input("Enter number of emails to send: "))):
	# create a message
	msg = MIMEMultipart()

	# setup the parameters of the message
	msg['From'] = fromEmail
	msg['To'] = email
	msg['Subject'] = subject + " " + str(i + 1)

	# add in the message body from message.txt, make sure to enter the file path
	msg.attach(MIMEText(open(messageFilePath, "r").read()))

	# send the message via the server.
	smtp_server.send_message(msg)

	print("Email number " + str(i + 1) + " sent")

	time.sleep(3)

print("Email sent successfully")

# close the SMTP server
smtp_server.quit()
