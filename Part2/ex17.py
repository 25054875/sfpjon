def add_two(number):
    return number + 2

name = input("What's your name? ")
fav_num = int(input("What's your favorite number? "))

new_num = add_two(fav_num)

print(f"Hey {name}, if we add 2 to your favorite number, it becomes {new_num}!")
