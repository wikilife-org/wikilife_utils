# coding=utf-8

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class SinpleMailSender(object):

    _smtp_host = None

    def __init__(self, smtp_host):
        """
        smtp_host: String, e.g: 'localhost'
        """
        self._smtp_host = smtp_host

    def send_text_mail(self, frm, to, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = frm
        msg['To'] = to[0] #TODO review this
        s = smtplib.SMTP(self._smtp_host)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

    def send_html_mail(self, frm, to, subject, text_body, html_body):
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = frm
        msg['To'] = to[0] #TODO review this

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text_body, 'plain')
        part2 = MIMEText(html_body, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        s = smtplib.SMTP(self._smtp_host)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
