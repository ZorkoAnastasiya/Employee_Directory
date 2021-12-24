### _Installing and running the project:_

---

1. Install packages from requirements.txt file

2. Create a .env file in the superproject directory and add to it:

   - Set the environment variable DEBUG (True - for local launch)

   - Add the environment variable DATABASE_URL, indicating the url to the connected database

3. Run the following commands from the superproject directory:
            
    - Apply migrations

        ```
        python manage.py migrate
        ```
    - Load test data into database
        ```
        python manage.py loaddata employees_data.json
        ```
    - Create a superuser for access to project administration
        ```
        python manage.py createsuperuser
        ```    
   
    - Start the local server
        ```
        python manage.py runserver
        ```
    - Create a group "Managers" in the admin panel. Users added to this group have access to the API or users with the "superuser" status.

    - For a complete picture, enter the data in the Payments table.
---	