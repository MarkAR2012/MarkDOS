import time
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
      print("speedtestmax - count to one billion")
      print("cls - clear the screen")
      print("osinfo - show operating system info")
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
      while x < 1000000001:
        print(x)
        x = x + 1
      end_time = time.time
      elapsed_time = end_time - start_time
      print("Elapsed time:" + str(elapsed_time))
      c = 1
    if command == "osinfo":
      print("MarkDOS v0.30")
      print(platform.platform())
      c = 1
    if command == "cls":
      os.system("clear")
      c = 1
    if c == 0:
      print("Invalid command or case")
