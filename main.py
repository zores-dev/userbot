import os
import asyncio
from pyrogram import Client, filters
import uvicorn
from fastapi import FastAPI

# --- ИНИЦИАЛИЗАЦИЯ ВЕБ-СЕРВЕРА (для аптайма Koyeb) ---
app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "ok", "bot": "running"}

async def run_web_server():
    port = int(os.environ.get("PORT", 8000))
    config = uvicorn.Config(app, host="0.0.0.0", port=port, log_level="error")
    server = uvicorn.Server(config)
    await server.serve()

# --- ИНИЦИАЛИЗАЦИЯ ЮЗЕРБОТА ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
SESSION_STRING = os.environ.get("SESSION_STRING", "")

userbot = Client(
    "my_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

@userbot.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping_handler(client, message):
    await message.edit_text("🏓 **Pong!** Юзербот работает на Koyeb.")

# --- ТОЧКА ВХОДА ---
async def main():
    # Запускаем веб-сервер и юзербота параллельно
    await asyncio.gather(
        run_web_server(),
        userbot.start()
    )
    # Удерживаем процесс активным
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
