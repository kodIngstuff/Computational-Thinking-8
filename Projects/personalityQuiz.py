#Beginning
import time

print("Welcome to your personality quiz!")
time.sleep(2)
print("This quiz will tell you where to take your next vacation.")
time.sleep(2)

USA_points = 0
france_points = 0
japan_points = 0
hawaii_points = 0

#Middle

answer = input("On a sunny day would you rather A) play video games, B) go outside to a historical monument, C) go to your favorite hamburger stand, or D) hang out at the beach\n")
if answer == "A":
    japan_points += 1
    hawaii_points -=1
elif answer == "B":
    france_points += 1
    USA_points -=1
elif answer == "C":
    USA_points += 1
    japan_points -=1
elif answer == "D":
    hawaii_points +=1
    france_points -=1

print("Ha! I like your answer!")
time.sleep(1)
answer = input("Would you rather go to A) a sushi restaurant, B) a gourmet pastry shop, C) a poke bowl restaurant, or D) a fried chicken restaurant\n")
if answer == "A":
    japan_points += 1
    USA_points -=1
elif answer == "B":
    france_points += 1
    japan_points -=1
elif answer == "C":
    hawaii_points += 1
    france_points -=1
elif answer == "D":
    USA_points +=1
    hawaii_points -=1

answer = input("Would you rather A) a tropical climate, B) A hot climate, C) A cold climate, or D)a temperate climate\n")
if answer == "A":
    hawaii_points += 1
    japan_points -=1
elif answer == "B":
    USA_points += 1
    france_points -=1
elif answer == "C":
    france_points += 1
    USA_points -=1
elif answer == "D":
    japan_points +=1
    hawaii_points -=1

answer = input("Would you rather A) watch an anime movie, B) watch a historical documentary, C) , watch a surfing video on youtube or D) watch a true crime show\n")
if answer == "A":
    japan_points += 1
    france_points -=1
elif answer == "B":
    france_points+= 1
    japan_points -=1
elif answer == "C":
    hawaii_points += 1
    USA_points -=1
elif answer == "D":
    USA_points +=1
    hawaii_points -=1

answer = input("Would you rather A) a pet cat, B) A pet dog, C) A pet bird, or D)a pet dolphin\n")
if answer == "A":
    japan_points += 1
    USA_points -=1
elif answer == "B":
    USA_points += 1
    japan_points -=1
elif answer == "C":
    france_points += 1
    hawaii_points -=1
elif answer == "D":
    hawaii_points +=1
    france_points -=1

    answer = input("Would you rather get A) red roses, B) dandelions, C) white orchids, or D) lotus flowers\n")
if answer == "A":
    france_points += 1
elif answer == "B":
    USA_points += 1
elif answer == "C":
    hawaii_points +=1
elif answer == "D":
    japan_points +=1

answer = input("On a rainy day, would you A) stay inside, B) soak in the rain outside, C) go to a cafe and read poetry, or D) make some soup and listen to the lovely raindrops?\n")
if answer == "A":
    USA_points += 1
elif answer == "B":
    hawaii_points += 1
elif answer == "C":
    france_points +=1
elif answer == "D":
    japan_points +=1

print ("Now tell me...")
time.sleep(2)
answer = input ("Would you drink A) Green Tea, B) Starbucks Coffee, C) Hipster Cafe Coffee, or D) Coconut Water?\n")
if answer == "A":
    japan_points += 1
elif answer == "B":
    USA_points += 1
elif answer == "C":
    france_points +=1
elif answer == "D":
    hawaii_points +=1

answer = input ("What kind of aquatic animal is your favorite, A) Mackerel, B) Lobster, C) Cod, or D) Tuna\n")
if answer == "A":
    japan_points += 1
elif answer == "B":
    USA_points += 1
elif answer == "C":
    france_points +=1
elif answer == "D":
    hawaii_points +=1

print ("Okay, final question...")
time.sleep(2)
answer = input ("Would you rather A) go to South Korea, B) go to Canada, C) go to Belgium, or D) go to Tahiti?\n")
if answer == "A":
    japan_points += 2
elif answer == "B":
    USA_points += 2
elif answer == "C":
    france_points += 2
elif answer == "D":
    hawaii_points += 2

#end:

if france_points>=japan_points and france_points >= hawaii_points and france_points >= USA_points:
    print ("You should go to France, the land of big steel towers, croissants, and lots of history.")
elif hawaii_points>=japan_points and hawaii_points >=japan_points and hawaii_points >=USA_points:
    print ("You should go to Hawaii, soak up the sun, waves, and sand of the beach and tour the natural beauty of the islands.")
elif USA_points>=japan_points and USA_points>=france_points and USA_points >=hawaii_points:
    print ("You should stay in the USA, maybe go to one of the different states, there's something unique to explore in all of them!")
elif japan_points>=USA_points and japan_points>=france_points and japan_points >=hawaii_points:
    print ("You should stay here, maybe go to one of the different states, there's something unique to explore in all of them!")