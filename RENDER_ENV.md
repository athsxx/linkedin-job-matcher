# Environment variables for Render

Set these in **Render Dashboard → Your Service → Environment** (or in the Blueprint envVars). GitHub cannot accept pushes that contain secrets, so use Render's UI.

| Key | Example / Note |
|-----|----------------|
| `FLASK_SECRET_KEY` | Use "Generate value" in Render or a long random string |
| `GOOGLE_AI_API_KEY` | Your Google AI Studio API key |
| `SENDGRID_API_KEY` | Your SendGrid API key |
| `SENDGRID_FROM_EMAIL` | Verified sender email (e.g. your Gmail) |
| `USE_EXTERNAL_FEEDS` | `true` |
| `USE_OLLAMA_FOR_RESUME` | `false` (Ollama is local; use `true` only if you add an Ollama server) |
| `OLLAMA_BASE_URL` | `http://localhost:11434` (ignored if USE_OLLAMA_FOR_RESUME=false) |
| `OLLAMA_MODEL` | `llama3.2` |
| `OLLAMA_TIMEOUT` | `120` |
| `PORT` | Set by Render automatically |

Copy the names and your values from your local `.env` into Render's Environment tab.
