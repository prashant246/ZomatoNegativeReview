'''
In this file we have taken some words which generally shows negative review and using this data we can classify sentiment of the user for the food
'''

words = ["stale","nasty","rancid","sour", "inedible", "unpalatable", "tasteless", "bland", "insipid", "bad", "acrid", "icky", "off", "overpowering", "pungent", "sickly",
         "spoiled","stewed", "tainted", "unappetizing", "uneatable", "unsavoury", "watery"]

def checkNegativity(text) :
    isNegative = False
    text = text.split()
    negative = ""
    for each in text :
        if each in words :
            negative += (each + " ")
            isNegative = True
    #print negative
    return isNegative, negative

