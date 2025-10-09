# WH 2nd rock paper scissors

import random
rps = ["""    
              _,==,_
            ,+######+,
            l########l
            '-+####+-'
""","""   
                 ,+^y,
             ,+^'    l
          ,+'        'l
        <'            'l
        'l             'l
         'l             'l
          'l           ,+'
           'l       ,+'
            'l   ,+'
             '+^'
""","""      
             ,-+##+,
            /#>'   `#+,
            l#>,     ##+
             `^l#,__,<##+-
                 '^^^^+l###,
                       '####+,
     ,-+#########*+-,__,-+####+.
    /#>'           `+###########################+.
    l#>.           ,+###########$+^^^^^^^^^^^^^^^'  
     `^l#############l^'      `+#$+
                                `+#$+
                                  `+#$+
                                    `+#$+
                                      `+#$+
                                        '^^'
"""]
comp_score = 0
player_score = 0
while True:
    while True:
      try:
          tape = int(input("\t1. play a game of rock paper scissors\n\t2. curent score\n\t3. exit\n"))
          break
      except:
         print("-------------------------------------------")
         print("not an input")
         print("-------------------------------------------")
    if tape == 1:
      while True:
        while True:
          try:
            print("-------------------------------------------")
            player_rps = int(input(f"Choose one:\n\t1. {rps[0]}\n\t2. {rps[1]}\n\t3. {rps[2]}\n"))
            break
          except:
            print("-------------------------------------------")
            print("not an input")
        comp_rps = random.randint(1,3)
        if player_rps == 1 or player_rps == 2 or player_rps == 3:
            print("-------------------------------------------")
            if comp_rps == 1:
              print(f"{rps[player_rps-1]}\tbeats{rps[(player_rps+4)%3]}")
              player_score += 1
            elif comp_rps == 2:
              print(f"{rps[player_rps-1]}\tties with{rps[(player_rps+5)%3]}")
            else:
               print(f"{rps[player_rps-1]}\tlosses to{rps[(player_rps+6)%3]}")
               comp_score += 1
            print("-------------------------------------------")
            break
        else:
          print("-------------------------------------------")
          print("not an input")
    elif tape == 2:
       print("-------------------------------------------")
       print(f"The computers score is {comp_score}.")
       print(f"Your score is {player_score}.")
       print("-------------------------------------------")
    elif tape == 3:
       break
    else:
       print("-------------------------------------------")
       print("not an input")
       print("-------------------------------------------")
