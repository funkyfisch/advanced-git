from time import sleep

def Sleep(duration):
    print(f"Sleeping for {duration}")
    sleep(duration)


if __name__ == "__main__":
    duration = 5
    Sleep(duration)