#Wh 2nd final project 
import random as rand
import math as m
text = {
    "game": {
        "start": "You are a hiker on a trail having a sandwich then a monkey comes by and has stolen your sandwich and gone off the trail.",
        "end": "you got your sandwich back you win. Would you like to play again?"
    },
    "info": {
    #section one
        "trail": "You are on the trail and the monkey went into the forest. There is nothing around.",
        "wooded area": "You are in a wooded area with lots of little shrubs around.",
        "brick wall":  "You see a big brick wall made of a limestone you see a tomato slice on the side of the wall. The wall has a key hole in the side, nothing else of interest.",
        "bench": "The wall seems to continue on until it abruptly stops and you see a bench with a tissue on it.",
    #path two
        "courtyard": "You find yourself in a courtyard with some dumbbells in the corner and a path forward.",
        "field": "you are in a big field with a rock.",
    #path one
        "brick room": "You are in a brick room with two dores each on one wall, one dore is decorated with stone carvings the other is just made of wood. The room also has a large stone in the middle.",
        "pedestal room": "You enter an empty room with a pedestal in the middle of the room",
    #end
        "cave": "You are in a cave? It has some pickles on the ground, there is a pool of water on your right and the cave continues.",
        "pedestal cave": "You find yourself in another cave with a pedestal in it.",
        "clearing": "You enter a clearing with the monkey in the middle."
    },
    "events": {
    #section one
        #section one
        "trail": {
            "Do nothing.": "Why are you waiting around, the monkey is getting away."
        },
        "wooded area": {
            "Touch the shrub.": "The scrub you touch comes to life and tries to kill you."
        },
        "brick wall": {
            "Mess with the key hole.":  "You fall through the ground.",
            "Use the key.": "The wall opens and you step through."
        },
        "bench": {
            "Pick up the tissue.": "You find a key under the tissue."
        },
    #path two
        "courtyard": {
            "Use the dumbbells to get stronger.":  "You feel stronger."
        },
        "field": {
            "Sit on the rock.":  "you fall through the ground."
        },
    #path one
        "brick room": {
            "Sit on the stone.": "You fell  healthier.",
            "Go to the decorated dore.":  "The dore springs to life and eats you."
        },
        "pedestal room": {
            "Investigate the pedestal.": "The pedestal springs to life and you start fighting."
        },
    #end
        "cave": {
            "Investigate the pool of water.": "You fall into the water."
        },
        "pedestal cave": {
             "investigate the pedestal": "The pedestal springs to life and you start fighting. Wait have we done this before"
        },
        "clearing": {
            "Fight the monkey.": "You walk up to the monkey."
        }
    }
}
events  = {
#section one
    #section one
    "trail": {
        "Do nothing.": [False, False]
    },
    "wooded area": {
        "Touch the shrub.": [False, "battle", "shrub", True]
    },
    "brick wall": {
        "Mess with the key hole.": [False, "move", "brick room", True],
        "Use the key.": [True, "move", "courtyard", True]
    },
    "bench": {
        "Pick up the tissue.": [False, "item", "key", "to", "brick wall", "Use the key.", False, True]
    },
#path two
    "courtyard": {
        "Use the dumbbells to get stronger.": [False, "stat", "strength", 0, True]
    },
    "field": {
        "Sit on the rock.": [False, "move", "cave", True]
    },
#path one
    "brick room": {
        "Sit on the stone.": [False, "stat", "HP", 0],
        "Go to the decorated dore.": [False, "move", "cave", True]
    },
    "pedestal room": {
        "Investigate the pedestal.": [False, "battle", "pedestal", "book", True]
    },
#end
    "cave": {
        "Investigate the pool of water.": [False, "move", "pedestal cave", False]
    },
    "pedestal cave": {
            "investigate the pedestal": [False, "battle", "pedestal", "air fryer", True]
    },
    "clearing": {
        "Fight the monkey.": [False, "battle", "monkey", "win", True]
    }
}
encounters = {
    "pedestal": {
            "entrance":  "You are fighting a living Pedestal.",
            "name": "Pedestal",
            "damage": 0,
            "defense": 0,
            "hp": 0,
            "exit": "The Pedestal returns back to normal and you find something."
    },
    "shrub": {
            "entrance": "You are fighting a living Shrub.",
            "name": "Shrub",
            "damage": 0,
            "defense": 0,
            "hp": 0,
            "exit": "The Shrub bursts into leaves and you find something."
    },
    "brick": {
            "entrance": "A Brick flyers into you and you start fighting.",
            "name": "Brick",
            "damage": 0,
            "defense": 0,
            "hp": 0,
            "exit": "The Brick brakes."
    },
    "leaf": {
            "entrance": "A Leaf flyers into your face. Honestly this is just a joke now.",
            "name": "leaf",
            "damage": 0,
            "defense": 0,
            "hp": 1,
            "exit": "You stomp on the leaf with a satisfying crunch."
    },
    "monkey": {
            "entrance": "you find that the monkey is wearing an amulet. Then you hear rumbling, the earth is shaking and then you see the monkey again but it is wearing a magical suit of glimmering bronze armor. You continue to battle with the monkey.",
            "name": "monkey ",
            "damage": 0,
            "defense": 0,
            "hp": 0,
            "exit": "You punch the monkey and get your sandwich back."
    }
}
movement = {
#section one
    "trail": {
        "Go into the forest.": "wooded area"
    },
    "wooded area": {
        "Go back to the trail.": "trail",
        "Continue into the forest.": "brick wall"
    },
    "brick wall": {
        "Follow the wall.": "bench",
        "Go back into the wooded area.": "wooded area"
    },
    "bench": {
        "Go back to the key hole in the wall.": "brick wall"
    },
#path two
    "courtyard": {
        "Go through the path.": "field"
    },
    "field": {
        "Go back to the courtyard.": "courtyard"
    },
#path one
    "brick room": {
        "Go through the wooden dore.": "pedestal room"
    },
    "pedestal room": {
        "Go back through the dore.": "brick room"
    },
#end
    "cave": {
        "Continue through the cave.": "clearing"
    },
    "pedestal cave": {
        "Go back through the pool of water": "cave"
    },
    "clearing": {
        "Leave": "cave"
    }  
}
chance = {
#section one
    "trail": {
        100: "null"
    },
    "wooded area": {
        75: "null",
        25: "leaf"
    },
    "brick wall": {
        100: "null"
    },
    "bench": {
        100: "null"
    },
#path two
    "courtyard": {
        75: "null",
        25: "brick"
    },
    "field": {
        100: "null"
    },
#path one
    "brick room": {
        75: "null",
        25: "brick"
    },
    "pedestal room": {
        100: "null"
    },
#end
    "cave": {
        100: "null"
    },
    "pedestal cave": {
        100: "null"
    },
    "clearing": {
        100: "null"
    }  
}
player = {
    "hp": 0,
    "strenght": 0,
    "damage": 0,
    "defence": 0,
    "weapon": 'stick"',
    "items": [],
    "position": "trail",
    "battle text": {
        "light attack": "You hit them fast.",
        "attack": "You hit them.",
        "heavy attack":  "You hit them hard."
    },
    "atacks": {
        "light attack": 0,
        "attack": 0,
        "heavy attack": 0
    }
}
items = {
    "air fryer": {
        "attack": 0,
        "speed": 0
    },
    "book": {
        "attack": 0,
        "speed": 0
    },
    "key": {
        "attack": 0,
        "speed": 0
    },
}

def damage(damage, damage_multiplier, defence, defence_multiplier):
    return m.floor((damage*damage_multiplier)-(defence*defence_multiplier**((defence-damage)/1)))

print(damage(10,1,1,2.5))