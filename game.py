import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.gold = 0

    def gain_level(self):
        self.level += 1
        print(f'You are now level {self.level}!')

    def gain_exp(self, amount):
        self.exp += amount

    def gain_gold(self, amount):
        self.gold += amount


class PlayerMoves:
    def __init__(self):
        self.moves = {
            'yell': "Yaahh!",
            'punch': 3,
            'kick': 5
        }
        
    def perform_move(self, player_move):
        try:
            moves = self.moves
            value = self.moves[player_move]
            print(f'You performed move: {player_move}')
            if player_move == 'yell':
                for key in moves:
                    if key != 'yell':
                        moves[key]*= 2
                print(f'Your increased your attack power by 100%!')
                return
            else:
                print(f'You did {value} damage!')
                return value
        except KeyError:
            print("Unknown move!, please choose 'yell', 'punch', 'kick?'")
            return 0

  
class Mob:
    mobs = {
        'Grunt': 1,
        'Elite': 5
    }

    @classmethod
    def spawn_random_mob(cls):
        mob_name, mob_hp = random.choice(list(cls.mobs.items()))
        return mob_name, mob_hp

class BossMob(Mob):
    mobs = {
        'Captain': 15,
        'Beast': 25,
        'Cyclops': 50
    }

def spawn_mob():
    method = random.choice([Mob.spawn_random_mob, BossMob.spawn_random_mob])
    return method()

        
class Game:
    def __init__(self):
        player_name = input('Input Player Name')
        self.player = Player(player_name)
        print(f'Welcome {self.player.name}')
        print(f'Level: {self.player.level} | Exp: {self.player.exp} | Gold: {self.player.gold}')
        print('You venture into the Dungeon')

        mob = Mob()
        self.player_moves = PlayerMoves()

    def play_game(self):
        mob_name, mob_hp = spawn_mob()
        print(f'{mob_name} | (HP: {mob_hp}) appeared!')
        print('What do you do?')

        while mob_hp > 0:
            player_move = input('yell, punch, kick?')
            damage = self.player_moves.perform_move(player_move)
            if player_move in self.player_moves.moves and isinstance(damage, int):
                mob_hp -= damage
                print(f'{mob_name} is hit! | (HP: {mob_hp})')
            else:
                print(f'{mob_name} flinched!')
            if mob_hp <= 0:
                print(f'{mob_name} has been defeated!')
                self.win_fight()
                break

    def win_fight(self):
        exp_gained = 100
        gold_gained = 160
        print(f'You got {exp_gained} Exp and {gold_gained} Gold')
        self.player.gain_exp(exp_gained)
        self.player.gain_gold(gold_gained)
        self.player.gain_level()
        self.display_player_stats()
        
    def display_player_stats(self):        
        print(f'Player Name: {self.player.name} | Level: {self.player.level} | Exp: {self.player.exp} | Gold: {self.player.gold}')

game = Game()
game.play_game()

