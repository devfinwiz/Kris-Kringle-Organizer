import numpy as np
import pandas as pd
import smtplib

participants = {
'Vikas'   : 'Email ID of Vikas',  #Example: 'abc@gmail.com'
'Dev'     : 'Email ID of Dev', #Example: 'bbc@gmail.com'
'Mahek'   : 'Emai ID of Mahek', #Example: 'cbc@gmail.com'
'Akash'  : 'Email ID of Akash', #Example: 'dbc@gmail.com'
'Vishal'  : 'Email ID of Vishal' #Example: 'lbc@gmail.com'
}

santa = list(np.random.choice(list(participants.keys()), len(list(participants.keys())), replace = False))
receiver = []
for i in range(-1, len(santa)-1):
	receiver.append(santa[i])
			
#Keep less secured apps option turned on from your gmail account to avoid error while sending out the mail.

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
email = input('Enter your email: ')
password = input('Enter your password: ')
smtpObj.login(email, password)

for j in range(len(participants)):
	smtpObj.sendmail(email, participants[santa[j]], \
	'Subject: Kris Kingle 2022 \
	\nHo Ho Ho %s! \
	\n\nChristmas is almost here, \
	\n\nThis Kris Kingle you are gifting to....... %s!' % (santa[j], receiver[j]))

smtpObj.quit()

df = pd.DataFrame({'santa':santa, 'receiver':receiver})
df.to_csv('Kris Kingle list.csv')





