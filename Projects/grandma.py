import time
while True:
    word = input("What do you think grandma likes?")

    if "t" in word or "v" in word:
        print(f"Grandma doesn't like {word}")
    else:
        print(f"Grandma likes {word}")

    print("")

    if "violin" in word:
        print(f"that instrument is completely the best. You are the greatest grandson/granddaughter I've ever had.")
    else:
        print(f"Grandma says: try the word violin")

    if "grandma" in word:
        print(f"What'dya thing was gonna happen")
        time.sleep(3)
        print("Ha! I like myself")