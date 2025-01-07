fruits=["apples","grapes","mango"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
    print(fruits)
print(fruits)

# exercise 1

#method 1 of find total score
total_score=sum(game_score)
print(total_score)

#method 2 of find the total score
sum=0
for score in game_score:
    sum+=score
print(sum)

#method 1 of find maximum score
print(max(game_score))

#method 2 of find maximum score
max=0
for maxi_score in game_score:
    if max > game_score:
        max=maxi_score
print(max)

#exercise 2
total_score=0
for score in range(1,101):
    total_score+=score
print(total_score)

#exercise 3
for number in range(1,101):
    if number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0 and number%5==0:
        print("Fizz Buzz")
    else:
        print(number)