import sys
def escaperooms():
    def escaperoom1():
        incorrectpts = 0
        print('Welcome to our Escape room. Find hints and clues to Escape!')
        hint1 = input('I am a show that is animated and My language is revolved around Japanese and sometimes English. | What am I? ')
        if hint1 == 'anime' or hint1 == 'Anime':
            print('Correct! Hint 1 complete')
        else:
            print('Sorry you have gotten the hint incorrect try again!')
            incorrectpts += 1


        hint2 = input('''I am a anime that revolves around superheros and superpowers called 'quirks' | What anime am I? ''')
        if hint2 == 'My Hero Academia' or hint2 == 'my hero academia' or hint2 == 'My Hero' or hint2 == 'my hero':
            print('Correct On to the next hint!')
        else:
            print('Incorrect try again')
            incorrectpts += 1


        hint3 = input('''I am a character in this anime and I go to UA. I have one of the strongest quirks and I have a letter 'I' in my name | Who am I? ''')
        heros = ['Izuku Midoriya', 'Katsuki Bakugo', 'Eijiro Kirishima', 'Kyoka Jiro', 'Mina Ashido', 'Shoto Todoroki']
        if hint3 == heros[0] or hint3 == heros[1] or hint3 == heros[2] or hint3 == heros[3] or hint3 == heros[4] or hint3 == heros[5]:
            print('This is true all of these characters have strong quirks so you are close to the escape! ')
        else:
            print('These hero students have strong quirks but their names do not have an I in their name  ')
            incorrectpts += 1


        hint4 = input('''Last Hint: Which student hero's power first started off as All For One's power that he forcefully gave to his brother? ''')
        if hint4 == heros[0]:
            print('Correct! Now on to the next room!')
        else:
            print('Incorrect Sorry you have failed the escape room.')
            sys.exit()

    def escaperoom2():
        print('Welcome to the second escape room This would test your knowledge on a movie! Good Luck!')
        print('Lets get started!')
        hint1 = input('What holiday that not everyone celebrates and is during at the end of the year? ')
        if hint1 == 'Christmas' or hint1 == 'christmas':
            print('Correct! on to the next hint!')
        else:
            print('Incorrect but on to the next hint to escape!')


        hint2 = input('Thinking about the last hint... What movie revolves around a child tricking adults? ')
        if hint2 == 'Home Alone' or hint2 == 'Home Alone 2' or hint2 == 'Home Alone 3' or hint2 == 'Home Alone 4' or hint2 == 'home alone':
            print('correct movie but which series of the movie is it?')
        elif hint2 == 'Home Alone 3':
            print('Correct! just type this same answer for the next hint!')
        else:
            print('Incorrect But onwards to the next hint!')


        hint3 = input('Which movie has 2 words and  the first word starts with a H the second starts with an A and this movie has a series to it? p.s. make sure you capitilize every first letter of the movie name. ')
        if hint3 == 'Home Alone' or hint3 == 'Home Alone 2' or hint3 == 'Home Alone 3' or hint3 == 'Home Alone 4':
            print('Correct! but which movie is it?')
        else:
            print('Incorrect')


        hint4 = input('If you have gotten that last question incorrect its going to be hard for you but which movie was produced on December 12th of 1997? ')
        if hint4 == 'Home Alone 3' or 'home alone 3':
            print('Correct onto the next room!!')
        else:
            print('You have failed this room try again next time!')
            sys.exit()


    def escaperoom3():
        hint1 = input('''what is something you eat everyday and has a general meaning to it. Also it starts with the letter 'F'. ''')
        if hint1 == 'Food' or 'food':
            print('Correct! ')
        else:
            print('Just think about the riddle and use if for the final riddle.')


        hint2 = input('''Thinking about vehicles I am apart of suv's, 18 wheelers, and vehicles that weigh more than 8,500 pounds (including payload) community. | What am I?  ''')
        if hint2 == 'Trucks' or hint2 == 'trucks':
            print('Correct! And remember every single answer you have gotten correct in this room it will help you in the end.')
        else:
            print('Just think again and keep that answer in your mind! ')


        hint3 = input('I am an action. I do this with cars and people with others to compete for a prize. What am I? ')
        if hint3 == 'Race' or hint3 == 'race':
            print('Correct!')
        else:
            print('Just think about this question one more time because you will need the correct answer for the next and finial hint!')


        hint4 = input('''This is the final hint: Remebering every question that you have answered add "The great" to each answer in order. Also to help you the host of this show is Tyler Florence. What show am I? ''')
        if hint4 == 'The great food truck race' or hint4 == 'The Great Food truck race':
            print('Correct and Congrats you have completed this escape room! I hope you feel proud that you know your different generes of shows and movies.')
            sys.exit()
        else:
            print('You have not completed this escape room try again next time see you!')
            sys.exit()
    escaperoom1()
    escaperoom2()
    escaperoom3()
escaperooms()
