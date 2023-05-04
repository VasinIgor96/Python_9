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
    name = input("Введіть своє ПІБ: ")
    age = input("Введіть свій вік: ")
    gender = input("Введіть свою стать: ")
    email = input("Введіть свою електронну адресу: ")
    phone = input("Введіть свій номер телефону: ")

    user = {
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone
    }
      
    while True:
        print('1 - зберегти: 2 - завантажити')
        action = input('дія->')
        if action == 'зберегти':
            fields_name = ['name', 'age', 'gender', 'email', 'phone']
            saveCSV([user], FILENAME, fields_name)
        elif action == 'завантажити':
            readCSV(FILENAME)
        else:
            print('Дія не знайдена!')

main()
