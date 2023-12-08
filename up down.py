"""
Q.1 7 Up or Down Game


You are tasked with creating a "7 Up or Down" game where the user has to guess 

whether a randomly generated number is above, below, or equal to 7. 

Your program should use the random module to generate a random number 

between 1 and 13 (inclusive). The user should then be prompted to make 

their guess. If the user's guess matches the random number, they win!

Otherwise, they lose.


Here are the specific requirements for your program:


1. Your program should generate a random number between 1 and 13 (inclusive)

using the random module.


2. Your program should prompt the user to enter their guess (above, below,

or equal to 7) and store it in a variable.


3. Your program should compare the user's guess to the random number and

print "You win!" if they guessed correctly, or "Sorry, you lose." if they guessed incorrectly.


4. Your program should handle invalid user input (e.g. if the user enters 

"between" instead of "above" or "below").
"""


"""
1.if user choise is below 7: 7down
2.equal to 7: lucky 7
3.above 7 : 7up
"""
user_choise = int(input("Enter your Choise (1,2 or 3): "))
import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print("1st dice :", dice1)
print("2nd dice :", dice2)
sum = dice1 + dice2
if (
    ((user_choise == 1) and (sum < 7))
    or ((user_choise == 2) and (sum > 7))
    or ((user_choise == 3) and (sum == 7))
):
    print("YOU WIN")
else:
    print("YOU LOST,BETTER LUCK NEXT TIME")
