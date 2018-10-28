from math import *

# Exercice 01
n = 4
k = 1
freq = {}
listCar = {'.', ',', '!', '?', '`'}
stoplist = open('stopwords_fr.txt', 'r')
stoplist = stoplist.read()
stoplist = stoplist.lower()
stoplist = stoplist.split()


while k <= n:
    print("********** INDEX DE FREQUENCES DU DOCUMENT ", k, " **********")
    f = open('D' + str(k), 'r')
    t = f.read()
    t = t.lower()
    i = 0
    while i < len(t):
        if t[i] in listCar:
            t = t.replace(t[i], "")
        i += 1
    a = t.split()
    nb = len(a)
    for w in a:
        if not w in stoplist and len(w) > 1:
            if not (w, k) in freq:
                freq[w, k] = a.count(w)
                print(w, freq[w, k])
    k += 1
f.close()
print("Le fichier inverse de la collection")
print(freq)

# Exercice 02


def indexdoc(freq, d):
    print("l'index du document ", d, " est")
    for (a, b) in freq:
        if b == d:
            print(a, ': ', freq[a, d])

print("Donner un document: ")
d = int(input())
indexdoc(freq, d)


def indexmot(freq, w):
    print("l'index du mot ", w, "est: ")
    for(a, b) in freq:
        if a == w:
            print(b, ':', freq[w, b])

print("Donner un mot: ")
w = input()
w = w.lower()
indexmot(freq, w)

# Exercice 03
# calcul de ni pour chaque mot dans freq
ni = {}
for (w, d) in freq:
    if not w in ni:
        ni[w] = 1
    else:
        ni[w] += 1
# calcul de la fréquence max de chaque document
max = {}
for(w, d) in freq:
    if not d in max:
        max[d] = freq[w, d]
    else:
        if freq[w, d] > max[d]:
            max[d] = freq[w, d]

# calcul du fichier inverse avec poids TF*IDF

poids = {}
for (w, d) in freq:
    poids[w, d] = (float(freq[w, d])/max[d]) * log10((float(n))/ni[w]+1)
print("Le fichier des poids est: ")
print(poids)

# Exercice 04


def indexdoc(poids, d):
    print("L'index pondéré du document ", d, " est")
    for (a, b) in poids:
        if b == d:
            print(a, ":", poids[a, d])

# Appel de la fonction
print("Donner un document: ")
d = int(input())
indexdoc(poids, d)


def indexmot(poids, w):
    print("les poids du mot ", w, " dans les documents sont: ")
    for(a, b) in poids:
        if a == w:
            print(b, ": ", poids[w, b])
# Appel de la fonction
print("Donner un mot")
w = input()
w = w.lower()
indexmot(poids, w)
