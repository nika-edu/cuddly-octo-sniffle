while True:
    strength = input("Ange avatarens styrka som ett tal 1 - 10 -> ")
    if strength.isdigit():
        strength = int(strength)
        if strength < 1 or strength > 10:
            continue
        else:
            break

print("Programmet avslutades")
