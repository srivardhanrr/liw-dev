import resend

resend.api_key = 're_accidBns_25oWZAftHrhd7K24SnccKycd'

params: resend.Emails.SendParams = {
    "from": "Acme <onboarding@resend.dev>",
    "to": ["electrochaser25@gmail.com"],
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
