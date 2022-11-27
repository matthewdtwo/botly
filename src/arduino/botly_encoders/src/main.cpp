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

Encoder leftMotorEncoder = Encoder(motor1pinA, motor1pinB);
Encoder rightMotorEncoder = Encoder(motor2pinA, motor2pinB);


void interrupt0() {
  leftMotorEncoder.interruptIncrementor();
  // Serial.print("left: ");
  // Serial.println(leftMotorEncoder.getCounter());
}

void interrupt1() {
  rightMotorEncoder.interruptIncrementor();
  // Serial.print("right: ");
  // Serial.println(rightMotorEncoder.getCounter());
}

void printEncoders() {
  Serial.print("left: ");
  Serial.println(leftMotorEncoder.getCounter());

  Serial.print("right: ");
  Serial.println(rightMotorEncoder.getCounter());
}

// initial setup - runs once on startup.
void setup() {
  
  Serial.begin(BAUD_RATE);

  attachInterrupt(digitalPinToInterrupt(motor1pinA), interrupt0, HIGH);
  attachInterrupt(digitalPinToInterrupt(motor2pinA), interrupt1, HIGH);
  
}


// main program loop
void loop() {
  delay(10);
  printEncoders();
}