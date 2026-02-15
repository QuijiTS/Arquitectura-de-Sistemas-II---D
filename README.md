# Tarea 01 - Load Balancer

## Diagrama de la Infraestructura

A continuación se muestra la arquitectura del balanceador de carga utilizando Nginx y Docker Compose:

```mermaid
graph TD
    Cliente([Navegador Web]) -->|http://localhost:8080| LB[Nginx Load Balancer\nPuerto: 8080]
    LB -->|Round Robin| S1[Servidor Web 1\nNginx en Puerto: 80]
    LB -->|Round Robin| S2[Servidor Web 2\nNginx en Puerto: 80]
```

## Comando para ejecutar la infraestructura

Para levantar toda la infraestructura descrita anteriormente, hay que tener instalado Docker y ejecuta el siguiente comando en la raíz del proyecto (donde se encuentra el archivo docker-compose.yml):

```bash
docker compose up -d
```

Para apagarlo se utiliza el siguiente comando en la raíz del proyecto:

```bash
docker compose down
```

## URL del balanceador de carga

Una vez que los contenedores estén en ejecución, puedes acceder al balanceador de carga ingresando a la siguiente dirección en tu navegador:

[http://localhost:8080](http://localhost:8080)
