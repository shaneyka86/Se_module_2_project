import random#imported the random moduke to randomize damage
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):#modified attack method to randomize damage
        random_damage = random.randint(self.attack_power-5,self.attack_power+5)
        opponent.health -= random_damage
        print(f"{self.name} attacks {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Added healing  method here
    def heal(self):
        self.health += 10 #increases health by 10
        print(f"{self.name} heals for 10 health! Current health: {self.health}")



# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def power_shot(self, opponent):
        random_damage = random.randint(self.attack_power-10,self.attack_power+10)
        opponent.health -= random_damage
        print(f"{self.name} uses Power Shot on {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def shield_block(self):
        self.health += 10
        print(f"{self.name} uses Shield Block and gains 10 health! Current health: {self.health}")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)  # Lower health, higher attack power
    # Add your cast spell method here
    def cast_spell(self, opponent):
        random_damage = random.randint(self.attack_power- 20,self.attack_power+20)
        opponent.health -= random_damage
        print(f"{self.name} casts a spell on {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def mana_shield(self):
        self.health += 5
        print(f"{self.name} uses Mana Shield and gains 5 health! Current health: {self.health}")



# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)  # Added Archer class

    # Add your special ability method here
    def poison_arrow(self, opponent):
        random_damage = random.randint(self.attack_power-15,self.attack_power+15)
        opponent.health -= random_damage
        print(f"{self.name} uses Poison Arrow on {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def quick_evade(self):
        self.health += 20
        print(f"{self.name} uses Quick Evade and gains 20 health! Current health: {self.health}")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health= 130, attack_power=25)#added paladin class
    
    def holy_hell(self, opponent):
        random_damage = random.randint(self.attack_power-10,self.attack_power+10)
        opponent.health -= random_damage
        print(f"{self.name} uses Holy Hell on {opponent.name} for {random_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.health += 15
        print(f"{self.name} uses Divine Shield and gains 15 health! Current health: {self.health}")

#EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  # Add Archer class here
    elif class_choice == '4':
        return Paladin(name)# Add Paladin class here
        pass
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Evade attack")
        print("5. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            if isinstance(player, Warrior):
                player.power_shot(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.poison_arrow(wizard)
            elif isinstance(player, Paladin):
                player.holy_hell(wizard)
        elif choice == '3':
            player.heal()
        elif choice =='4':
            if isinstance(player, Archer):
                player.quick_evade()
            elif isinstance(player, Paladin):
                player.divine_shield()
            elif isinstance(player, Warrior):
                player.shield_block()
            elif isinstance(player, Mage):
                player.mana_shield()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()