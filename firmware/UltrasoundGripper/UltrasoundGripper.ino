
const int grip = 8;
const int trigPin = 9;
const int echoPin = 10;
const int threshold = 5;
const int buttonPin = 2;

int buttonState = 0;

long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
pinMode(trigPin, OUTPUT);

pinMode(buttonPin, INPUT);

pinMode(grip, OUTPUT);

pinMode(echoPin, INPUT);

pinMode(LED_BUILTIN, OUTPUT);

Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
buttonState = digitalRead(buttonPin);

if (buttonState == HIGH){
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin,LOW);

duration = pulseIn(echoPin, HIGH);

distance = duration*0.034/2;

Serial.print("Distance: ");
Serial.println(distance);
}

if (distance < threshold) {
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(grip, HIGH);
} else {
  digitalWrite(LED_BUILTIN, LOW);
  digitalWrite(grip, LOW);
}


}

