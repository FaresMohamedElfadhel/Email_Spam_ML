from re import T
import collections
import spacy
# with open("test.txt", "r") as f:
#     text = f.read()


nlp = spacy.load("en_core_web_sm")
vocabulaire = []
k = 3

doc = nlp('best')
for i in range(5):
    email = list(doc.sents)[0]

    mots = {}
    for mot in email.lemma_.split():
        mots[mot] = mots.get(mot, 0)+1
    print(max(mots, key=lambda x: mots[x]))
    mots = {k: v for k, v in sorted(
        mots.items(), key=lambda item: item[1], reverse=True)}
    plus_freq = list(mots.keys())
    if(k < len(plus_freq)):
        plus_freq = plus_freq[:k]

    for plus_frequant in plus_freq:
        if plus_frequant not in vocabulaire:
            vocabulaire.append(plus_frequant)
with open('vocab.txt', 'w') as vocab:
    vocab.write(' '.join(vocabulaire))

# print(mots)


print(plus_freq)


# print(mots)


# for word in email:
#     print(word, word.lemma_)
