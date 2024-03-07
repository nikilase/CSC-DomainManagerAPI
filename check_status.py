from time import sleep

from api import get_zone_edit_status

if __name__ == "__main__":
	print("Please enter your edit id:")
	edit_id = input()
	propagated = False
	i = 0
	while not propagated:
		status = get_zone_edit_status(edit_id)
		if status is None:
			print("Exiting Program!")
			exit(2)
		elif status == "COMPLETED":
			propagated = True
			print("COMPLETED!")
			exit(0)
		else:
			if i > 30:
				i = 0
				print(".")
			else:
				print(".", end="")
		sleep(1)
