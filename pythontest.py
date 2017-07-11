class Word(object):
    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

lexicon = {
"house" :   ["N", "sg"],
"to be" :   ["V"],
"red"   :   ["ADJ", "color"]
}

def merge(a, *args):
    sequence = ""
    if args:
        sequence += a
        for word in args:
            sequence += " " + word
        return sequence
    else:
        return a

def get_category(word):
    pos = lexicon.get(word)[0]
    result = "This word is a "
    if pos == "V":
        return result + "verb"
    elif pos == "N":
        return result + "noun"
    elif pos == "ADJ":
        return result + "adjective"
    else:
        return "This word belongs to an unrecognized grammatical category"


#print(merge("house", "to be", "red"))

print(get_category("to be"))
