import resend

resend.api_key = 're_accidBns_25oWZAftHrhd7K24SnccKycd'

params: resend.Emails.SendParams = {
    "from": "Leadership Innovation World <alerts@marksmanclub.in>",
    "to": ["electrochaser26@gmail.com"],
    "subject": "hello world",
    "html": "<strong>it works!</strong>",
}

email = resend.Emails.send(params)
print(email)
