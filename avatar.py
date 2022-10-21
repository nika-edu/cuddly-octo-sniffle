while True:
    styrka = input("Ange avatarens styrka som ett tal 1 - 10 -> ")
    if styrka.isdigit():
        styrka = int(styrka)
        if styrka < 1 or styrka > 10:
            continue
        else:
            break

print("Programmet avslutades")
