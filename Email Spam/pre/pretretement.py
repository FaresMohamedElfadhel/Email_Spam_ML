import os
import random
import re

# Obtention du repertoire contenant les email
emails = os.listdir("../Data/easy_ham")
nb_emails = len(emails)

random.seed()
random_email = random.randint(0, nb_emails - 1)

# Ouvrir un email choisie aleatoirement
with open('../Data/easy_ham/' + emails[random_email], 'r') as email_file:
    # with open('../Data/easy_ham/' + '0290.3dc3f5442e351aea16d027b6c5a44e65', 'r') as email_file:
    print('file: ' + emails[random_email] + '\n')
    email = email_file.readlines()

# Le traitement

# 1- Suppression des lignes vides
email = [line.strip() for line in email]
email = [line for line in email if not line == '']
# email[-1] = email[-1][0: -1]
email = ' '.join(email)

# 2- Conversion de l'mail en minuscule
email = email.lower()

# 3- Suppression des balises html
email = re.sub("<.+?>", '', email)

# 4- Suppression des email adresses
email_re = r"\w+([\.\-]?\w+){0,2}@\w+([\.\-]?\w+)*(\.\w{2,3})+"
email = re.sub(email_re, ' emailaddr ', email)

# 5- Suppression des URL
url_re = r"(http\:\/\/|https\:\/\/)?([a-z][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]*([\/\.\-\?,_=%@#]?\w*)*"
email = re.sub(url_re, ' httpaddr ', email)

# 6- Suppression des numeros
email = re.sub(r"\d+", ' number ', email)

# 7- Suppression des symboles de $
email = re.sub(r"\$", ' dollar ', email)

# 8- Radicalization
# SpaCy(email)

# 9- Suppression des caracteres speciaux
email = re.sub(r"[^a-zA-Z]", ' ', email)

# 10- Suppression des espaces
email = ' '.join(email.split())

# 11- Count the frequency of the words. (in a dict)

# 12- Add the k most frequent words from the above dict. (only from the spam emails)

print(email)
