#!/usr/bin/python3

import requests

MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    results = requests.get(MYAPI)
   # print(result.text)
    if "1" in results.text:
        print("You won!")
    else:
        print("You lost")

main()
