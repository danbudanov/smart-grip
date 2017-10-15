#include <Servo.h>

Servo myServo;
int angle;

//const int grip = 8;
const int trigPin = 9;
const int echoPin = 10;
const int threshold = 5;
const int TouchPin = 4;

long duration;
int distance;
char inByte = 0;

void setup() {
    // put your setup code here, to run once:
    myServo.attach(11);

    pinMode(trigPin, OUTPUT);

    pinMode(TouchPin, INPUT);

    //pinMode(grip, OUTPUT);

    pinMode(echoPin, INPUT);

    pinMode(LED_BUILTIN, OUTPUT);

    Serial.begin(9600);
    //establishContact();
}

void loop() {
    if (Serial.available()) {
        inByte = Serial.read();

        switch (inByte) {
            case(100) : { // 100

                digitalWrite(trigPin, LOW);
                delayMicroseconds(2);

                digitalWrite(trigPin, HIGH);
                delayMicroseconds(10);
                digitalWrite(trigPin,LOW);

                duration = pulseIn(echoPin, HIGH);

                distance = duration*0.034/2;

                //Serial.print("Distance: ");
                Serial.println(distance);
                // Serial.write(distance);
                delay(1000);

                if (distance < threshold) {
                    digitalWrite(LED_BUILTIN, HIGH);
                    //    digitalWrite(grip, HIGH);
                }  else {
                    digitalWrite(LED_BUILTIN, LOW);
                    //   digitalWrite(grip, LOW);l
                }
                break;

            }
            case('t') : { // 116

                int sensorValue = digitalRead(TouchPin);
                //Serial.print("Touch: ");
                Serial.println(sensorValue);
                delay(1000);
                // Serial.write(sensorValue);
                break;
            }

            case('g') : { // 103
                angle = Serial.read();
                myServo.write(angle);
                delay(15);
                break;
            }
            case('u') : {// 117
                myServo.write(0);
                delay(15);
                break;
            }
        }
    }
}
