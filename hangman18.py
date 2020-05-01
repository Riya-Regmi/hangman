
def instruction():
    print('''
    INSTRUCTIONS :
    each field consists of 5 questions:
    score will be increased by 2 when answer is correct
    you can use hint if you like , on using hint score will be deduced by 1
    you can play until hanged man is not seen
        ''')
    choices()

# asked for choices
def choices():
    choice2 = input('''click:
     C to continue
     Q to quit: ''').upper()
    if choice2 == "C":
        field()
    elif choice2 == "Q":
        print(f'your score is={hint}')
        quit()
    else:
        choices()


def geography():
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    global checker
    mat = [
        ['Largest state of America?', 'alaska'],
        ['Turkish city named after cartoon character?', 'batman'],
        ['SAARC science museum loacted in?', 'kirtipur'],
        ['second biggest ocean in world is?', 'atlantic'],
        ['which country lies in equator line?', 'brazil'],
    ]
    k = 0  # to ask question in form of loop
    u = 0
    while k <= 4:
        j = 0
        while j < 1:
            guess_word=[]
            n = 5
            hang=[]
            hang = a.copy()                                   #each question will get new hangman
            p=[]
            ke=[]
            checker=[]
            word = mat[k][1].upper()                         #answer of question asked
            word_list=list(word)
            print(f'{k + 1}.{mat[k][j]}')                    #question is presented on screen
            for it in range(len(word_list)):
                guess_word.insert(it, " _ ")                 #Blank given to guess number of letters in answer
            checking(word_list, word)
            j = j + 1
        k = k + 1
    choices()


def history():
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    global checker
    mat = [
        ["Which country is previously known as 'Dutch East Indies' ?", 'indonesia'],
        ['last kirant king?', 'gasti'],
        ['who built changunarayan?', 'mandev'],
        ['what is pagoda style introduced by Araniko called?', 'paitaste'],
        ['capital city of gopal dynasty?', 'matatirtha'],
    ]
    k = 0
    u = 0
    while k <= 4:
        j = 0
        while j < 1:
            guess_word = []
            n = 5
            hang = []
            hang = a.copy()
            p = []                                                  #Method same as geography only questions are different
            ke = []
            checker = []
            word = mat[k][1].upper()
            word_list = list( word )
            print( f'{k + 1}.{mat[k][j]}' )
            for it in range( len( word_list ) ):
                guess_word.insert( it, " _ " )
            checking( word_list, word )
            j = j + 1
        k = k + 1
    choices()


def field():
    global faculty
    if len(faculty)>1:
        choice = input(f'enter {faculty}  ').upper()
        try:
            if choice == "S":
                del faculty["S"]                                            #When science is chosen it will get deleted from dictinary and function scitech is called
                scitech()
            elif choice == "G":
                del faculty["G"]
                geography()
            elif choice == "L":
                del faculty["L"]
                literature()
            elif choice == "H":
                del faculty["H"]
                history()
            elif choice == "Q":
                print(f'Your score ={hint}')
                quit()
            else:
                field()
        except KeyError:                                                      #When deleted item from a dictionary is once again called
            field()
    elif len(faculty)==1:
        print("*************** CONGRATULATIONS YOU WON *************** ")      #when all field is played successfully
        print(f"Your score ={hint}")
        quit()

def literature():
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    global checker
    mat = [
        ["In which part of Shakespeare do you find the character Ophelia?", 'hamlet'],
        ['What is the name of the infamous novel by Vladimir Nabokov?', 'lolita'],
        ['which book won madan puraskar on 2074 BS', 'yogmaya'],
        ['In the book ‘the Lord of the Rings ‘, who or what is Bilbo?', 'Hobbit'],
        ["who wrote 'Where ignorance is bliss, it is folly to be wise'?", 'Shakespeare'],
    ]
    k = 0
    u = 0
    while k <= 4:
        j = 0
        while j < 1:
            guess_word = []
            n = 5
            hang = []
            hang = a.copy()
            p = []
            ke = []
            checker = []
            word = mat[k][1].upper()
            word_list = list( word )                  #Method same as geography only questions are different
            print( f'{k + 1}.{mat[k][j]}' )
            for it in range( len( word_list ) ):
                guess_word.insert( it, " _ " )
            checking( word_list, word )
            j = j + 1
        k = k + 1
    choices()


def scitech():
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    global checker
    mat = [
        ['In astronomy,what are pallas,vesta and davida', 'asteroids'],
        ['gas evolved from paddy and marsh field', 'methane'],
        ['what is biological polymer of paper', 'cellulose'],
        ['wave used for communication in artificial satellite', 'microwave'],
        ['largest bone of human body', 'femur'],
    ]
    k = 0
    u = 0
    while k <= 4:
        j = 0
        while j < 1:
            guess_word = []
            n = 5
            hang = []
            hang = a.copy()
            p = []
            ke = []
            checker = []
            word = mat[k][1].upper()
            word_list = list( word )
            print( f'{k + 1}.{mat[k][j]}' )               #methods same as geography only questions are different
            for it in range( len( word_list ) ):
                guess_word.insert( it, " _ " )
            checking( word_list, word )
            j = j + 1
        k = k + 1
    choices()


def checking(word_list, word):
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    global checker
    name_list=[]
    finding=[]
    check_list=[]
    ans = ''
    ans_list = []
    collection_list=[]
    if (hang.count(" ")) <6:                                                    #can be played until a hanged man is seen
        if guess_word.count(" _ ") > 0:                                         #Player is asked to enter until all the given blanks are filled
            ans = input(f'Enter:{"".join(guess_word)}').upper()
            ans_list = list(ans)
        elif guess_word.count(" _ ") == 0:                                      #when all the blanks are filled
            ans_list = guess_word
        if ans_list == word_list:                                               #When player enters correct answer
            print(f'{word}  IS CORRECT👍👍👍👍👍👍')
            hint = hint + 2
            print(f"Your score = {hint}")
        else:
            if word_list != ans_list:
                if len( word_list ) >= len( ans_list ):
                    collection_list.clear()                                     #once again initialized list
                    check_list.clear()
                    for it in ans_list:
                        if it not in check_list:
                            check_list.append(it)                               #check_list is for collection of unique letters in a list
                    name_list = list(word).copy()                               #name_list is a copy of list of correct answer
                    for it in check_list:
                        if it not in checker:                                    #checker helps to enter unique letter
                            checker.append(it)
                            if it in word_list:
                                for ia in range(len(word_list)):
                                    if it in name_list:
                                        num = name_list.index(it)
                                        p.append(num)                            #p is to collet index of correctly entered letters
                                        del guess_word[num]                      #deleted blank so coreect letter can occupy its place
                                        guess_word.insert(num, word_list[num])
                                        del name_list[num]                        #deleted position of correct letter from name_list so unique index can be obtained
                                        name_list.insert(num, " _ ")
                            if it not in word_list:
                                collection_list.append(it)                       #collection_list keeps record of incorrect letters
                        elif it in checker:
                            print(f' {it} is already entered 😁')                 #when same letters is entered
                    if len(collection_list)==0:
                        checking(word_list,word)                                  #checking is called when no entered letters are wrong
                    elif len(collection_list)>0:                                  #when incorrect letters are entered
                        for de in range(len(collection_list)):
                            if n >= 0:
                                del hang[n]                                      #one by one body parts of hanged man is deleted
                                hang.insert(n," ")
                                n = n - 1
                        for id in range(1):
                            print(f'🤣🤣🤣🤣🤣🤣🤣🤣 > {"".join(collection_list)} OOPS  🤣🤣🤣🤣🤣🤣🤣🤣🤣')
                            d=(f'''                                    ____________________
                                   |                    |
                                   |                   {hang[0]}
                                   |                 {hang[1]} {hang[2]}                                       
                                   |                   {hang[3]}
                                   |                  {hang[4]}{hang[5]}
                                   |
                                   |
                                   |
                                   ''')
                            print(d.center(50))                                     #Hanged man is displayed on screen
                        for id in range(len(word_list)):
                            if id not in p:                                         #p=collection of index of correctly entered  letters
                                if id not in ke:                                   #ke = collection of index of letter given as hint
                                    i = id
                                    ke.append(id)
                                    if hint>0:
                                        hints(word_list, word)
                                    elif hint==0:
                                        checking(word_list,word)
                                        break
                if len(ans_list)>len(word_list):                                    #when player enters more letters than given blank
                    print("🤨🤨🤨🤨🤨try no to be oversmart")
                    checking(word_list,word)
    if (hang.count(" ")) >=6:                                                     #when all the hanged man's body part is deleted
        print(f'The word={word}')
        print("You are out")
        quit()


def hints(word_list, word):
    global a
    global hint
    global guess_word
    global n
    global hang
    global i
    global p
    global ke
    if hint > 0:
        lifeline_use = input(f'your  {hint} lifeline is present,press L if to use else press NO:').upper()
        if lifeline_use.upper() == "L":
            hint = hint - 1
            print(f'the letter is:{word[i]}')
            checking(word_list, word)
        elif lifeline_use.upper() == "NO":
            if len(ke)>0:
                ke.pop()                                                     #if player doesnot want to use hint then  index of letter to be given as hint is deleted
                checking(word_list, word)
            elif len(ke)==0:
                checking(word_list,word)
        else:
            hints(word_list, word)
    elif hint == 0:
        checking(word_list, word)


#List and Variables initialized
guess_word = []
checker=[]
#List containing elements to build hangman
a = [ ' O', ' \ ' ,' /', ' |', ' /' ,' \ ']
hang = []
hint = 5
i = 0
s = 0
n = 5
p = []
ke = []
#Initialized dictionary containing choices
faculty = {
    "S": "Science",
    "G": "Geography",
    "L": "Literature",
    "H": "History",
    "Q": "Quit"
}
print("************** WELCOME TO HANGMAN GAME ********************")
choice1 = input('''CLICK: 
  I for instruction
  C to continue : ''').upper()
if choice1 == "I":
    instruction()
elif choice1 == "C":
    field()
else:
    choices()
