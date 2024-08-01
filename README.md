# ...Flask Api with Sqlite... 



I have tried to make standard folder structure for every sections creating CRUD.


## Features
+ Authentication and CRUD functionalities.

User Registration
```
  http://127.0.0.1:5000/auth/register
```
  Body
```
{
  "username": "mamun",
  "email": "mamun@example.com",
  "password": "mamun123"
}

```
User Login
```
http://127.0.0.1:5000/auth/login
```
Body
```
{
  "email": "mamun@example.com",
  "password": "mamun123"
}

```

  


+ Two Models 
   - Item
   - Expense


API Routes are

POST 
```
Create an item http://127.0.0.1:5000/items
Create an Expense http://127.0.0.1:5000/expenses
```


Body
```
For Item
{
  "name": "Al Mamun",
  "description": "A Sr software Engineer"
}

For Expense 
{
    "date": "2024-07-31",
    "description": "Movie Ticket",
    "amount": 100
}
```


GET 
 ```
http://127.0.0.1:5000/items   //Read All Items
http://127.0.0.1:5000/expenses
 ```


GET
```
http://127.0.0.1:5000/items/2    //get a single Item
http://127.0.0.1:5000/expenses

```

PUT
```
http://127.0.0.1:5000/items/2 // Update an Item
http://127.0.0.1:5000/expenses/1
```


Body
```
{
  "name": "Al Mamun",
  "description": "A software Engineer"
}
{
    "date": "2024-07-28",
    "description": "James Song",
    "amount": 50.00
}
```


DELETE 
```
http://127.0.0.1:5000/items/3 //Delete an Item
http://127.0.0.1:5000/expenses/2
```


