#include <ESP32Servo.h>
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
#include <Wire.h>
#define in1 19
#define in2 21 
#define in3 22 
#define in4 23 
#define enA 32 
#define enB 33 
char heading='N';
char key[]={'N','E','S','W'};
int val[]={1,2,3,4};
void setup() {
  SerialBT.begin("Esp32-BT");
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enA,OUTPUT);
  pinMode(enB,OUTPUT);
  
}
int getValue(char k) {
  for (int i = 0; i < 4; i++) {
    if (key[i] == k) {
      return val[i];
    }
  }
}
void forward()
{
  analogWrite(enA,155);
  analogWrite(enB,155);
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  delay(400);
  stop();
}
void left(int n)
{
  analogWrite(enA,155);
  analogWrite(enB,155);
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  delay(300*n);
  stop();
}
void right(int n)
{
  analogWrite(enA,155);
  analogWrite(enB,155);
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  delay(300*n);
  stop();
}
void stop()
{
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  delay(75);
}
void rotate(char a)
{
  if(a==heading)
  return;
  else
  {
    int p=getValue(a)-getValue(heading);
    if(p==3)
    left(1);
    else if(p==-3)
    right(1);
    else if(p==2 || p==-2)
    right(2);
    else if(p==1)
    right(1);
    else left(1);
    heading=a;
    return;
  }
}
void run(char a)
{
  rotate(a);
  forward();
}
void loop() {
  if(SerialBT.available())
  {
    String ch=SerialBT.readStringUntil('\n');
    int n=ch.length();
    for(int i=0;i<n;i=i+1)
    {
      run(ch.charAt(i));
    }
  }
  delay(50);  
}
