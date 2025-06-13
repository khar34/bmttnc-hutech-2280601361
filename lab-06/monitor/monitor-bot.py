import psutil
import logging
import time
import asyncio
import os
from telegram import Bot
from dotenv import load_dotenv

# Load bien moi truong tu .env tai vi khong ai di hardcode may cai api ca
load_dotenv()
# API truy cap cua Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
# chat id
CHAT_ID = os.getenv("CHAT_ID")

print(f"BOT_TOKEN: {BOT_TOKEN}")
print(f"CHAT_ID: {CHAT_ID}")
# Cau hinh logging
logging.basicConfig(
    level=logging.INFO,
    filename="system_monitor_bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()


# Ham ghi log
def log_info(category, message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")


# Ham gui tin nhan qua Telegram
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)


# Ham giam sat CPU va bo nho
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    log_info("CPU", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")

    # Gui thong bao qua telegram
    message = f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_info.percent}%"
    asyncio.run(send_telegram_message(message))


# Ham thuc hien giam sat toan bo he thong
def monitor_system():
    log_info("System Monitor", "Starting system monitoring...")

    while True:
        monitor_cpu_memory()
        log_info("System monitor", "-------------------------------------------------")
        time.sleep(60)


if __name__ == "__main__":
    monitor_system()
