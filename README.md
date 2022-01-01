<!-- Title -->
<span align = "center">

# ArduRaspiAuth
  
</span>
<!-- End of Title -->

Authentication method to validate arduino board identity in UART protocol communication between Arduino and Raspberry Pi.

When you connect Arduino board with Raspberry Pi via UART communication, you can get location of Arduino port by typing `ls /dev/tty*` in terminal. But, if you connect more than one Arduino connected to Raspberry Pi,  you will get confused. The terminal only show the location. You can't know well where is Arduino A location or Arduino B location.

This repository give you a technique to differentiate the Arduino board by giving an identity to the Arduino board. The Arduino Board save this identity on its memory. And when Raspberry Pi call to get Arduino board identity, Arduino board will give its identity via UART communication.

## How To Use
You can go to `src/ArduRaspiAuth.py` and copy the code. After copying the code, save in the file named `ArduRaspiAuth.py` in your workspace.

Or

You can clone this repository and move/copy `ArduRaspiAuth.py` to workspace.
```
git clone https://github.com/SuryaAssistant/ArduRaspiAuth
```

The Arduino code is available in `example.ino`.
