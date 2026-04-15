# Basic File Logger

while True:
    try:
        #user input
        action = input("Enter user action (type 'exit' to stop): ")

        #Exit condition
        if action.lower() == 'exit':
            print("Stopped logging.")
            break

        #Open file in append mode and write data
        with open("user_logs.txt", "a") as file:
            file.write(action + "\n")

        print("Action logged successfully!")

    # Step 4: Handle file-related errors
    except IOError:
        print("Error: Problem writing to file.")

    # Step 5: Handle unexpected errors
    except Exception as e:
        print("Unexpected error:", e)
