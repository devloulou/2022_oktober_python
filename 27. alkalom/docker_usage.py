"""
Docker

A Docker egyfajta konténerizációs technológia

Amikor fut nekünk a Docker Desktop, akkor egy ún. dockerd nevű szolgáltatás fut
Ő vezérli magát a Docker működését

- image letöltése registryből
docker pull postgres 

- imagek listázása
docker image ls

- container listázásA
docker container ls

docker run --name postgres -p 5455:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres

POSTGRES_USER - postgres
POSTGRES_PASSWORD - postgres
POSTGRES_DB - postgres


"""