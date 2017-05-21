'''
this is the main script in which we have queried the review from the zomato API and classified the reviews according to the rating and sentiment.
'''

import requests
import sendgrid
from sendgrid.helpers.mail import *
from Email_body import body
from Key import *
from NegativeReviewChecker import checkNegativity
from DatabaseConnection import *

def SendGridAPI(SENDGRID_API_KEY, sender, receiver, subject, content):
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    from_email = Email(sender)
    to_email = Email(receiver)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)

def ZomatoAPI(ZomatoKEy, SendGridKey, Sender, Receiver):
    res_id = 310719
    url = "https://developers.zomato.com/api/v2.1/reviews?res_id=" + str(res_id)
    header = {"user_key" : ZomatoKEy}
    response = requests.get(url, headers = header)
    data = response.json()
    jsonData = data["user_reviews"]

    for each in jsonData:
        temp = each["review"]
        rating = temp["rating"]
        id = temp["id"]
        user = temp["user"]
        user_name = user["name"]
        profile_url = user["profile_url"]
        #print "f"
        if find(id) :
            #print "df"
            review_text = temp["review_text"]
            isNegative, words = checkNegativity(review_text)
            if isNegative or rating <= 3.0:
                if len(words) < 2:
                    words = review_text
                rating_text = temp["rating_text"]
                content = Content("text/plain", body(words, user_name, profile_url))
                subject = "Negative Review for Restaurant id " + str(res_id) + ": " + rating_text + " " + str(rating)
                insert(id, rating_text, words, user_name, profile_url, rating)
                #print "in lala"
                SendGridAPI(SendGridKey, Sender, Receiver, subject, content)


if __name__ == '__main__':
    ZomatoKey = getZomatoKey()
    SendGridKey = getSendGridKey()
    Sender = getSender()
    Receiver = getReceiver()
    ZomatoAPI(ZomatoKey, SendGridKey, Sender, Receiver)

