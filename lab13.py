"""
Welcome AT
aim : ascii values and unicode charset
pre-requsite :
"""

#lets find the ascii code for Latin capital 'A'
# we are finding code from char
print(ord('A'))
# Now char from number
print(chr(65))

# outside ascii
print(ord('A'))   # ASCII range
print(ord('€'))   # outside ASCII

# encode decode
text = "Hello"
print(text)
print(text.encode('utf-7'))
print(text.encode('utf-8'))
print(text.encode('utf-16'))
print(text.encode('utf-32'))

#lets encode an text and then decode it
text = "Welcome AT"
print(f" text is : {text}")
new_text = text.encode('utf-16')
print(f" text in utf-16 is : {new_text}")
# after decode
print(f" decoded code is : {new_text.decode('utf-16')}")

# WE can perform various tasks via knowing that
"""
 ord stands for  “ordinal” , ordindal mean?
In math and computer science:
An ordinal number represents the < position or order of something in a sequence.>
So:
ord('A') → gives the position of 'A' in the Unicode table
"""

"""
More to learn !

enocoding / decoding

"""