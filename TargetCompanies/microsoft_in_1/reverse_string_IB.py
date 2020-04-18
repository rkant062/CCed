def reverse_string(s):
    s1 = ""
    words = s.split(' ')
    s1 = ' '.join(reversed(words))
    print(s1)

reverse_string("hello is my name")
