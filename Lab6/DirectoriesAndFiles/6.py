#Program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

letters = []

for letter in range(65, 91):
    letters.append(chr(letter))

for letter in letters:
    with open(f'F:\Study\Labs\Lab6\DirectoriesAndFiles\ForExamples\ForExample6\{letter}.txt', 'x') as file:
        file.write('')