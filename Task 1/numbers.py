'''
Write a function that takes two arguments, 145 and 'o'
,and uses the `format` function to return a formatted string.
Print the result. Try to identify the representation used
'''
def format(num,char):
    return "{} {}".format(num,char)

print(format(145,'o'))

#When you run this code, it will output:
#  145 o