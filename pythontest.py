def merge(a, *args):
    sequence = ""
    if args:
        sequence += a 
        for word in args:
            sequence += " " + word
        return sequence
    else:
        return a

print(merge("hey", "you", "there"))
