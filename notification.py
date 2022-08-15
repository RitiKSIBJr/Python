import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Alert",
            message = "Take a break!!",
            timeout = 10
        )

        #Stops the program for an hour(3600 seconds)
        time.sleep(3600)