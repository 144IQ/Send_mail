import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

EMAIL, PASSWORD = ('example@gmx.us', 'password')
CONTENT = "送るメッセージ"

message = MIMEText(CONTENT)
message["Subject"] = "題名"
message["From"] = formataddr(("自分の名前", EMAIL))
message["To"] = '送信先のメールアドレス'

with smtplib.SMTP('smtp.gmx.com', 587) as smtpobj:
    smtpobj.starttls()
    smtpobj.login(EMAIL, PASSWORD)
    smtpobj.send_message(message)