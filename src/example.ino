/*---------------------------------------------
* Example code of ArduRaspiAuth
* Authentication method to validate Arduno board identity when connected
* to Raspberry Pi via UART communication
*
* Further information : https://github.com/SuryaAssistant/ArduRaspiAuth
*/


//---------------------------------------------
// Arduin Board Credential
//---------------------------------------------
String boardIdentity = "exampleofidentity";
String checkIDCode = "get_id"
String inputCommand;

int baudrate = 9600     // same as Raspberry Pi baudrate

void setup()
{
    Serial.begin(baudrate);
}

void loop()
{
    // Read serial message from Raspberry Pi
    if (Serial.available())
    {
        inputCommand = Serial.readStringUntil('\n');
        processUART(inputCommand);
    }

    // Your code here

}

void processUART(String inputCommand)
{
    if (inputCommand == "get_id")
    {
        Serial.println(boardIdentity);
        Serial.flush();
    }
}
