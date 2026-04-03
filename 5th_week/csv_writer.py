import csv

name = input("What's your name? ")
age = input("How old are you? ")

with open("peoplew.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","age"])
    writer.writerow({"name": name, "age":age})