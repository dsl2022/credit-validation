import re

def validate_credit_card(number):
    # Check if it starts with 4, 5, or 6 and contains only digits and optional hyphens
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", number):
        # Remove hyphens and check for consecutive repeated digits
        number = number.replace("-", "")
        if re.search(r"(\d)\1{3,}", number):
            return "Invalid"
        else:
            return "Valid"
    else:
        return "Invalid"

# # Read the number of test cases
# n = int(input())

# # Process each test case
# for _ in range(n):
#     card_number = input()
#     result = validate_credit_card(card_number)
#     print(result)
