#WH 2nd tic tac toe

bord = ["x","x","x","x","x","x","x","x","x"]

if bord[0] == "x" and bord[1] == "x" and bord[2] == "x":
    print("computer won")
    break
elif bord[3] == "x" and bord[4] == "x" and bord[5] == "x":
    print("computer won")
    break
elif bord[6] == "x" and bord[7] == "x" and bord[8] == "x":
    print("computer won")
    break
if bord[0] == "x" and bord[4] == "x" and bord[8] == "x":
    print("computer won")
    break
elif bord[6] == "x" and bord[4] == "x" and bord[2] == "x":
    print("computer won")
    break
if bord[0] == "x" and bord[3] == "x" and bord[6] == "x":
    print("computer won")
    break
elif bord[1] == "x" and bord[4] == "x" and bord[7] == "x":
    print("computer won")
    break
elif bord[2] == "x" and bord[5] == "x" and bord[8] == "x":
    print("computer won")
    break