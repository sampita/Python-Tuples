# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("panda", "koala", "giraffe", "lion", "elephant", "monkey", "tiger", "hamster", "squirrel", "platypus")

# Find one of your animals using the tuple.index(value) syntax on the tuple.

print(zoo.index("squirrel"))


# Determine if an animal is in your tuple by using value in tuple syntax.

animal_to_find = "koala"
if animal_to_find in zoo:
    print(f'There is a {animal_to_find} at the zoo.')
else:
    print(f'There is not a {animal_to_find} at the zoo')
    

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
children = ("Sally", "Hansel", "Gretel", "Svetlana")
(first_child, second_child, third_child, fourth_child) = children
print(first_child) # Output is "Sally"
print(second_child) # Output is "Hansel"
print(third_child) # Output is "Gretel"
print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.

(animal_one, animal_two, animal_three, animal_four, animal_five, animal_six, animal_seven, animal_eight, animal_nine, animal_ten) = zoo
print(animal_one)
print(animal_two)
print(animal_three)
print(animal_four)
print(animal_five)
print(animal_six)
print(animal_seven)
print(animal_eight)
print(animal_nine)
print(animal_ten)

# Convert your tuple into a list.
new_list = list( zoo )
print(new_list)

# Use extend() to add three more animals to your zoo.
new_list.extend(["dinosaur", "anteater", "gremlin"])
print(new_list)



# Convert the list back into a tuple.
new_tuple = tuple(new_list)
print("new_tuple:", new_tuple)
