# Flask Blog Site
This is a Blog website project.
I've used Jinja and Flask-SQLAlchemy extension.
Right now, all the data is coming from database, not the users.

### Home Page
Here all posts will be displayed in brief using ```for loop``` from Jinja. 
![homepage](assets/homepage.png)

Each post will be linked to their own post page, passing data from database and displaying using Jinja. Content will be visible on the post page.
Eg:
![homepage](assets/postpage.png)

### Contacts Page
It has a working contacts page, connected to offline database. Soon will be deployed online

### Blog Post Page
Currently working on fetching posts from users