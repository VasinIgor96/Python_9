#-*- coding: utf-8 -*-
import csv
FILENAME = "users.csv" 
def saveCSV(data, filename, fields_name):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields_name)
        writer.writeheader()
        writer.writerows(data)
    file.close()
def readCSV(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], "-", row["age"])
def main():
    _name = input("¬вед≥ть ≥м'€ користувача: ")
    _
    _age = input("¬вед≥ть в≥к користувача: ")
    _profession = ("¬вед≥ть профес≥ю користувача: ")
    _
  

    users = [
        {"name": "Bob", "age": 28},
         {"name": "Tommy", "age": 23},
        {"name": "John", "age": 34}
    ]
    while True:
        print('1 - save: 2 - load')
        action = input('action->')
        if action == 'save':
            fields_name = {'name', 'age'}
            saveCSV(users, FILENAME, fields_name)
        elif action == 'load':
            readCSV(FILENAME)
        else:
            print('Action not found!')
main()