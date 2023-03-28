# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random


def Input():
    text = input("Enter text that you want to send: ")
    if len(text) < 3:
        r = text[::-1]
        print("Message for receiver: ", r)
        return r
    else:
        add = text[0]
        r = text[1:]
        r = r + add
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for i in range(3):
            random_chars = random.choice(chars)
            r = random_chars + r + random_chars
        print("Message for receiver: ", r)
        return r


def Output(text):
    if (len(text) < 3):
           o = text[::-1]
           print("Message from sender: ", o)
           return o
    else:
        o = text[3:-3]
        o = o[-1] + o[:-1]
        print("Message from sender: ", o)
        return 0


result = Input()
Output(result)
