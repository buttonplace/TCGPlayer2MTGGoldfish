import sys

if len(sys.argv) != 2:
    print("Usage: 'python TCGtoGoldfish.py <input.txt>'")
    exit()

tcg = sys.argv[1]
out = 'IMPORTME.csv'

with open(tcg, 'r') as tcg, open(out, 'w') as goldfish:
    goldfish.write('Name,Edition,Qty,Foil\n')
    for line in tcg:
        split = line.split()
        name = '\"' + ' '.join(split[1:-1]) + '\"'
        goldfish.write(f'{name},{split.pop(-1)[1:4]},{split.pop(0)},No\n')

print(f"File exported as {out}")
print(f"Import to MTGGoldfish as an MTG Studio file.")