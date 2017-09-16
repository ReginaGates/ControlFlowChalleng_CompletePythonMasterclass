#Complete Python Masterclass - Tim Buchalka & Jean-Paul Roberts
#Challenge - Program Flow

#Regina Gates - First efforts with many edits, but without checking, and without correcting for all cases, like the IP
# address starting with '.'
# Even though this code does not account for every error, including adding a + sign, which signals a segment count,
# I'm going to submit to github, before I watch the solution video. -RG

name = input("What is your name? ")
user_IP_address = input("Hello, {}, what is your IP address? ".format(name))

seg_count = 0 #this increments with each number of the enetered IP address.
new_string = '' # created this to help track the hidden changes in the program,
                # to ensure the program was working. Will take the length
                # to report this informationt to the user.

# Handle the error if the user inputs an empty string.
if user_IP_address == '':
    user_IP_address = input("Please enter a valid IP address? ")


# If the terminal value of the IP address is a period, 
elif user_IP_address[-1] == '.': #updated for efficiency, after viewing solution
    for char in user_IP_address:
        if char not in '0123456789':
            seg_count += 1
    # In the case the beginning value of the IP add. is '.', we want to ignore it
    # for the segment count.
    if user_IP_address[0] == '.':
        seg_count -= 1 

# This code forces this statement to count the final segment.
elif user_IP_address[-1] != '.': #updated for efficiency
    for char in user_IP_address:
        if char not in '0123456789':
            seg_count += 1
    seg_count += 1
    # This appends a '.' onto the IP add. so the final FOR statement can report
    # the info on the final segment to the user.
    user_IP_address += '.'
    if user_IP_address[0] =='.':
        seg_count -= 1

# Tells the user how many segments there are in the add.
print("This IP address has {} segments.".format(seg_count))

# resets the seg_count so the FOR statement can report properly.
seg_count = 0

for char in user_IP_address:
    if char in '0123456789':
        new_string += char
    #This elif will stop adding characters for the segment, when it encounters a
    # period. 
    elif char == '.':
        seg_count += 1
        print("Segment {0} has {1} digits.".format(seg_count, len(new_string)))
        #reset new_string to an empty string for the next iteration.
        new_string = ''
