from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice,randint,shuffle
import re

if not isfile("Words.txt"):
    print ("Downloading Words.txt...")
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    with open("Words.txt","wb") as f:
        f.write(urlopen(url).read())

#open the file in read mode and splitting words on the delimiter /n
words=open("Words.txt","r").read().split("\n")
special_chars=["-","_","!","?"]

def password_check(password):
    """
    Verify the strength of 'password'
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"\W", password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
    if(password_ok):
        return 'Password Strong'
    else:
        return{
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }
def create_password(num_words=2,num_numbers=3,num_special=1):
 '''giving a default value for no of word characters,no of digits,no of special characters;
    digits are specified by making use of randint,
    special chars are mentioned from special_Chars given,
    words are taken from Words.txt 
 '''   
 pass_str=""
 for _ in range(0,num_words):
  pass_str+=choice(words).lower().capitalize()
 for _ in range(num_numbers):
  pass_str+=str(randint(0,9))
 for _ in range(num_special):
  pass_str+=choice(special_chars)
 return pass_str


def main():
 pass_str=create_password()
 pass_str1=list(pass_str)
 shuffle(pass_str1)
 pass_str2=''.join(pass_str1)
 strength,_=test(pass_str2)
 print("PASSWORD: %s"%pass_str2)
 #checks the strength of password 
 print("STRENGTH: %0.5f"%strength)
 print(password_check(pass_str2))
if __name__=="__main__":
 main()

