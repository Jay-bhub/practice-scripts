total = 0
con = False
ent = []

while not con:
    print("Would you Like to add an entry? (yes/no)")
    con = input()
    if con == "yes" or con == "Yes":
        print("Add a number: ")
        num = float(input())
        ent.append(num)
        con = False
    elif con == "no" or con == "No":
        con = True

if con == True:
    for entry in ent:
        total += entry

print(total)