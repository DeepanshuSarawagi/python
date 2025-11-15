computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]

"""Carefully observe below code where you will see how Python behaves when you want to replace an item in a list using list slicing"""
# computer_parts[3:5] = "trackball"  # This will output ['computer', 'monitor', 'keyboard', 't', 'r', 'a', 'c', 'k', 'b', 'a', 'l', 'l', 'hdmi cable']
# To resolve this issue, following is the right way of ding it
computer_parts[3:5] = ["trackball"]
print(computer_parts)