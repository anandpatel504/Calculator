from calculator import*
while True:
	def calculator(n1,n2,operation):
		if operation=="add":
			print add(n1,n2,operation)
		elif operation=="sub":
			print sub(n1,n2,operation)
		elif operation=="mul":
			print mul(n1,n2,operation)
		elif operation=="div":
			print div(n1,n2,operation)
		else:
			print "Invalid input"
	calculator(input("enter the first num"),input("enter the second num"),raw_input("enter the operation:-"))
	user=raw_input("Do you want to do calculator again?y/n")
	if user=="N" or user=="n":
		break