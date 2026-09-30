#include <LiquidCrystal.h>
#include <Servo.h>


LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // sets LCD


const int trigPin = 9; // sets pins for ultrasnonic sensor. 
const int echoPin = 10; // sets the pins of the ultrasonic sensor


const int servoPin = 8; // sets the pin for the servo
Servo myServo;


const int redPin = A0;
const int greenPin = A1; // sets the pins for the RGB
const int bluePin = A2;


const int buzzerPin = 6; // sets the pin for the buzzer


int angle = 0;
int direction = 1; // sets the direction values for the radar

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  pinMode(trigPin, OUTPUT); // the trigpin will output noise
  pinMode(echoPin, INPUT); // the echopin will listen for noise

  pinMode(buzzerPin, OUTPUT); // 

  lcd.begin(16, 2);
  lcd.print("Radar Ready");
  delay(1000);
  lcd.clear();

  myServo.attach(servoPin);

}

void setColor(int r, int g, int b) {
  analogWrite(redPin, r);
  analogWrite(greenPin, g);
  analogWrite(bluePin, b);
}

long getDistance() {
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;
  return distance;
}

void loop() {

  long dist = getDistance();

  myServo.write(angle); // moves the servo
  angle += direction;

  if (angle >= 180 || angle <= 0) {
    direction = -direction;
  }

  lcd.setCursor(0, 0); // for the LCD screen, prints the current distance
  lcd.print("Distance:      ");
  lcd.setCursor(0, 1);
  lcd.print(dist);
  lcd.print(" cm        ");

  if (dist >= 25) { // if the distance is greater than or equal to 25 cm
    setColor(0, 255, 0);
    noTone(buzzerPin);
  }
  else if (dist >= 20) { // if the distance is greater than or equal to 20 cm
    setColor(255, 165, 0);
    tone(buzzerPin, 800);
    delay(400);
    noTone(buzzerPin);
  }
  else if (dist >= 10) { // if the distance is greater than or equal to 10 cm
    setColor(255, 0, 0);
    tone(buzzerPin, 1000);
    delay(200);
    noTone(buzzerPin);
  }
  else { // if the distance is less than 10 cm
    setColor(255, 0, 0);
    tone(buzzerPin, 1200);
    delay(100);
    noTone(buzzerPin);
  }

  delay(15); // for a clean signal, waits 15 milliseconds
}

