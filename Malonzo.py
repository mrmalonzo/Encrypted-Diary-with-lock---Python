import string
import collections
Diary={}
user_password="useruser"
counter=3
login=0

def caesar(rotate_string, number_to_rotate_by):

	upper=collections.deque(string.ascii_uppercase)
	lower=collections.deque(string.ascii_lowercase)
	characters=collections.deque("0123456789.,?!")

	upper.rotate(number_to_rotate_by)
	lower.rotate(number_to_rotate_by)
	characters.rotate(number_to_rotate_by)

	upper=''.join(list(upper))
	lower=''.join(list(lower))
	characters=''.join(list(characters))

	return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower)).translate(str.maketrans("0123456789.,?!", characters))

with open("secret.txt") as fh:
	for data in fh:
		user_password=caesar(data,4)
fh.close()

print("---------------------------------------")
print("\nWELCOME TO YOUR OWN PERSONAL DIARY\n")
print("---------------------------------------")
counter=3
login=0

for i in range(0,99):
	password=input("Please Enter your Password: ")
	if counter!=0:
		if password!=user_password:
			print("Wrong Password")
			print("The default password is: useruser")
			counter-=1
			print("Trials left: "+ str(counter))
			print("------------------------")
		else:
			print("------------------------")
			print("\nLogin Successful\n")
			login=1
			break
	else:
		break

if login==0:
	exit()

with open("Data.txt") as fh:
	for data in fh:
		data=data[:-1]

		save=data.split("\t")
		Entry_Number=caesar(save[0],4)
		Date=caesar(save[1],4)
		Time=caesar(save[2],4)
		Story=caesar(save[3],4)
		password=caesar(save[4],4)
		Diary[Entry_Number]=[Date,Time,Story,password]
fh.close()


def menu():
	print("------------------------")
	print("Please CHOOSE from this OPTIONS what YOU want to do!")
	print("[1] Add Entry")
	print("[2] View Specific Entry")
	print("[3] Edit Specific Entry")
	print("[4] Delete Specific Entry")
	print("[5] Delete Diary")
	print("[6] Change Main Password")
	print("[0] Exit Diary")
	choice=int(input("Please choose from the options above: "))
	return choice
while True:
	select= menu()

	if select==0:
		break

	elif select==1:
		Entry_Number=input("Entry Number?: ")
		if Entry_Number in Diary:
			print("------------------------")
			print("\nEntry Number is already used\n")
		else:
			Entry_Info=[]
			Date=input("Date: ")
			Entry_Info.append(Date)
			Time=input("Time: ")
			Entry_Info.append(Time)
			Story=input("Your story: ")
			Entry_Info.append(Story)
			while True:
				password=input("Password of the entry: ")
				password2=input("Confirm Password: ")
				if password==password2:
					Entry_Info.append(password)
					break
				else:
					print("------------------------")
					print("\nPassword does not match\n")
					print("------------------------")

			print("------------------------")
			print("\nEntry Added!\n")
			Diary[Entry_Number]=Entry_Info

	elif select==2:
		Entry_Numberinput=input("Entry Number you want to view?: ")
		Entry_Number=Entry_Numberinput
		if Entry_Numberinput not in Diary:
			print("------------------------")
			print("\nEntry Number does not exist!\n")

		else:
			password=input("Please input the password of the entry: ")
			realpassword=Diary[Entry_Number][3]
			counter=0
			if password==realpassword:
				while True:
					print("------------------------")
					print("My Diary; Entry Number: " + str(Entry_Number))
					Date=(Diary[Entry_Number][0])
					print("Date: " + Date)
					Time=(Diary[Entry_Number][1])
					print("Time: " + Time)
					Story=(Diary[Entry_Number][2])
					print("Story: " + Story)
					print("------------------------")
					cont=input("Press enter to continue!")
					counter+=1
					if cont=="":
						break
					else:
						print("------------------------")
						print("\nYou do not follow intructions!\n")
						if counter==3:
							print("------------------------")
							print("\nYou're a stubborn one!\n")
							break

			else:
				print("------------------------")
				print("\nPassword is incorrect\n")

	elif select==3:
		Entry_Numberinput=input("Entry Number that you want to edit: ")
		if Entry_Numberinput not in Diary:
			print("------------------------")
			print("\nEntry Record does not exist!\n")
		else:
			password=input("Please input the password of the entry: ")
			Entry_Number=Entry_Numberinput
			realpassword=Diary[Entry_Number][3]
			if password==realpassword:
				print("------------------------")
				print("Welcome to the edit section!")
				print("[1] Date")
				print("[2] Time")
				print("[3] Story")
				print("[4] Password")
				details=int(input("What do you want to edit? "))

				if details==1:
					Date=input("New Date that you want?")
					Diary[Entry_Number][0]=Date
					print("------------------------")
					print("\nDate Changed Successfully!\n")
				elif details==2:
					Time=input("New Time that you want?")
					Diary[Entry_Number][1]=Time
					print("------------------------")
					print("\nTime Changed Successfully!\n")
				elif details==3:
					Story=input("New Story that you want?")
					Diary[Entry_Number][2]=Story
					print("------------------------")
					print("\nStory Changed Successfully!\n")
				elif details==4:
					while True:
						password2=input("New Password: ")
						password3=input("Confirm Password: ")
						if password2==password3:
							Diary[Entry_Number][3]=password2
							print("------------------------")
							print("\nPassword Changed Successfully!\n")
							break
						else:
							print("------------------------")
							print("\nPassword does not match\n")
							print("------------------------")
				else:
					print("------------------------")
					print("\nInvalid Selection!\n")
					
			else:
				print("------------------------")
				print("\nPassword is incorrect!\n")

	elif select==4:
		delete_entry=input("Entry Number that you want to delete?")
		Entry_Number=delete_entry
		if delete_entry not in Diary:
			print("------------------------")
			print("\nEntry Number does not exist!\n")
		else:
			password=input("Please input the password of the entry: ")
			realpassword=Diary[Entry_Number][3]
			if password==realpassword:
				del Diary[Entry_Number]
				print("------------------------")
				print("\nEntry Deleted!\n")
			else:
				print("------------------------")
				print("\nPassword is Incorrect!\n")
				

	elif select==5:
		if Diary=={}:
			print("------------------------")
			print("\nDIARY ALREADY EMPTY!\n")
		else:
			Diary.clear()
			print("------------------------")
			print("\nAll Entries Have Been Deleted!\n")

	elif select==6:
		print("------------------------")
		askpassword=input("Please enter the old password: ")
		if askpassword==user_password:
			while True:
				print("------------------------")
				user_password=input("Please enter the new password: ")
				confirm_password=input("Confirm New Password: ")
				if user_password!=confirm_password:
					print("password does not match")
				else:
					with open("secret.txt", "w") as fh:
						up=caesar(user_password,-4)
						fh.write(up)
					fh.close()
					print("------------------------")
					print("\nPassword Successfully changed!\n")
					break
		else:
			print("------------------------")
			print("\nPassword is incorrect\n")



	with open("Data.txt", "w") as fh:
		for i in Diary:
			Entry_Number=i
			E=caesar(str(Entry_Number),-4)
			D=caesar((Diary[Entry_Number][0]),-4)
			T=caesar((Diary[Entry_Number][1]),-4)
			S=caesar((Diary[Entry_Number][2]),-4)
			p=caesar((Diary[Entry_Number][3]),-4)
			fh.write(E+'\t'+D+'\t'+T+'\t'+S+'\t'+p+'\t')
			fh.write("\n")
	fh.close()