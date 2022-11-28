#include <Arduino.h>

class Encoder {
    private:
        int pinA;
        int pinB;

        int statusPinA = digitalRead(pinA);
        int statusPinB = digitalRead(pinB);

        int counter = 0;
        
        void readEncoders() {
            statusPinA = digitalRead(pinA);
            statusPinB = digitalRead(pinB);
        }


    public:
        Encoder(int encA, int encB) {
            pinA = encA;
            pinB = encB;

            pinMode(pinA, INPUT);
            pinMode(pinB, INPUT);
        }

        void interruptIncrementor() {
            readEncoders();

            if(statusPinA == statusPinB) {
                counter--;
            } else {
                counter++;
            }
        }

        int getCounter() {
            return counter;
        }

};
