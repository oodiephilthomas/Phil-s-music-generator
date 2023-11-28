#Data types included(str, int, ?)
#impliment loops

words = [ "Thank you", "for", "using", "my", "program" ]

tryAgain = True #boolean data type. Data types store True or False

while tryAgain:
    #start of program 
    def opening():
        print("welcome to the music recommender")
        print("here we will help you choose your favorite music!")
    opening()

    #choosing a genre menu
    def genre():
        print("what genre will you choose?")
        print("1: Rock", "2: Pop", "3: Rap")
        #selecting a genre
        genre_choice = int(input("please enter your choice: ")) # int data type
        #if genre is rock
        if genre_choice == 1:
            print("you have chosen rock")
            print("here are some artist you may enjoy:")
            print("1: destroy boys", "2: Arctic Monkeys", "3: maneskin")
            artist_choice_rock = int(input("which artist do you like best?"))
            if artist_choice_rock == 1:
                print("you chose Destroy Boys, a great choice!")
                print("here are some songs you may enjoy!")
                print("Shadow", "Drink", "muzzle")
                print("thanks for playing")
            elif artist_choice_rock == 2:
                print("you chose Arctic Monkeys")
                print("here are some songs you may enjoy")
                print("I Wanna be Yours", "Do I Wanna Know", "505")
                print("thanks for playing")
            elif artist_choice_rock == 3:
                print("you have chosen Maneskin")
                print("here are some songs you may enjoy")
                print("Beggin", "I Wanna Be Your Slave", "Gossip")
                print("thanks for playing")
    # pop
        if genre_choice == 2:
                print("you have chosen pop")
                print("here are some artist you may enjoy")
                print("1: Bruno Mars", "2: Michael Jackson", "3: Katy Perry")
                artist_choice_pop = int(input("please enter your choice: "))
                if artist_choice_pop == 1:
                    print("you have chosen Bruno Mars")
                    print("here are some songs you may enjoy:")
                    print("what song will you choose?")
                    print("Thats What I Like", "24k Magic", "Locked Out of Heaven")
                    print("thanks for playing")
                elif artist_choice_pop == 2:
                    print("you have chosen Michael Jackson")
                    print("here are some songs you may enjoy")
                    print("what song will you choose?")
                    print("Billie Jean", "Beat It", "Thriller")
                    print("thanks for playing")
                elif artist_choice_pop == 3:
                    print("you have chosen Katy Perry")
                    print("here are some songs you may enjoy:")
                    print("California gurls", "Dark Horse", "Firework")
                    print("thanks for playing")
    #rap
        if genre_choice == 3:
            print("you have chosen rap")
            print("here are some artists you may enjoy")
            print("1: Jcole", "2: Kendrick lamar", "3: Sheff G")
            artist_choice_rap = int(input("which artist would you like to listen too?:"))
            if artist_choice_rap == 1:
                print("you have chosen Jcole")
                print("here are some songs you may enjoy")
                print("what song will you choose?")
                print("Work Out", "Middle Child", "Deja vu")
                print("thanks for playing")
            elif artist_choice_rap == 2:
                print("you have chosen kendrick lamar")
                print("here are some songs you may enjoy")
                print("what song will you choose?")
                print("United In Grief", "Pride", "Money Trees")
                print("thanks for playing")
            elif artist_choice_rap == 3:
                print("you have chosen Sheff G")
                print("here are some songs you may enjoy")
                print("what song will you choose?")
                print("Picasso", "No suburban", "Moody")
                print("thanks for playing")
    genre()

    # string data type
    reply = input( "Would you like to try again y/n" )

    # If reply is not equal to a yes. != means not equal to
    if reply != "y":
        tryAgain = False

# Go through all the words list, grab each word one by one and print it
for singularWord in words:
    print( singularWord )

