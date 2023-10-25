signal = ""
statement = "stop"

while True:
    signal = input('> ').lower()
    if signal == "start":
        if statement == "start":
            print('Car already started')
        else:
            print('Car started...Ready to go!')
            statement = signal
    elif signal == "stop":
        if statement == "stop":
            print('Car already stopped')
        else:
            print('Car stopped')
            statement = signal
    elif signal == "help":
        print("""
        start - to start car
        stop - to stop car
        help - to show tips
        quit - to quit
        """)
    elif signal == "quit":
        break
    else:
        print("Sorry, I don't understand that...")
