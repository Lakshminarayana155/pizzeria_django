# Pizza Ordering API

This is a Django-based API for ordering pizzas and retriving with id.

## Getting Started

Follow these steps to set up and run the project on your local machine:

### Prerequisites

- docker should be installed on your system.


Run the docker-compose file this will start the services. 
```
    docker-compose up -d
```

Access the django shell to run migrations.
```
    docker-compose exec django bash
```
    
Inside Shell Run this cmd to apply the migrations .
  ```
    python manage.py runserver
  ```   
    
Create the superuser as well if need to access the admin panel.
  ```
    python manage.py createsuperuser
  ``` 
    
Restart the Docker containers.
  ```
    docker-compose down
    docker-compose up -d
  ``` 
    
The API is now up and running.
# usage

Create a Pizza Order
```
    URL: http://127.0.0.1:8000/api/orderpizza/
    Request Body:[
    {
        "base": 2,
        "cheese": 1,
        "toppings": [1, 5, 4, 6, 7]
    },
    {
        "base": 1,
        "cheese": 2,
        "toppings": [1, 3, 4, 6, 7]
    }
    ]
    Response:[
    {
        "id": 1,
        "base": "Normal",
        "cheese": "Cream Cheese",
        "order_status": "Accepted",
        "orderd_at": "2023-09-05T11:06:59.126161Z",
        "total_price": "100.00",
        "toppings": ["Pepperoni", "Onions", "Black Olives", "Sausage", "Pineapple"]
    },
    {
        "id": 2,
        "base": "Thin-Crust",
        "cheese": "Mozzarella",
        "order_status": "Accepted",
        "orderd_at": "2023-09-05T11:06:59.193905Z",
        "total_price": "100.00",
        "toppings": ["Pepperoni", "Green Peppers", "Onions", "Sausage", "Pineapple"]
    }
    ]
```

Retrieve a Pizza Order
```
    URL: http://127.0.0.1:8000/api/pizzaorders/1

    Response:{
    "id": 1,
    "base": "Normal",
    "cheese": "Cream Cheese",
    "order_status": "Preparing",
    "orderd_at": "2023-09-05T11:06:59.126161Z",
    "total_price": "100.00",
    "toppings": ["Pepperoni", "Onions", "Black Olives", "Sausage", "Pineapple"]
    }

 ``` 
You can access the retrieve pizza order api to know the changing order status.
