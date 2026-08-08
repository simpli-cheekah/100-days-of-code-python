bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) # it removes the decimals finish, but it could be dangerous

print(round(bmi))  # it rounds up the number to a whole number

print(round(bmi, 2)) # it rounds it to 2 decimal places

score = 0

score += 5
print(score)  # instead of writing score = score + 5 just use this, they are assignment variables


#f- strings, to mix different data types

print(f"Your score is: {score}") # easier

print(f"Your score is: " + str(score)) # instead of this
