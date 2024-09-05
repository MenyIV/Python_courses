from Coffe_machine_data import kafe


import time

logo = kafe
rows = logo.splitlines(0)
print (rows)
for row in rows:
    print(row)
    time.sleep(0.1)
