import random

def main():
    score = float(input("Enter score: "))
    determine_score(score)
    get_random_score()

def determine_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def get_random_score():
    random_score = random.randint(0, 100)
    print("Random score:", random_score)

main()
