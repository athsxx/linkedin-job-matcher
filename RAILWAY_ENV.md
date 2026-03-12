# Railway – Environment variables

Set these in **Railway Dashboard → Your Service → Variables**.

| Variable | Value / Note |
|---------|------------------|
| `FLASK_SECRET_KEY` | Generate: `python3 -c "import secrets; print(secrets.token_hex(32))"` |
| `GOOGLE_AI_API_KEY` | Your Google AI Studio API key |
| `SENDGRID_API_KEY` | Your SendGrid API key |
| `SENDGRID_FROM_EMAIL` | Verified sender email (e.g. your Gmail) |
| `USE_EXTERNAL_FEEDS` | `true` |
| `USE_OLLAMA_FOR_RESUME` | `false` (Ollama is local; keep false on Railway) |
| `OLLAMA_BASE_URL` | `http://localhost:11434` (optional) |
| `OLLAMA_MODEL` | `llama3.2` (optional) |
| `OLLAMA_TIMEOUT` | `120` (optional) |

`PORT` is set by Railway automatically. Start command is in `railway.toml` (gunicorn).
