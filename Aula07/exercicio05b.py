import time

for minuto in range(9, -1, -1):
    for segundo in range(59, -1, -1):
        print("{:02d}:{:02d}".format(minuto, segundo))
        time.sleep(1)