import time
import random




traits = []
randomnum = []
yes = ['Y', 'y', 'Yes', 'yes', 'YES', 'YEs', 'YeS', 'yES', 'yeS', 'yEs']
allowed = ['Pikachu', 'Eevee', 'Charmander', 'Bulbasaur', 'Squirtle', 'Doduo', 'Magneton', 'Rattata', 'Voltorb', 'Caterpie', 'Horsea', 'Rhyhorn']
used = []
pokemon = ['Pikachu', 'Eevee', 'Charmander', 'Bulbasaur', 'Squirtle', 'Doduo', 'Magneton', 'Rattata', 'Voltorb', 'Caterpie', 'Horsea', 'Rhyhorn']
#Above is all the variables that are used widely throughout all the functions.
##################################################################################################################################################
def gen():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('traits!')


##################################################################################################################################################
def randomgen(): #rename to randomgen
    i = 0
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Please wait...')

    while i < 300:
        randlang = random.randrange(0, 99999999999999999999999999999999)
        r1 = random.randint(randlang, randlang)
        r2 = random.randint(randlang, randlang)
        r3 = random.randint(randlang, randlang)
        r4 = random.randint(randlang, randlang)
        r5 = random.randint(randlang, randlang)
        r6 = random.randint(randlang, randlang)
        r7 = random.randint(randlang, randlang)
        r8 = random.randint(randlang, randlang)
        r9 = random.randint(randlang, randlang)
        r10 =random.randint(randlang, randlang)
        r11 =random.randint(randlang, randlang)
        r12 = random.randint(randlang, randlang)
        rs = str(r12)
        randomnum.append(r1)
        randomnum.append(r2)
        randomnum.append(r3)
        randomnum.append(r4)
        randomnum.append(r5)
        randomnum.append(r6)
        randomnum.append(r7)
        randomnum.append(r8)
        randomnum.append(r9)
        randomnum.append(r10)
        randomnum.append(r11)
        randomnum.append(r12)
        randomnum.append(rs)
        i += 1
    else: 
        gen()







######################################################################################################################################################
#Below this before the hashed comments, this function allows them to confirm the choices they have made.
def sure():
    print("The pokemon you have entered are:")
    print('')
    print('')
    print('')
    print('')
    print('')
    print(used)
    print('')
    print('')
    print('')
    print('')
    print('')
    sure = input('Are you sure you would like to proceed with the Pokemon? If yes then type y if not type n:')
    if sure in yes:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('running next part...')
        time.sleep(2)
        randomgen()
    else:
        print("Okay, restarting now....")
        print('')
        print('')
        print('')
        print('')
        print('')
        main()
##################################################################################################################################################
def usedpoke():
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Already in use try a different one')
#What we are doing here is we are taking the main function and calling it. If you enter a wrong pokemon it will call NoPoke which says it's not a pokemon and restarts it.
#This is very redundant but it works
def nopoke():
    print('')
    print('')
    print('')
    print('')
    print('')
    print("Not A Pokemon try again!")
####################################################################################
#If it is a pokemon however it will run this function. Which will say it is a pokemon.
def goodpoke():
    print('')
    print('')
    print('')
    print('')
    print('')
    print("Is a pokemon!")
#########################################################################################

#This is the main function where the first things happen
def main(): #rename to main
    print("Please pick a team of generation one pokemon")
    print('')
    print('')
    print('')
    print('')
    print('')
    print("The Pokemon that you are allowd to use are as follows:")
    print('')
    print('')
    print('')
    print('')
    print('')
    print(pokemon)
    while True: 
        p0 = input("First Pokemon: ")
        if p0 in pokemon:
            goodpoke()
            used.append(p0)
            allowed.remove(p0)
            break
        else:
            nopoke()
#The above code runs the functions above
#############################################################################################
    while True:   
        print("The Pokemon that you are allowed to use are as follows:")
        print('')
        print('')
        print('')
        print('')
        print('')
        print(allowed)
        print('')
        print('')
        print('')
        print('')
        print('')
        p1 = input("Second Pokemon: ")
        if p1 in pokemon:
            if p1 in used:
                usedpoke()
            else:
                goodpoke()
                used.append(p1)
                allowed.remove(p1)
                break
        else:
            nopoke()
#The While Loops repeat the function until you get a pokemon that is not used.
######################################################################################
    while True:
        print("The Pokemon that you are allowd to use are as follows:")
        print('')
        print('')
        print('')
        print('')
        print('')
        print(allowed)
        print('')
        print('')
        print('')
        print('')
        print('')
        p2 = input("Third Pokemon: ")
        if p2 in pokemon:
            if p2 in used:
                usedpoke()
            else:
                goodpoke()
                used.append(p2)
                allowed.remove(p2)
                break
        else:
            nopoke()
#####################################################################################################
    while True:
        print("The Pokemon that you are allowd to use are as follows:")
        print('')
        print('')
        print('')
        print('')
        print('')
        print(allowed)
        print('')
        print('')
        print('')
        print('')
        print('')
        p3 = input("Fourth Pokemon: ")
        if p3 in pokemon:
            if p3 in used:
                usedpoke()
            else:
                goodpoke()
                used.append(p3)
                allowed.remove(p3)
                break
        else:
            nopoke()
#####################################################################################################################
    while True:
        print("The Pokemon that you are allowd to use are as follows:")
        print('')
        print('')
        print('')
        print('')
        print('')
        print(allowed)
        print('')
        print('')
        print('')
        print('')
        print('')
        p4 = input("Fifth Pokemon: ")
        if p4 in pokemon:
            if p4 in used:
                usedpoke()
            else:
                goodpoke()
                used.append(p4)
                allowed.remove(p4)
                break
        else:
            nopoke()
################################################################################################################################
    while True:
        print("The Pokemon that you are allowd to use are as follows:")
        print('')
        print('')
        print('')
        print('')
        print('')
        print(allowed)
        print('')
        print('')
        print('')
        print('')
        print('')
        p5 = input("Sixth Pokemon: ")
        if p5 in pokemon:
            if p5 in used:
                usedpoke()
            else:
                goodpoke()
                used.append(p5)
                allowed.remove(p5)
                break
        else:
            nopoke()

    
    sure()

main()
