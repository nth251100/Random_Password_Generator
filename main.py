import string
import random 

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def password_generator(password_generator):
  printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
  
  printable = list(printable)
  random.shuffle(printable)

  random_password = random.choices(printable , k = password_generator)
  random_password = ''.join(random_password)

  return random_password

def get_password_lenght():
  password_lenght = input("How long do you want your password: ")
  return int(password_lenght)

def main():
  password_lenght = get_password_lenght()
  password = password_generator(password_lenght)
  print(password)

if __name__ == "__main__":
  main()