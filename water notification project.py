import time
from plyer import notification

def notify_water_reminder():
    notification.notify(
        title='Time to Drink Water',
        message='Stay hydrated! Drink a glass of water.',
        timeout=10
    )

if __name__ == "__main__":
    while True:
        notify_water_reminder()
        time.sleep(60 * 60)  # Notify every hour
