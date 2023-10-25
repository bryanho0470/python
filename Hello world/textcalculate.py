numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
phone = input("Phone: ")
result = ""
for number in phone:
    result += numbers.get(number, "!!") + " "
print(result)
