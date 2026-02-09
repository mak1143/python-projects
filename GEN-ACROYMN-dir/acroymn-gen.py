#Get user input
userInput = input("Enter a phrase: ")


#spiliting the user input into individual words using split () method

phrase = userInput.split() 


#initiailizing an empty string to append the acronym

append = ""

#loop to append acronym

for word in phrase:
	append += word[0].lower()

print(f"Acronym of {userInput} is [{append}] " )
