import random

answer = ''

while len(answer) < 3:
    random_number = str(random.randint(1,9))
    if random_number not in answer:
        answer += random_number

while True:
    x = input("What is your guess? ")
    x = str(x)
    if len(x) != len(answer):
        print('Not 3 digits!')
        continue
    else:
        """ (matches += 1) for i in len(x) if (x[i] == answer[i]) """
        if x == answer:
            print('The number is correct!')
            break
        else:
            for i in range(len(x)):
                if x[i] == answer[i]: print("Number in position " + str(i+1) + " is correct!")
    print("Try again!")
    print()