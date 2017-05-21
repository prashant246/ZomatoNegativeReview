This script will get the negative review for "Barbeque Nation Sector 16 Noida" based on the following two points:

1. If rating is less than 3.0
2. If the review text contains some pre defined words which shows the negative review about food.


There are five python file in this project.
1. Script.py
2. DatabaseConnection.py
3. NegativeReviewChecker.py
4. Key.py
5. Email_body.py

-------------------------------------------------------------------------------------------------------------------------

Script.py :::::

This is the main file which contains the main function and contains two functions, namely, 
ZomatoAPI (This function will fetch the user review from the Zomato and will classify the review accordingly
and if the review is found to be negative then this will store that data in the database and will send a mail
 to the user containing the details about user and review) and SendGridAPI( this function uses SendGrid API 
to send the mail to the user).

-------------------------------------------------------------------------------------------------------------------------


DatabaseConnection.py :::::

This file contains the functionality of the databases
 
The database structure is as follows:
review_id : int
rating : char
rating_text : char
sentiment : char
user : char
user_id : char

This file contains three function namely, insert(), find() and delete() which works as refer by their names.

------------------------------------------------------------------------------------------------------------------------

NegativeReviewChecker.py :::::

This file is use to check the review_text contains any negative word or not. There is a dictionary of words which 
contains some words which shows some negativity. And if the text contains any of these words then the review is
classified as negative review


------------------------------------------------------------------------------------------------------------------------

Key.py :::::

This file contain the API keys for Sendgrid and Zomato

------------------------------------------------------------------------------------------------------------------------

Email_body.py :::::

This file can use to generated the Email body as required.


-------------------------------------------------------------------------------------------------------------------------





HOW TO RUN THE SCRIPT TO RECEIVE NEGATIVE REVIEWS::::

To run the script, just run the Script.py file.

P.S. kindly use your own API keys for Zomato and SendGrid