tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index")

def main():
    global tasks
    print("1 - lisa ülesanne \n2 - kustuta ülesanne \n3 - ülevaadata ülesanded")
    userInput = input("Mida sa tahad teha? ")

    if userInput == "1":
        add_task(input("Sisesta ülesanne: "))
    elif userInput == "2":
        try:
            delete_choice = int(input("Sisestage ülesanne, mida soovite kustutada (index): "))
            delete_task(delete_choice)
        except ValueError:
            print("Palun sisesta kehtiv number.")
    elif userInput == "3":
        if tasks:
            for index, element in enumerate(tasks):
                print(f"{index}. {element}")
        else:
            print("Pole ülesandeid.")
    else:
        print("Sa sisestasid midagi vale.")

main()
