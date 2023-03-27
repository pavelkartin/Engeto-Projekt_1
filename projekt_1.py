"""
projekt_1.py: První projekt do Engeto Online Python Akademie
author: Pavel Kartin
email: pevelkartin@seznam.cz
discord: KKonaPaul#9430
"""



TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
accounts = {
    'bob': '123',
    'ann': 'pass123',
    'mike' : 'password123',
    'liz' : 'pass123',
}
registered = False
separator = "-" * 43
terminate = "Terminating the program..."
texts_amount = len(TEXTS)

# [Vyžádá si od uživatele přihlašovací jméno a heslo]
user = input("Username: ")
entered_password = input("Password: ")
print(separator)

# [Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů]
if user in accounts:
    password = accounts.get(user)
    if entered_password == password:
        registered = True

# [Pokud není registrovaný, upozorni jej a ukonči program]
if not registered:
    print(f"User not found or wrong password. \n{terminate}")
    quit()

# [Pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty]
print(f"Welcome to the app, {user}.\nWe have {texts_amount} texts to be analyzed.")
print(separator)

# [Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS] 
selection = input(f"Enter a number between 1 and {texts_amount} to select: ")
print(separator)

# [Pokud uživatel zadá jiný vstup než číslo]
if not selection.isdigit():
    print(f"The input in not an integer.\n{terminate}")
    quit()
else:
    selection = int(selection)

# [Pokud uživatel vybere takové číslo textu, které není v zadání]
texts_range = range(1, texts_amount + 1, 1) # "+ 1", protože konec je vyloučen
if selection not in texts_range:
    print(f"The entered number \"{selection}\" is not between 1 and {texts_amount}! \n{terminate}")
    quit()

# Rozdělit text na slova
text = TEXTS[selection - 1] # Index začíná od 0
splitted_text = text.split() # ( také převádí položky na řetězce )
words = []

# Odstrait interpunkční znaménka
for word in splitted_text:
    clear_word = word.strip(".,!?")
    words.append(clear_word)

# [Pro vybraný text spočítá následující statistiky:]
words_amount = len(words)
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numbers = []
numbers_sum = 0

for item in words:
    if item.isdigit():
        numbers.append(item)
    elif item.istitle():
        titlecase_words += 1
    elif item.isupper():
        uppercase_words += 1
    elif item.islower():
        lowercase_words += 1

for number in numbers:
    numbers_sum += int(number)

print(f"""There are {words_amount} words in the selected text.
There are {titlecase_words} titlecase words.
There are {uppercase_words} uppercase words.
There are {lowercase_words} lowercase words.
There are {len(numbers)} numeric strings.
The sum of all the numbers {numbers_sum}""")
print(separator)

# [Program zobrazí jednoduchý sloupcový graf, 
# který bude reprezentovat četnost různých délek slov v textu]
word_lengths = {}

for word in words:
    length = len(word)
    if length not in word_lengths:
        word_lengths[length] = 1 # Vytvořit nový klíč slovníku a přidat první hodnotu
    else:
        word_lengths[length] += 1 # Pokud již klíč existuje, přidat 1

longest_word = max(word_lengths.values())
sorted_lengths = sorted(word_lengths.keys())

print(f"LEN|{('OCCURENCES').center(longest_word + 1)}|NR.")
print(separator)

for number in sorted_lengths:
    print(f"{number:3}| {'*' * word_lengths[number]:{longest_word}}| {word_lengths[number]}")
    # ':' nastavuje minimální šířku pole
