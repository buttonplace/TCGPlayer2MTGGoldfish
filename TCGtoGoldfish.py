import sys

if len(sys.argv) != 2:
    print("Usage: 'python TCGtoGoldfish.py <input.txt>'")
    exit()

tcg = sys.argv[1]
goldfish = 'IMPORTME.csv'

with open(tcg, 'r') as tcg, open(goldfish, 'w') as goldfish:
    goldfish.write('Name,Edition,Qty,Foil\n')
    for line in tcg:
        split = line.split()
        count = split.pop(0)
        mtgSet = split.pop(-1)[1:4]
        name = ' '.join(split)
        if ',' in name:
            name = f'\"{name}\"'
        foil = 'No'
        goldfish.write(f'{name},{mtgSet},{count},{foil}\n')
