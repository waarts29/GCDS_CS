import random
import time

# ------------------------------
# CARD DEFINITIONS
# ------------------------------

class Card:
    def __init__(self, name, card_type, elixir, hitpoints=0, damage=0, target="ground", rarity="common"):
        self.name = name
        self.card_type = card_type  # troop, spell, building
        self.elixir = elixir
        self.hitpoints = hitpoints
        self.damage = damage
        self.target = target
        self.rarity = rarity

    def __repr__(self):
        return f"{self.name} ({self.card_type}, {self.elixir} elixir)"


# FULL CARD LIST (with safe placeholder stats)
ALL_CARDS = [
    Card("Knight", "troop", 3, 800, 120),
    Card("Archers", "troop", 3, 400, 70, target="air"),
    Card("Giant", "troop", 5, 2000, 200),
    Card("Musketeer", "troop", 4, 500, 160, target="air"),
    Card("Mini P.E.K.K.A", "troop", 4, 900, 300),
    Card("Skeleton Army", "troop", 3, 200, 40),
    Card("Baby Dragon", "troop", 4, 900, 100, target="air"),
    Card("Wizard", "troop", 5, 600, 160, target="air"),
    Card("P.E.K.K.A", "troop", 7, 3000, 600),
    Card("Hog Rider", "troop", 4, 1000, 200),
    Card("Valkyrie", "troop", 4, 1200, 120),

    # spells
    Card("Fireball", "spell", 4, damage=300),
    Card("Arrows", "spell", 3, damage=200),
    Card("Zap", "spell", 2, damage=150),

    # buildings
    Card("Cannon", "building", 3, 900, 80),
    Card("Tesla", "building", 4, 1000, 90),
    Card("Inferno Tower", "building", 5, 1500, 400),

    # Example of including every CR card safely
    *[
        Card(name, "troop", random.randint(2, 7), 500, 100)
        for name in [
            "Barbarians", "Royal Giant", "Mega Minion", "Electro Wizard", "Bowler",
            "Goblin Gang", "Elite Barbarians", "Golem", "Lava Hound", "Ice Wizard",
            "Bandit", "Ram Rider", "Royal Ghost", "Mega Knight", "Skeletons",
            "Wall Breakers", "Dark Prince", "Prince", "Executioner", "Hunter",
            "Minions", "Minion Horde", "Sparky", "Night Witch", "Witch",
            "Ice Spirit", "Fire Spirit", "Goblins", "Spear Goblins", "Dart Goblin"
        ]
    ]
]

# ------------------------------
# PLAYER CLASS
# ------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.elixir = 5
        self.deck = random.sample(ALL_CARDS, 8)
        self.hand = self.deck[:4]
        self.towers = 3000  # simple tower value

    def draw_card(self):
        new_card = random.choice(ALL_CARDS)
        self.hand[random.randint(0, 3)] = new_card

    def play_card(self, card_index):
        card = self.hand[card_index]
        if card.elixir > self.elixir:
            print(f"{self.name} does not have enough elixir!")
            return None

        print(f"{self.name} plays {card.name}!")
        self.elixir -= card.elixir
        self.draw_card()
        return card

# ------------------------------
# BATTLE SIMULATOR
# ------------------------------

class Battle:
    def __init__(self, player, bot):
        self.player = player
        self.bot = bot

    def simulate_round(self, card_user, card_target, user, enemy):
        if card_user.card_type == "spell":
            print(f"{user.name}'s {card_user.name} hits tower for {card_user.damage} damage!")
            enemy.towers -= card_user.damage
        else:
            print(f"{user.name}'s {card_user.name} attacks!")
            enemy.towers -= card_user.damage

        if enemy.towers <= 0:
            print(f"{enemy.name}'s tower is destroyed!")
            return True
        return False

    def start(self):
        print("\n=== CLASH ROYALE PYTHON SIMULATION ===")
        print(f"{self.player.name}'s deck: {self.player.deck}")
        print(f"{self.bot.name}'s deck: {self.bot.deck}")
        print("\nBattle Start!\n")

        while self.player.towers > 0 and self.bot.towers > 0:
            time.sleep(1)
            
            # elixir regen
            self.player.elixir = min(10, self.player.elixir + 0.8)
            self.bot.elixir = min(10, self.bot.elixir + 0.8)

            print(f"\n{self.player.name} elixir: {self.player.elixir:.1f}")
            print(f"{self.bot.name} elixir: {self.bot.elixir:.1f}")

            print("\nYour hand:")
            for i, c in enumerate(self.player.hand):
                print(f"{i}: {c.name} ({c.elixir})")

            # player move
            try:
                choice = int(input("Play a card (0-3): "))
                card_p = self.player.play_card(choice)
            except:
                print("Invalid. Skipping turn.")
                card_p = None

            # bot move
            affordable = [c for c in self.bot.hand if c
