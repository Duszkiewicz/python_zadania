with open("usuwanie_slow.txt", 'r', encoding="utf8") as file:
    text1 = file.read()
    text2 = text1.replace("i", "oraz")
    text3 = text2.replace("oraz", "i")
    text4 = text3.replace("nigdy", "prawie nigdy")
    text5 = text4.replace("dlaczego", "czemu")
print(text5)