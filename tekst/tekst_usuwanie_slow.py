with open("usuwanie_slow.txt", 'r', encoding="utf8") as file:
    text = file.read()
    text1 = text.replace("się", "")
    text2 = text1.replace("i", "")
    text3 = text2.replace("oraz", "")
    text4 = text3.replace("nigdy", "")
    text5 = text4.replace("dlaczego", "")
print(text5)