# Bulk-Emails-Python
Send bulk emails through Python Script

In the excel file, under the Emails tab - Enter the email address of people you want to send email.

Installing Pandas on Mac OSX or Windows cmd
pip install pandas  # Run this code on Terminal or Command Prompt

In line 4: Add the path of excel file

In line 8: Enter the SMTP for the account that is being used. Enter the port number for it as well.

Default: For Hotmail:  SMTP = smtp-mail.outlook.com and Port Number: 587

In line 10: Enter the email id and password for the account you wish to send email from.
In line 11: Enter the message you wish to send to the client.
In line 12: Enter the subject field
In line 16: Enter the same email id again.

Make sure to print the excel file to check if file is read properly 


# Error : SMTPAuthenticationError when sending mail using gmail and python 
Answer: Try logging in through your browser and if you are able to access your account come back and try your code again. Just make sure that you have typed your username and password correct

EDIT: Google blocks sign-in attempts from apps which do not use modern security standards (mentioned on their support page). You can however, turn on/off this safety feature by going to the link below:

Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps


