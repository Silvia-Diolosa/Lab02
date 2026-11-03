class Dictionary:
    def __init__(self, diz = {}):
        self.diz = diz

    def __str__(self):
        risultato = ""
        for key in self.diz:
            risultato = risultato + (f"{key}: {self.diz[key]}") + "\n"
        return risultato

    def addWord(self, entry):
        # non gestisce caso in cui mettiamo più traduzioni assieme
        if entry[0] not in self.diz:
            self.diz[entry[0]] = entry[1]
        else:
            valore_prec = self.diz.get([entry[0]])
            if isinstance(valore_prec, str): # se era una stringa (un solo valore)
                valore_nuovo = [] # trasforma in lista
                valore_nuovo.append(valore_prec) #e aggiunge il valore di prima
            else:
                # se era già lista, prende semplicemente questa lista
                valore_nuovo = self._diz.get(entry[0])

            # in entrambi i casi, poi aggiunge i nuovi valori scritti nell'entry
            self._dict[entry[0]] = [*valore_nuovo, entry[1]]
            # Crea una nuova lista con tutti gli elementi di currentVal (* li “spacchetta”) più la nuova traduzione in fondo,
            # e la salva al posto del valore vecchio




    def translate(self, entry):
        return self.diz[entry]



    def translateWordWildCard(self, entry):
        sostituito = "abcdefghijklmnopqrstuvwxyz"
        match = {}

        for char in sostituito:
            nuovo = entry.replace("?", char)
            if nuovo in self.diz:
                match[nuovo] = self.diz[nuovo]

        return match



    def carica_dizionario(self,diz):
        infile = open(diz, "r", encoding="utf-8")
        contenuto = infile.read().splitlines()
        for linea in contenuto:
            linea_split = linea.split(" ")
            self.diz[linea_split[0]] = linea_split[1]
        infile.close()



    #per effettivamente modificare file dizionario

    # def saveDictionary(self, file_path="dictionary.txt"):
    #     with open(file_path, "w", encoding="utf-8") as f:
    #         for parola, traduzioni in self._dict.items():
    #             if isinstance(traduzioni, str):
    #                 traduzioni = [traduzioni]
    #             f.write(parola + " " + " ".join(traduzioni) + "\n")