#Random allotment and secretly mailing the allotment details to each participant.

import numpy as np
import pandas as pd
import smtplib

participants = {
'Vikas'   : 'Email ID of Vikas',  #Example: 'abc@gmail.com'
'Dev'     : 'Email ID of Dev',  #Example: 'bbc@gmail.com'
'Mahek'   : 'Emai ID of Mahek',   #Example: 'cbc@gmail.com'
'Akash'   : 'Email ID of Akash', #Example: 'dbc@gmail.com'
'Vishal'  : 'Email ID of Vishal' #Example: 'lbc@gmail.com'
}


#set groups of people which must not gift each other, 0 means no constrains, every other number is a group  

constrains = {
'Vikas'   : 0,
'Dev'     : 0,
'Mahek'   : 1,
'Akash'   : 1,
'Vishal'  : 0
}


def setRandom():
	santa = list(np.random.choice(list(participants.keys()), len(list(participants.keys())), replace = False))
	receiver = []
	for i in range(-1, len(santa)-1):
		receiver.append(santa[i])
	return santa, receiver

def checkConstrains():
	for i in range(len(santa)):
		print(i, santa[i], constrains[santa[i]], receiver[i], constrains[receiver[i]], sep = ' | ', end = '\n')
		if santa[i]==receiver[i]:
			return False
		if constrains[santa[i]] and constrains[santa[i]] == constrains[receiver[i]]: #se il vincolo è diverso da 0 oppure se sono uguali
			return False
	return True





santa, receiver = setRandom()
while not checkConstrains():
	santa, receiver = setRandom()
print(santa, receiver)

		
#Keep less secured apps option turned on from your gmail account to avoid error while sending out the mail.

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
email = input('Enter your email: ')
password = input('Enter your password: ')
smtpObj.login(email, password)

for j in range(len(participants)):
	smtpObj.sendmail(email, participants[santa[j]], \
	'Subject: Secret Santa 2022 \
	\nHo Ho Ho %s! \
	\n\nChristmas is almost here, \
	\n\nThis year you are gifting to....... %s!' % (santa[j], receiver[j]))

smtpObj.quit()

#df = pd.DataFrame({'santa':santa, 'receiver':receiver})
#df.to_csv('Kris Kingle list.csv')





