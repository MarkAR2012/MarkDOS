import time
import webbrowser
import platform
import os
print("Welcome to MarkDOS!")
while 0 == 0:
    c = 0
    command = input("MarkDOS> ")
    if command == "help":
      print("echo - type this command, press enter, then type what to echo")
      print("exit - the name speaks for itself")
      print("speedtest - count to one million")
      print("speedtestmax - count to ten million")
      print("cls - clear the screen")
      print("osinfo - show operating system info")
      print("calc - type this command, press enter, then type what to calculate")
      print("google - type this command, press enter, then type what to search on google")
      print("youtube - type this command, press enter, then type what to search on youtube")
      c = 1
    if command == "echo":
        echo = input("echo: ")
        print(echo)
        c = 1
    if command == "exit":
      break
    if command == "speedtest":
      start_time = time.time()
      x = 0
      while x < 1000001:
          print(x)
          x = x + 1
      end_time = time.time()
      elapsed_time = end_time - start_time
      print("Elapsed time: " + str(elapsed_time))
      c = 1
    if command == "speedtestmax":
      start_time = time.time
      x = 0
      while x < 10000001:
        print(x)
        x = x + 1
      end_time = time.time
      elapsed_time = end_time - start_time
      print("Elapsed time:" + str(elapsed_time))
      c = 1
    if command == "osinfo":
      print("MarkDOS v0.7 - Stable v1")
      print(platform.platform())
      c = 1
    if command == "cls":
      if os.name == "nt":
          os.system("cls")
      else:
          os.system("clear")
      c = 1
    if command == "calc":
        num1 = input("Number 1: ")
        num2 = input("Number 2: ")
        type = input("Type: (+-*/) ")
        calculation = (num1) + " " + (type) + " " + (num2)
        print(eval(calculation))
        c = 1
    if command == "google":
        query = input("Google search: ")
        url = "https://www.google.com/search?q=" + query
        webbrowser.open(url)
        c = 1
    if command == "youtube":
        query = input("Youtube search: ")
        url = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(url)
        c = 1
    if c == 0:
      print("Invalid command or case")
