is_male = False
is_tall = False

if is_male and is_tall:
    print ("You are a tall male")

elif is_male and not(is_tall):
    print("You are a short male")

elif not (is_male) and is_tall:
    print("You are not a male but tall")

else:
    print("You are neither a male nor tall")