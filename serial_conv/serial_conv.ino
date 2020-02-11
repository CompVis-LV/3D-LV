#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor
int angle = 0;
int newAngle;
int steps;
int a;
int deg;
int rev;
String inString = "";    // string to hold input
int inChar;
// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  myStepper.setSpeed(30);
  // Open serial communications and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // send an intro:
  Serial.println("\n\nString toInt():");
  Serial.println();
}

void loop() {
  // Read serial input:
  while (Serial.available() > 0) {
    inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string, then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
    }
  }
  if (inString != "") {
    if (inChar == '\n') {
      newAngle = inString.toInt();
      Serial.println (newAngle);

      a = newAngle - angle;
      //deg = ((a + 180) % 360) - 180;
      rev = ((a + 100) % 200) - 100;
      //rev = deg / 1.8;
      angle = newAngle;

      // step one revolution  in one direction:
      Serial.println("Rotating");
      Serial.println(rev);
      myStepper.step(rev);
      delay(500);

      Serial.println(1);
      delay(50);
      // clear the string for new input:
      inString = "";
    }
  }
}
