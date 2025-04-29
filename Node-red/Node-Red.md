# Download Node Red:

## Link para instalação:
https://nodered.org/docs/getting-started/local

![image](https://github.com/user-attachments/assets/64add2ea-1db4-4624-a8c3-07e6bda694d4)

![image](https://github.com/user-attachments/assets/af90557e-2d7f-4511-9deb-a7dd007fac91)

![image](https://github.com/user-attachments/assets/0c354201-79cd-4c0f-aa1c-fe4ccc78a462)

![image](https://github.com/user-attachments/assets/ba74cd2d-e19d-4584-8ead-1880cb2aa075)

Opção Sring
![image](https://github.com/user-attachments/assets/c4e5ffc9-4bc7-4cbc-b013-ceb792461509)

Manage Palet
![image](https://github.com/user-attachments/assets/9aea5e8a-8367-47f1-8da2-b4ad77578984)


node-red-node-serialport
![image](https://github.com/user-attachments/assets/87530247-5549-4bc0-812d-9478b42a04e0)

![image](https://github.com/user-attachments/assets/cb2d223a-92b4-48aa-893c-13cbfa397a4a)


![image](https://github.com/user-attachments/assets/432445e0-f7e5-4546-9e96-7e0f011e7f76)

![image](https://github.com/user-attachments/assets/cc64ded2-934a-425b-9a36-89023623fab3)

![image](https://github.com/user-attachments/assets/31e625d3-d736-40dc-a726-e2be6e54f209)

![image](https://github.com/user-attachments/assets/5901d5d6-7cef-4e76-b073-549a516125b3)

Trocar de String para msg
![image](https://github.com/user-attachments/assets/bd1545e2-f1e0-4092-b2a1-c06fcf58cf1d)

O nome vêm dos atributos definidos no arduino:
![image](https://github.com/user-attachments/assets/296c0bb8-79b9-4ee0-87cb-d4b11876e315)
![image](https://github.com/user-attachments/assets/8e96c643-5653-4bec-8b2a-610442218b8e)
![image](https://github.com/user-attachments/assets/1c2f24eb-2021-4625-b8df-30cce2ef00de)

![image](https://github.com/user-attachments/assets/a6e55d4f-ec80-4764-8559-9ffdfe01ea3d)

# Adicionando o Ultrassônico:
![image](https://github.com/user-attachments/assets/6d1719b8-aa61-4df8-ab13-2093fca42045)
![image](https://github.com/user-attachments/assets/8c3916b6-1717-49fa-915d-1c060d228e79)
![image](https://github.com/user-attachments/assets/4ca85c52-0cb2-4958-b2ce-8ec97eab721a)
![image](https://github.com/user-attachments/assets/c29c0174-9819-490d-963c-6db1ecee077e)
![image](https://github.com/user-attachments/assets/1282eb91-fee0-4afc-b770-447f8d9f1e78)

# Exportar no Node-red:
![image](https://github.com/user-attachments/assets/dae33ec5-dbab-4a11-b50a-5cd9ee2dddc2)



## Código Arduino:
#include<DHT.h>
#include <ArduinoJson.h>


#define dhtpin 2
#define dhttype DHT11

#define trigger 4 
#define echo 5  

DHT dht (dhtpin, dhttype);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(trigger, OUTPUT); 
  pinMode(echo, INPUT); 
}

void loop() {
  int temp = dht.readTemperature();
  int umi = dht.readHumidity();
  

  digitalWrite(trigger, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trigger, LOW);

  int dist = pulseIn(echo, HIGH); 
  dist = dist/58;

  //Criando o doc json
  StaticJsonDocument<100>json;
  
  //Criando o Atributo = Valor
  json["Temperatura"] = temp;
  json["Umidade"] = umi;
  json["Distancia"] = dist;

  serializeJson(json, Serial);
  Serial.println();
  //delay(2000);

}

