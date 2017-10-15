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
int inByte = 0;

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
  inByte = Serial.read();
  
  // put your main code here, to run repeatedly:
  if (inByte == 100) {
  
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

}
if (inByte == 116) {
 
 int sensorValue = digitalRead(TouchPin);
  //Serial.print("Touch: ");
  Serial.println(sensorValue);
  delay(1000);
 // Serial.write(sensorValue);
}

if (inByte == 103) {
  angle = Serial.read();
  myServo.write(angle);
  delay(15);
}
if (inByte == 117) {
  myServo.write(0);
  delay(15);
}
}

//void establishContact() {

  
//}

