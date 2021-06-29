import yagmail


def send_email(username: str, password: str, to: str, image, body: str, subject: str, ):
    yag = yagmail.SMTP(username, password)
    contents = body
    yag.send(to=to,
             subject=subject,
             contents=contents,
             attachments=image
             )
