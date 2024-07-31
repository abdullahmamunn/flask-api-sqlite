# ...Flask Api with Sqlite... 



I have tried to make standard folder structure for every sections creating CRUD.


## Features
+ Authentication and CRUD functionalities.


+ Two Models 
   - Item
   - Expense


API Routes are

POST 
```
Create an item http://127.0.0.1:5000/items
```


Body
```
{
  "name": "Al Mamun",
  "description": "A Sr software Engineer"
}
```


GET 
 ```
http://127.0.0.1:5000/items   //Read All Items
 ```


GET
```
http://127.0.0.1:5000/items/2    //get a single Item
```

PUT
```
http://127.0.0.1:5000/items/2 // Update an Item
```


Body
```
{
  "name": "Al Mamun",
  "description": "A software Engineer"
}
```


DELETE 
```
http://127.0.0.1:5000/items/3 //Delete an Item
```


