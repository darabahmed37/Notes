
# Notes Taking Application



## Installation

Install Django project Following Commands

```bash
  pip install -r requirements.txt
```
    
# Category 

Run the Server with 
``python3 manage.py runserver 8000``

Open a API Client and use these endPoints to make an API Request

To add a new Category or to Retrieve all Category 

http://127.0.0.1:8000/cat/
```
{
    "description": "", //Enter description Here
    "priority": null // Enter An Integer Value for priority
}

```
To Update,Delete, Retrieve 

http://127.0.0.1:8000/cat/1


Where the Integer at the end is the ID of Category
# Notes
To get All Notes

http://127.0.0.1:8000/notes/

to Apply Ordering With Respect to priority

http://127.0.0.1:8000/notes/?ordering=category__priority

or to get Value in descending order use ``ordering=-category__priority``

To Get, Update, Delete one single note use this end point

``http://127.0.0.1:8000/notes/1/``

whereas 1 is the Primary key

Now to Add A new Notes 

``http://127.0.0.1:8000/notes/new/``

```
{
    "information": "",
    "category": null
}
```

pass this in Request Body