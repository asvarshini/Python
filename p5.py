#project 3 of car game
'''command = ""
started =False
while True:
    command= input(">").lower()
    if command =="help":
        print("start - to start the car")
        print("stop  - to stop the car")
        print("quit  - to exit")
    elif command =="start":
        if started:
            print("car already started")
        else:
            started = True
            print("car know started ready to go")
    elif command =="stop":
        if not started:
            print("car already stopped")
        else:
            started =False
            print("car  stopped")
    elif command =="quit":
        break
    else:
        print("i dont understand the command")'''
# project 3.b User can start/stop a car, but the car only works if there is fuel.
# Fuel decreases each time the car starts, and the game continues until the user quits or fuel runs out.
commend =""
started = False
Max_fuel=3

fuel =3
while True:
    commend =input(">").lower()
    if commend =="help":
        print('''
start ---> to start car
fuel ----> to check the fuel
stop ----> to stop the car
Max_suel ----> to check how much fuel in it''')
    elif commend =="start":
        if started:
            print("car started already to go")
        elif fuel ==0:
            print("car is out of fuel refuel to start the car")
        else:
            started =True
            fuel -=1
            print(f"car started ready to go your fule is:{fuel}")
            
        
    elif commend =="stop":
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopeed")
    elif commend == "refuel":
        fuel =Max_fuel
        print(f"car is refuel of{ fuel} your car is ready to go")

    elif commend =="quit":
        break
    else:
        print("sorry! unable to understand")


        


