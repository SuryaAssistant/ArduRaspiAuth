# import dependency(s)
import time
import serial

uart_message = "get_id"

# class to detect arduino identity
def arduino_get_id(port_number, tty_name, uart_baudrate):
    with serial.Serial("/dev/{}{}".format(tty_name, port_number), uart_baudrate, timeout=1) as checked_port:
        
        # wait serial com to open
        time.sleep(0.25)
        print("Check Arduino in {}".format(checked_port.port))

        # if serial com is open, send message to get the arduino id
        if checked_port.isOpen():
            print("Arduino in {} connected".format(checked_port.port))
            print("Check Arduino in {} identity".format(checked_port.port))
            check_message = ("{}\n".format(uart_message))
            
            time.sleep(3)

            # send message to Arduino
            checked_port.flushInput()
            checked_port.write(check_message.encode('utf-8'))

            # wait for Arduino's response
            while checked_port.inWaiting()==0: pass

            if checked_port.inWaiting():
                # get id from Arduio
                answer = checked_port.readline()
                decode_answer = answer.decode('utf-8').rstrip()
                checked_port.flushInput()
            
        else:
            print("{} is not connected".format(checked_port.port))

    # send Arduino identity to main program
    return decode_answer

if __name__ == "__main__":
    print("Detect Arduino connection\n")
    print("Example : \n")

    print("from ArduRaspiAuth import *")
    print("Arduino_ID = arduino_get_id({port_number}, USB, 9600)")

    print("\nor\n")
    
    print("from ArduRaspiAuth import *")
    print("Arduino_ID = arduino_get_id({port_number}, ACM, 9600)")