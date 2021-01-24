command = ""
started = True
while command != "quit".lower():
    command = input(">: ")
    if command == "help":
        print("""
        start __ to start the car
        stop __ to stop the car
        quit __ to exit the game
        help -- to read the instruction
        
        """)
    elif command == "start":
        print("the car has started")
    elif command == "stop":
        print("the car has stopped")
    elif command == "quit":
        break
    else:
       print("invalid command")
       break