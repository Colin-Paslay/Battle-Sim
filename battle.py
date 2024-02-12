from random import randint
class Actor:
    def __init__(self):
        self.hp = 15
        self.ap = 3
        self.atk1 = 2
        self.atk1ap = 1
        self.atk2 = 8
        self.atk2ap = 3
        self.dfn = 1
player = Actor()
enemy = Actor()
def attack():
    print(f"AP: {player.ap}")
    print(f"1. Light Attack | AP: {player.atk1ap} | DMG: {player.atk1}")
    print(f"2. Heavy Attack | AP: {player.atk2ap} | DMG: {player.atk2}")
    action = int(input(">> "))
    if action == 1 and player.ap > 0:
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
        print(f"You did {player.atk1} damage")
    elif action == 2 and player.ap > 2:
        oooooooooooooooooo = randint(player.atk2/2, player.atk2)
        enemy.hp -= oooooooooooooooooo
        player.ap -= player.atk2ap
        print(f"You did {oooooooooooooooooo} damage")
    else:
        print("You're too tired to act")
def defend():
    if player.ap > 0:
        player.hp -= 4
        player.ap -= 1
    else:
        print("You're too tired to act")
def wait():
    player.ap += 2
def enemy_turn():
    if enemy.ap >= 3:
        oooooooooooooooooo = randint(enemy.atk2/2, enemy.atk2)
        player.hp -= oooooooooooooooooo
        enemy.ap -= enemy.atk2ap
        print(f"You took {oooooooooooooooooo} damage")
    elif enemy.ap == 0:
        enemy.ap += 2
        print("The enemy recovers")
    elif enemy.hp <= 5:
        enemy.hp += 3
        enemy.ap -= 1
        print("The enemy patches itself up")
    else:
        player.hp -= enemy.atk1
        enemy.ap -= enemy.atk1ap
        print(f"You took {enemy.atk1} damage")
def start():
    while enemy.hp > 0:
        print("Choose your action")
        print(f"HP: {player.hp} | AP: {player.ap}")
        print(f"Enemy HP: {enemy.hp}")
        print("1. Attack")
        print("2. Defend")
        print("3. Wait")
        action = int(input(">> "))
        if action == 1:
            attack()
        elif action == 2:
            defend()
        elif action == 3:
            wait()
        enemy_turn()
        if player.hp <= 0:
            input("You Died")
            break
    input("YOU WIN!")