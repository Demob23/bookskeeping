from random import randint


def get_employees():
    employees = ["Sam", "Deen", "Hugh", "Jack", "Ron", "Judy"]
    workers = []
    for i in range(3):
        workers.append(employees.pop(randint(0, len(employees) - 1)))
        print(employees)
    print("Сегодня на смену заступают:")
    for worker in workers:
        print(worker)
