# proyecto-t-evolvers

[![Whats-App-Image-2022-06-18-at-2-52-08-PM.jpg](https://i.postimg.cc/brwsdkXr/Whats-App-Image-2022-06-18-at-2-52-08-PM.jpg)](https://postimg.cc/DJR2MWw3)
- Pasos para la ejecucion del proyecto
- tener en cuenta que se utiliza una arqeuitectura orientda a enventos
- Tener instalado Docker y docker-compose
- Los respectivos servicios se llaman producer, consumer y register
- se encuentran acompañados por dos bases de datos uno para consumer y otro para register
- con el comando docker ps podemos objervar la creacion de los 3 servicios y 2 bases de datos
- El productor simula el envío de la data del dispositivo
- El consumidor escucha esos eventos, los guarda y los envía al último servicio el registrador
- Para desplegar todos los servicios es el docker-compose up -d --build
- Para listar que efectivamente estén los servicios arriba docker ps
- Una vez estén listos, revisar los logs del producer con docker logs -f producer
- Los logs del consumidor con docker logs -f consumer
- los del registrador con docker logs -f register
- los puertos 8080, 8081, 8082 para los servicios principales deben estar libres en la máquina local donde se ejecuten estos servicios
- En la base de datos que guarda las métricas en el servicio de consumer se creó una tabla llamada metrics que pueden consultar al conectarse a la dB de la siguiente forma: mysql -h localhost -u root -ppassword --port=33061
- En la base de datos que guarda los registros en el servicio de register se creó una tabla llamada registers que pueden consultar al conectarse a la dB de la siguiente forma: mysql -h localhost -u root -ppassword --port=33062
- comandos de conexión a las db:
- mysql --host 0.0.0.0 --port 33061 -ppassword -u root para la db-consumer
- mysql --host 0.0.0.0 --port 33062 -ppassword -u root para la db-register
 
