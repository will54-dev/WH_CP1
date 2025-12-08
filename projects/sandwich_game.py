#Wh 2nd final project 
import random as rand
text = {
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
    "event": {
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
        "Investigate the pool of water."
    },
    "pedestal cave": {
            "investigate the pedestal"
    },
    "clearing": {
        "Fight the monkey."
    }
}
encounters = {

}
movement = {
#section one
    "trail"
    "wooded area"
    "brick wall"
    "bench"
#path two
    "courtyard"
    "field"
#path one
    "brick room"
    "pedestal room"
#end
    "cave"
    "pedestal cave"
    "clearing"   
}
chance = {
#section one
    "trail"
    "wooded area"
    "brick wall"
    "bench"
#path two
    "courtyard"
    "field"
#path one
    "brick room"
    "pedestal room"
#end
    "cave"
    "pedestal cave"
    "clearing"   
}
player = {

}
items = {

}
