# Django_test
Django_test

# DRF with serializer project 

# Curl for  Get api 
curl --location 'http://127.0.0.1:8000/api/compliances/' \
--header 'Cookie: csrftoken=9rPGcLE4g2sWuiv7kfanpP7CqBW3yYed'

# Curl for Get api 
curl --location 'http://127.0.0.1:8000/api/applications/' \
--header 'Cookie: csrftoken=9rPGcLE4g2sWuiv7kfanpP7CqBW3yYed'

# Curl for post api compliances with applications 
curl --location 'http://127.0.0.1:8000/api/compliances/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=9rPGcLE4g2sWuiv7kfanpP7CqBW3yYed' \
--data '{
  "name": "tec",
  "applications": [
    {
      "application_name": "App3",
      "product_name": "Product3"
    },
    {
      "application_name": "App4",
      "product_name": "Product4"
    }
  ]
}
'

# Curl for post api applications
curl --location 'http://127.0.0.1:8000/api/applications/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=9rPGcLE4g2sWuiv7kfanpP7CqBW3yYed' \
--data '{
  "application_name": "Your Application Name",
  "product_name": "Your Product Name"
}
'