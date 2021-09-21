# dockercompose-two-service-webapp
docker-compose sample of multiple services communicating (API + PHP/apache)

API Service: localhost:5001
---------------
- Expect JSON response

Webpage: localhost:5000
-----------------------
- Expect web page with JSON values


NOTES
---------
#Detached mode 
- `docker-compose up -d`
- Verify `docker ps`
