# WH 2nd crew shares project
while_boll = False
while while_boll == False:
    try:
        money = float(input("how much money did they earn.\n"))
        while_boll = True
    except:
        while_boll = False
while_boll = False
while while_boll == False:
    try:
        crew_number = int(input("how many crew members are there.\n"))
        while_boll = True
    except:
        while_boll = False
captain_shares = 7
first_mate_shares = 3
share = money/(captain_shares+abs(crew_number)+first_mate_shares)
print(f"They earnd a total of {money:.2f}$.\nThey have {abs(crew_number)} crew members.")
print(f"The captain gets: {captain_shares*share:.2f}$\nThe first mate gets: {first_mate_shares*share:.2f}$\n Crew still needs: {share-500:.2f}$")