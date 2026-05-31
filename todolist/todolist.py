print("TO-DO LIST")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")