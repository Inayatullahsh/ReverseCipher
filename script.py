# Reverse Cipher


# cipher = '.daed era meht fo owt fi ,terces a peek nac eerhT'
# decipher = 'Three can keep a secret, if two of them are dead.'

while True:
	cipher = input("Enter a cipher or 'q' => ")
	decipher = ""
	pattern = "--" * 20
	# terminate the program if the input is one of the following keyword
	quit_keywords = ["Quit", "quit", "Q", "q"]




	if cipher in quit_keywords:
		print(pattern)
		print(f" {quit_keywords} are reserved keyword for terminating the program.")
		print("Program Terminated...")
		print(pattern)
		break

	length = len(cipher) - 1

	while length >= 0:
	    decipher = decipher + cipher[length]
	    length = length - 1

	print(pattern)
	print("Result ==> ", decipher)
	print(pattern)
