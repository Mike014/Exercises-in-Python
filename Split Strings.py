# Completa la soluzione in modo che divida la stringa in coppie di due caratteri. Se la stringa contiene un numero dispari di caratteri, il carattere mancante nella seconda posizione dell'ultima coppia deve essere sostituito con un trattino basso ('_').

# Esempi:
# 'abc' => ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']

# list = ['ab', 'cd', 'ef']
# n = len(list)
# sliced_list = list[-n:]
# print(sliced_list)

def split_string(s):
    # Aggiungi un trattino basso se la lunghezza della stringa è dispari
    if len(s) % 2 != 0:
        s += '_'
    
    # Crea una lista di coppie di due caratteri
    return [s[i:i+2] for i in range(0, len(s), 2)]

# Test degli esempi forniti
print(split_string('abc'))    # Output: ['ab', 'c_']
print(split_string('abcdef')) # Output: ['ab', 'cd', 'ef']





