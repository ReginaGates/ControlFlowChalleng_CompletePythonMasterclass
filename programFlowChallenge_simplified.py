#Complete Python Masterclass - Tim Buchalka & Jean-Paul Roberts
#Challeng - Program Flow

#Simplified

name = input("What is your name? ")
user_IP_address = input("Hello, {}, what is your IP address? ".format(name))

seg_count = 0
new_string = ''


# if user_IP_address[-1] == '.':
#     for char in user_IP_address:
#         if char not in '0123456789':
#             seg_count += 1
#
if user_IP_address[-1] != '.':
#     for char in user_IP_address:
#         if char not in '0123456789':
#             seg_count += 1
#     seg_count += 1
    user_IP_address += '.'
#
# print("This IP address has {} segments.".format(seg_count))
#
# seg_count = 0

for char in user_IP_address:
    if char in '0123456789':
        new_string += char
    elif char == '.':
        seg_count += 1
        print("Segment {0} has {1} digits.".format(seg_count, len(new_string)))
        new_string = ''
