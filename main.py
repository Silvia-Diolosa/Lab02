import translator as tr

t = tr.Translator() # oggetto di classe translator


txtIn = 0

while(int(txtIn) != 5):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Okay, quale parola devo aggiungere? ")
        parola_input = input()
        t.handleAdd(parola_input)
        print("Parola aggiunta correttamente")

    if int(txtIn) == 2:
        print("Okay, quale parola devo cercare? ")
        parola_input = input()
        pulita = parola_input.lower()
        traduzione = t.handleTranslate(pulita)
        print(f"La traduzione di {parola_input} è {traduzione}")

    if int(txtIn) == 3:
        print("Okay, quale parola devo cercare? ")
        parola_input = input()
        traduzione = t.handleWildCard(parola_input)
        print(f"La traduzione di {parola_input} è {traduzione}")

    if int(txtIn) == 4:
        t.printDiz()

    if int(txtIn) == 5:

        break