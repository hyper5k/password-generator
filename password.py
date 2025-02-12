import random
import string
import requests

# function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength =  input("how long should your password be")
passwordLength = int (passwordLength)

def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()


def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word

def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "f" in word:
        word = word.replace("f", "%") 
    if "e" in word:
        word = word.replace("e", "P")
    if "o" in word:
        word = word.replace("o", "$")

    return word



def generate_weaker_passoword():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    passoword = word1 + word2
    return passoword

print(generate_weaker_passoword())