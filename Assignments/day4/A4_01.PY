#12/8/24 A4_01)Write a program to count the number of each vowel in a sentenece.
sent = input('Write a sentence: ')
a = 0
e = 0
i = 0
o = 0
u = 0

for char in sent:
    if char.lower() == 'a':
        a += 1
    elif char.lower() == 'e':
        e += 1
    elif char.lower() == 'i':
        i += 1
    elif char.lower() == 'o':
        o += 1
    elif char.lower() == 'u':
        u += 1

print(f'''Count of each vowel in the sentence:
a = {a}
e = {e}
i = {i}
o = {o}
u = {u}''')
