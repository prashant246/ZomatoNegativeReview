'''
we have use this file to generate the body of the mail which is to be sent to user
'''

def body(words, user_name, user_url) :
    text = "Hi, You have got negative review for your restaurant from " + user_name + "(" + user_url + "). " + "Sentiments are : "
    for each in words:
        text = text + each + " "
    return text
