#!/bin/bash
# Run the AI Resume Matcher app with SendGrid email working (SSL fix)
cd "$(dirname "$0")"

# Activate venv
source venv/bin/activate

# Fix SSL so SendGrid can send mail (needed on some macOS/Windows)
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
export REQUESTS_CA_BUNDLE="$SSL_CERT_FILE"

echo "Starting app at http://localhost:5003"
echo "SendGrid will send resumes to the email you use to log in."
python app.py
