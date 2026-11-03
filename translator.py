# Dictionary si occupa dei dati: come sono memorizzate le parole, come si aggiungono, come si cerca
# (anche con wildcard). Non sa nulla di menù, print dell’interfaccia o input.
# Translator si occupa dell’applicazione: il menù, la lettura dell’input dell’utente, i controlli sulla
# sintassi (“solo lettere a-zA-Z”, “un solo ?”), il formato dei messaggi.

from dictionary import Dictionary

class Translator:

    def __init__(self, diz =Dictionary()):
        self._diz = diz # è un oggetto di classe dizionario

    def printMenu(self):
        print("______________________________")
        print("   Translator Alien-Italian")
        print("______________________________")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("________________________________")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self._diz.carica_dizionario(dict)



    def handleAdd(self, txtEntry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entry = txtEntry.split(" ")
        print(entry)
        self._diz.addWord(entry)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self._diz.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self._diz.translateWordWildCard(query)


    def printDiz(self):
        print(self._diz)