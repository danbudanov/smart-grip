
//const int grip = 8;
const int trigPin = 9;
const int echoPin = 10;
const int threshold = 5;
const int TouchPin = 4;

long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
pinMode(trigPin, OUTPUT);

pinMode(TouchPin, INPUT);

//pinMode(grip, OUTPUT);

pinMode(echoPin, INPUT);

pinMode(LED_BUILTIN, OUTPUT);

Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin,LOW);

duration = pulseIn(echoPin, HIGH);

distance = duration*0.034/2;

int sensorValue = digitalRead(TouchPin);
Serial.print("Touch: ");
Serial.println(sensorValue);

Serial.print("Distance: ");
Serial.println(distance);
delay(100);

if ((distance < threshold) & (sensorValue == 1)) {
  digitalWrite(LED_BUILTIN, HIGH);
 // digitalWrite(grip, HIGH);
} else {
  digitalWrite(LED_BUILTIN, LOW);
 // digitalWrite(grip, LOW);
}


}

