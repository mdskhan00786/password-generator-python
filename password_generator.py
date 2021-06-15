import random
import string

adjectives = ['aggressive','agreeable','ambitious','brave','calm','delightful','eager','faithful']
nouns = ['area','book','business','case','child','company','country','day','eye','fact','family','government','group','hand','home']

print("You are welcome to password checker")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("Your password is: ",password)

    response = input("would you like to see another password y for yes n for no: ")
    if response=='n':
        break
print("You have a strong password")    

