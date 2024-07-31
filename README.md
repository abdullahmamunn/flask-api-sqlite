...Flask Api with Sqlite... 



I have tried to make standard folder structure for every sections creating CRUD.


#Two Models 


--> Item


--> Expense


API Routes are

POST Create an item
http://127.0.0.1:5000/items


Body
{
  "name": "Al Mamun",
  "description": "A Sr software Engineer"
}


GET Read All Items
http://127.0.0.1:5000/items


GET get a single Item
http://127.0.0.1:5000/items/2


PUT Update an Item
http://127.0.0.1:5000/items/2


Body
{
  "name": "Al Mamun",
  "description": "A software Engineer"
}


DELETE Delete an Item
http://127.0.0.1:5000/items/3


