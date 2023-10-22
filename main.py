from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

subject = 'Test Email'
html_content = '<html><body><h1>This is my first transactional email </h1></body></html>'
sender = {"name":"Anshul Gowda","email":"anshuljg07@gmail.com"}
to = [{"email":"indybomber@gmail.com","name":"Rick Shumer"}]
cc = [{"email": "cc@example.com", "name": "CC Recipient Name"}]
bcc = [{"email": "bcc@example.com", "name": "BCC Recipient Name"}]
reply_to = {"email":"anshuljg07@gmail.com","name":"Anshul Gowda"}
headers = {"Some-Custom-Name":"unique-id-1234"}
params = {"parameter":"My param value","subject":"New Subject"}

send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)

except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
