# Lesson 5

money = float(input("Enter the amount of money: "))
cookies = input("Which cookies did you get? ")

# big_cookies = 0
# normal_cookies = 0

big_cookies = cookies.count("b")
normal_cookies = cookies.count("c")

# for current_cookie in cookies:
#     if current_cookie == "c":
#         normal_cookies += 1
#     elif current_cookie == "b":
#         big_cookies += 1
#     else:
#         print(f"{current_cookie} is not a valid sale item")

total_cookies = big_cookies + normal_cookies

sales = (normal_cookies * 1.25) + (big_cookies * 2)
cost = (normal_cookies * 0.5) + (big_cookies * 0.75)
profit = sales - cost
total = money + profit

print(f"You sold {total_cookies}, made ${profit} in profit, and now have ${total}.")