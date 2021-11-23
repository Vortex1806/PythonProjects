command = ""
status = "stopped"
while command.upper() != 'QUIT':
    command = input("> ")
    if command.lower() == 'help':
        print("""start - to stop the car
stop - to stop the car
quit - to exit""")
    elif command.lower() == 'start' and status == "stopped":
        print('Car started')
        status = 'started'
    elif command.lower() == 'start' and status == "started":
        print("Car is aldready running")
    elif command.lower() == 'stop' and status == "started":
        print('Car Stopped')
        status = 'stopped'
    elif command.lower() == 'stop' and status == "stopped":
        print("Car is aldready at halt")
    elif command.lower() == 'quit':
        exit()
    else:
        print('I dont understand...')