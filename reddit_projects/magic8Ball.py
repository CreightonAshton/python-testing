from random import randrange
import time

responses = ["Ask again later", "Outlook Good", "Signs point to yes", "Signs point to no", "'Tis a mystery", "Yes", "No"]

def question():
	go = True
	while go == True:
		input("What is your question? ")
		print ("Thinking...")
		time.sleep(3)
		print (responses[randrange(len(responses))])
		ans = ""
		while ans != "y" and ans != "n":
			ans = str(input("Do you have another question? (y/n) ")).lower()
			if ans == "n":
				go = False
	print ("Good Bye")
			
			
question()