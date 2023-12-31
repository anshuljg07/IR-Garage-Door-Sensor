from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import datetime
import digitalio
import board

#using Brevo email service

def sendEmail():
    ct = datetime.datetime.now()

    subject = 'ALERT! Signal Lost'
    html_content = f'<html><body><h1> No longer receiving Signal through IR to receiver!</h1><p>Current Timestamp: {ct}</p></body></html>'
    sender = {"name": "Anshul Gowda", "email": "anshuljg07@gmail.com"}
    to = [{"email": "indybomber@gmail.com", "name": "Rick Shumer"}]
    cc = [{"email": "cc@example.com", "name": "CC Recipient Name"}]
    bcc = [{"email": "bcc@example.com", "name": "BCC Recipient Name"}]
    reply_to = {"email": "anshuljg07@gmail.com", "name": "Anshul Gowda"}
    headers = {"Some-Custom-Name": "unique-id-1234"}
    params = {"parameter": "My param value", "subject": "New Subject"}

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers,
                                                   html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '{Enter API KEY}'
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

waveDetected = digitalio.DigitalInOut(board.D14)
waveDetected.direction = digitalio.Direction.INPUT
sent = False

while True:
    if waveDetected.value == 0:
        if sent == False:
            print('No Signal Detected. Email Sent!!!')
            sendEmail()
            sent = True
    else:
        sent = False
