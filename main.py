# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request
from sys import argv
import urllib3
from os import system as terminal
import requests
from colorama import Fore, Style

count = input("Oluşturulacak Proxy Sayısı: ")
proxy_api = "https://www.proxyscan.io/api/proxy?format=txt&type=http"

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    i = int(count)

    for x in range(i):
        with urllib.request.urlopen(proxy_api) as url:
            s = url.read()
            proxy = (s.strip().decode("utf-8"))
            # print(x, ".", "Proxy")
    else:
        print("Finally finished!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
