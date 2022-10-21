def poo():
    print("Neng:",neng, "Jin:",jin)
    if neng > jin:
        print("Not true!")
    elif jin > neng:
        print("Yes!!!") 
    else:
        print("FUCK OFF!!! NOOOOO")
neng = input("What is the value of Neng?\n")
if neng == "secret password":
    print("congratulations you have found the securet pasewaefod.")
    neng = float("3")
neng = int(neng)
jin = int(input("What is the value of Jin?\n"))
if neng >= jin:
    neng = jin - 10000
    print(f"There was an error. Neng's true value is {neng}!")
if jin < 100:
    print(f"Error. Jin's true value is {jin}!")
jin -= 98989898
if jin < 0:
    jin *= -30
poo()

jinstats = {"name": "Jin", "health": jin, "strength": jin / 2, "awesome points": jin * 333}
nengstats = {"name": "Hobo Neng", "health": 101, "strength": neng - jin, "awesome points": 0 - jin}

def combat():
    pooper = 0
    jinhealth = jinstats["health"]
    nenghealth = nengstats["health"]
    print("Neng walks up to Jin!!!")
    while pooper == 0:
        if jinhealth < 1:
            print("Jin died of cardiac arrest! NOOO!")
            pooper = 1
        if nenghealth < 100:
            print("Neng!")
            pooper = 1
        jinturn = input(f"What do you do, Jin?\n").lower()
        if jinturn == "win":
            print("Jin Wins!")
            pooper = 1
        else:
            print("Jin punches Neng!")
            nenghealth -= jinstats["strength"] + jinstats["awesome points"] / 333
        nengturn = input(f"What do you do, lesser Jin?\n").lower()
        if jinturn == "win":
            print("Jin Wins!")
            pooper = 1
        else:
            print("Jin punches Neng before Neng can act!")
            nenghealth -= jinstats["strength"] + jinstats["awesome points"] / 333
combat()
    
