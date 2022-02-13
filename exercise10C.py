# PART 3: hiding the PIN
# import getpass
import getpass

pin = 1011

attempt = 0

while attempt < 3:
    supplied_pin = int(getpass.getpass("Enter your PIN: "))
    if supplied_pin == pin:
        print('correct pin')
        break
    else:
        attempt += 1
        print('wrong pin')
        print('attempt:', attempt)

if attempt == 3:
    print('too many attempts, account blocked')