import re

def validate_credit_card(number):
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", number):
        number = number.replace("-", "")
        if re.search(r"(\d)\1{3,}", number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

# # Read the number of test cases for hackerrank
# n = int(input())

# # Process each test case
# for _ in range(n):
#     card_number = input()
#     result = validate_credit_card(card_number)
#     print(result)
