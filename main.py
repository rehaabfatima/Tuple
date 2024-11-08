my_tuple=()
print(my_tuple)

my_tuple=(1,2,3)
print(my_tuple)

my_tuple=("dog",2,3,4,5)
print(my_tuple)

my_tuple=("mouse",[1,2,3],(4,5,6))
print(my_tuple)

my_tuple=("a","b","c","d","e")
print(my_tuple[0])
print(my_tuple[4])

n_tuple=("Hello",[2,3,4,5],(8,9,0,6))

print(n_tuple[0][3])
print(n_tuple[2][3])

print("Sliced :",my_tuple[1:4])

for letters in (my_tuple):
    print("Hello",letters)


