from colorama import Back, init, Fore, Style
from prettytable import PrettyTable
table = PrettyTable()

Print_madlips = Fore.CYAN + "Printable Mad  lips".center(34,'-')
print(Print_madlips)
table.add_column("nouns" ,
["Adelaide","ring","milk","toilet","accra","garlic","hippo"])
table.add_column("adjective" ,
["flutty","young","tall","sharp","dirty","dizzy","wet"])
table.add_column("verbs" ,
["leap","skip","laugh","march","scamper","sing","crawl"])


print(table)



#dictionary 
categories = ["noun","adjective","verb"]
words = {}


for category in categories:
    words[category] = input(f"Enter a(an) {category}: ")

story_templates = f"Every day, they would {words['verb']} to the {words['noun']} and {words['verb']} with their {words['adjective']}, {words['noun']}🤓"



print(Fore.RED + story_templates.center(10))


