import random
#codes:
#Main_characters: Start with 1, then 1
    #Noire=111
    #Root=112
    #Luna=113
#Enemies: Start with 1, then 2
    #Trish=121
    #Ester=122
    #Nadine=123
    #Follower of false god=124
    #Mary=125
    #Rugs=126
#Weapons: Start with 2
    #Melee weapons: Followed by 1
        #Knife=211
        #Luna´s Axe=212
    #Ranged weapons: Followed by 2
        #Gun= 221
        #Root´s gun= 222
#Items: Start with 4
#characters
class Character:
    def __init__(self, name, current_hearts, max_hearts, id):
        self.name= name
        self.max_hearts= max_hearts
        self.current_hearts= current_hearts 
        self.id=id
class Player(Character):
    def __init__(self, name, current_hearts, max_hearts, id, melee_weapon, ranged_weapon, magazines):
        super().__init__(name, current_hearts, max_hearts, id)
        self.melee_weapon= melee_weapon
        self.ranged_weapon= ranged_weapon
        self.magazines= magazines
    alive= True    
    def melee_attack(self, current_player, current_enemy):
        print(f"Trish´s hearts= {current_enemy.hearts}")
        hit= random.random()
        if hit <= current_player.melee_weapon.base_accuracy:
            print("Hit")
            current_enemy.hearts-= current_player.melee_weapon.base_damage
            print(f"Trish hearts= {current_enemy.hearts}")
        else:
            print("Miss")
            
    def ranged_attack(self, current_player, current_enemy):
        print(f"{current_enemy.name} hearts= {current_enemy.hearts}")
        hit= random.random()
        if hit <= current_player.ranged_weapon.base_accuracy:
            print("Hit")
            current_enemy.hearts-= current_player.ranged_weapon.base_damage
            print(f"Trish hearts= {current_enemy.hearts}")
            current_player.ranged_weapon.ammo-=1
            current_enemy.isalive()
            print(f"new ammo= {current_player.ranged_weapon.ammo}")

        else:
            current_player.ranged_weapon.ammo-=1
            print("Miss")
            print(f"new ammo= {current_player.ranged_weapon.ammo}")
    def talk(self, current_enemy):
        current_enemy.enemy_answer(current_enemy)
    
    def pray(self, current_enemy):
        current_enemy.attack()
    def is_alive(self, current_player):
        if current_player.current_hearts<=0:
            return False
        else: 
            return True
    #items 
    def reload_weapon(self, current_player):
        print("Recargando....")
        input()
        current_player.ranged_weapon.ammo=current_player.ranged_weapon.max_ammo
        current_player.magazines-=1
    def heal(self, current_player):
        if current_player.current_hearts==current_player.max_hearts:
            print("Max health")
        else:
            print("Healed!")
            current_player.current_hearts+=1
    def increase_melee_damage(self, current_player):
        current_player.melee_weapon.base_damage+=1
    def increase_ranged_damage(self, current_player):    
        current_player.ranged_weapon.base_damage+=1
class Enemy(Character):
    def __init__(self, name, current_hearts, max_hearts, id, answer):
        super().__init__(name, max_hearts, current_hearts, id)
        self.answer= answer
    def is_alive(self, current_enemy):
        if current_enemy.hearts<=0:
            current_enemy.die()
        else:
            print("Alive")
    def die(self):
        print("Enemy defeated")
        input()
        clear_window()
    def attack(self, current_player):
        current_player.hearts-=1

    def enemy_answer(self, current_enemy):
        print(f"{current_enemy.answer}")

#weapons
class Weapons:
    def __init__(self, weapon_name, base_damage, base_accuracy, id):
        self.weapon_name= weapon_name
        self.base_damage= base_damage
        self.base_accuracy= base_accuracy
        self.id= id
class Melee_weapons(Weapons):
    def __init__(self, weapon_name, base_damage, base_accuracy, id):
        super().__init__(weapon_name, base_damage, base_accuracy, id)
        
class Ranged_weapons(Weapons):
    def __init__(self, weapon_name, base_damage, base_accuracy, id, ammo, max_ammo):
        super().__init__(weapon_name, base_damage, base_accuracy, id)
        self.ammo= ammo
        self.max_ammo= max_ammo

        
        
#objects        
class Objects:
    def __init__(self, object_name):
        self.object_name= object_name
class Healing_objects(Objects):
    def __init__(self, object_name):
        super().__init__(object_name)


#assignations    
knife= Melee_weapons("Knife", 1, 0.85, 211)
gun= Ranged_weapons("Gun", 2, 0.75, 221, 6, 6)
potion= Healing_objects("Potion")      
Noire= Player("Noire", 5, 5, 111, knife, gun, 1)

Trish= Enemy("Trish", 4, 4, 121, "I hate you")

current_player= Noire
current_enemy= Trish
current_player.is_alive(current_player)
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()