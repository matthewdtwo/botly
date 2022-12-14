#include <Arduino.h>
#include "../lib/Encoder.cpp"

#define BAUD_RATE 115200

int fullRotation = 475;
int wheelDiameterCM = 7;
int piDigits = 3.1416;

int motor1pinA = 3; // motor 1 encoder A output
int motor1pinB = 4; // motor 1 encoder B output

int motor2pinA = 2; // motor 2 encoder A output
int motor2pinB = 5; // motor 2 encoder B output

Encoder motor1Encoder = Encoder(motor1pinA, motor1pinB);
Encoder motor2Encoder = Encoder(motor2pinA, motor2pinB);


void interrupt0() {
  motor1Encoder.interruptIncrementor();
  Serial.print("left: ");
  Serial.println(motor1Encoder.getCounter());
}

void interrupt1() {
  motor2Encoder.interruptIncrementor();
  Serial.print("right: ");
  Serial.println(motor2Encoder.getCounter());
}

// initial setup - runs once on startup.
void setup() {
  
  Serial.begin(BAUD_RATE);

  attachInterrupt(digitalPinToInterrupt(motor1pinA), interrupt0, HIGH);
  attachInterrupt(digitalPinToInterrupt(motor2pinA), interrupt1, HIGH);
  
}


// main program loop
void loop() {
}