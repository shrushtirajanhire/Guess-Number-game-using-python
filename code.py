import random
secret_number = random.randint(0,50)
guess_count=0
guess_limit=3
print("Secret number should be in between 1 to 50 ")
while guess_count<guess_limit:
    guess = int(input("Guess :"))
    guess_count += 1
    if guess==secret_number :
        print("you won")
    else:
        print("you lose")

print(f"The secret number is {secret_number}")
