from os import system
import battle
while True:
    print("Text Based Battle Simulator")
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Quit")
    print("Credits: Me, Myself, and I")
    choice = int(input(">> "))
    if choice == 1:
        print("Starting...")
        battle.start()
    elif choice == 2:
        print("Loading...")
    elif choice == 3:
        pass
    elif choice == 4:
        system("cls")
        exit(0)
    system("cls")