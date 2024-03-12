from time import sleep

from app.api import get_zone_edit_status


def wait_status_ok(edit_id: str) -> bool:
    i = 1
    while True:
        status = get_zone_edit_status(edit_id)

        if status is None:
            print("No Status Found!")
            return False
        elif status == "PROPAGATING" or status == "PROCESSING":
            if i >= 30:
                i = 0
                print(".")
            else:
                print(".", end="", flush=True)
            i += 1
        elif status == "COMPLETED":
            return True
        else:
            print(f"GOT STATUS: {status}")
            return False
        sleep(1)


def main():
    print("Please enter your edit id:")
    edit_id = input()
    if wait_status_ok(edit_id):
        print("Status Complete!")

