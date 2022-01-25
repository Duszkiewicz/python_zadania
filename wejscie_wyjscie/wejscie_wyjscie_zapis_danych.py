set_code = []
print("Set 4 digit code")
for i in range(4):
    set_code.append(int(input()))
check_code = []
print("Put 4 digit code")
for i in range(4):
    check_code.append(int(input()))
good = 0
for i in range(4):
    if set_code[i] == check_code[i]:
        good += 1
if good == 4:
    print("Correct code")
else:
    print("Wrong code")
