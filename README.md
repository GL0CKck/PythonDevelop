# PythonDevelop
## **Functional Requirements**

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count

# Install #
 $ git clone git@github.com:GL0CKck/PythonDevelop.git

 $ pip install -r requirements.txt 
 
 $ python manage.py runserver 
 
# Docker # 

 You need update settings.py <DATABASE>
 
 $ docker-compose build
 $ docker-compose up
 
# PostMan # 

$ https://www.postman.com/mishamoloko/workspace/my-workspace/collection/12177298-3a06a72c-174f-466c-8cce-4c8f7d4e29ad?action=share&creator=12177298