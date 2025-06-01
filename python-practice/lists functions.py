lucky_num = [1,2,3,5,4]
friends = ["sam","Tom","Kim","jom", "jim", "jim"]
friends.append("Cat")
print(friends)
friends.insert(1, "Kath")
print(friends)
friends.remove("Cat")
print(friends)
friends.pop()
print(friends)
print(friends.index("jim"))
print(friends.count("jim"))
lucky_num.sort()
print(lucky_num)
friends.sort()
print(friends)
lucky_num.reverse()
print(lucky_num)
friends2 = friends.copy()
print(friends2)
friends.extend(lucky_num)
print(friends)





