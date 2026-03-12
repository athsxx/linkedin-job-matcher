#!/usr/bin/env python3
"""
Test SendGrid email sending. Run from project root with venv activated.
Usage: python test_sendgrid.py [to_email]
  If to_email omitted, uses SENDGRID_FROM_EMAIL (send to yourself).
"""
import os
import sys
import base64
from dotenv import load_dotenv

load_dotenv()

def main():
    to_email = (sys.argv[1:] and sys.argv[1]) or os.getenv('SENDGRID_FROM_EMAIL')
    api_key = os.getenv('SENDGRID_API_KEY')
    from_email = os.getenv('SENDGRID_FROM_EMAIL')

    print('Config:')
    print('  SENDGRID_API_KEY:', 'SET' if api_key else 'MISSING')
    print('  SENDGRID_FROM_EMAIL:', from_email or 'MISSING')
    print('  To:', to_email or 'MISSING')
    if not all([api_key, from_email, to_email]):
        print('ERROR: Set .env and optionally pass to_email')
        sys.exit(1)

    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType
    except ImportError as e:
        print('ERROR: SendGrid not installed:', e)
        sys.exit(1)

    subject = "Test: Resume and job listings"
    html_body = """
    <h2>Test email from AI Resume Matcher</h2>
    <p><strong>Job link:</strong> <a href="https://example.com/job">Example Job</a></p>
    <h3>Job description</h3>
    <div style="white-space: pre-wrap; background: #f5f5f5; padding: 12px;">Test job description here.</div>
    <p>The generated resume is attached as <strong>resume.html</strong>.</p>
    """
    resume_html = "<html><body><h1>Test Resume</h1><p>If you see this, attachment works.</p></body></html>"

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_body
    )
    encoded = base64.b64encode(resume_html.encode('utf-8')).decode()
    attachment = Attachment(FileContent(encoded), FileName("resume.html"), FileType("text/html"))
    message.attachment = attachment

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print('SendGrid response status:', response.status_code)
        if response.status_code in (200, 202):
            print('SUCCESS: Email sent. Check inbox (and spam) for', to_email)
        else:
            print('Response body:', response.body)
    except Exception as e:
        print('ERROR sending email:', e)
        if hasattr(e, 'body'):
            print('Detail:', e.body)
        sys.exit(1)

if __name__ == '__main__':
    main()
