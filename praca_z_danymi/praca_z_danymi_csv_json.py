import csv
lines = list()
i = 0
with open('obowiazki.csv', 'r', encoding="utf-8", newline='' ) as readFile:
    data = csv.reader(readFile)
    for row in data:
        lines.append(row)
        print(i, row)
        i += 1
readFile.close()

print("Choose your action")
print("1. Add new data")
print("2. Remove old one")
action = int(input())

if(action == 1):
     print("Put your new chore")
     new_chore = input()
     print("Put chore priority")
     priority = input()
     lines.append([new_chore, priority])

elif(action == 2):
    print("Put which row you would like to delete")
    delete = int(input())
    j = 0
    for row in lines:
        if j == delete:
            lines.remove(row)
        j += 1

with open('obowiazki.csv', 'w', encoding="utf-8", newline='') as writeFile:
    new_data = csv.writer(writeFile)
    new_data.writerows(lines)
writeFile.close()
