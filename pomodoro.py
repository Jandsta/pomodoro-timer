import time

while True:
    work_minutes = int(input("Enter work minutes: "))
    if work_minutes > 0:
        break
    print("please enter a positive number!")

while True:
    break_minutes = int(input("Enter break minutes: "))
    if break_minutes > 0:
        break
    print("Please enter a positive number!")

print("Work:", work_minutes, "min, Break:", break_minutes, "min")

#convert minutes to seconds
remaining_seconds_a = work_minutes * 60
remaining_seconds_b = break_minutes * 60

#countdown loop for work
for remaining in range(remaining_seconds_a, -1, -1):
    minutes_a = remaining // 60
    seconds_a = remaining % 60

    print(f"\rWork remaining:{minutes_a:02d}:{seconds_a:02d}", end=" ")
    time.sleep(1)

print("\nWork period done! Take a break.")

#countdown loop for break
for remaining in range(remaining_seconds_b, -1, -1):
    minutes_b = remaining // 60
    seconds_b  = remaining % 60

    print(f"\rBreak remaining:{minutes_b:02d}:{seconds_b:02d}", end=" ")
    time.sleep(1)

print("\nBreak done")
