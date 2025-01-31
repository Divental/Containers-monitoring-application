import LoggerPack.log_container as lc
from TelegramBotAlertsPack import alerts

def main_block():
    lc.logger.info("The app has started!")
    alerts.start_telegram_bot()
    return 0

if __name__ == "__main__":
    ending_code = main_block()
    if ending_code == 0:
        lc.logger.info("The app is complete!")



