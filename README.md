# Tweeter API Clone, Twitter! project

## Description
This project is a clone of Twitter's API functionality, implementing core features and endpoints to replicate the basic functionality of the Twitter platform. It's designed as a learning tool and demonstration of RESTful API development.

## Installation
```bash
git clone https://github.com/AmirHosein-Vahed/Ariana-Tweeter.git twitter
cd twitter
pip install -r requirements.txt
python manage.py runserver localhost:8000
```
or use docker to build and run

```bash
git clone https://github.com/AmirHosein-Vahed/Ariana-Tweeter.git twitter
cd twitter
docker build -t twitter-django .
docker run -p 8000:8000 twitter-django
```

## Usage
```bash
POST api/v1/token/                # --> to get token with sending username and password
POST api/v1/token/refresh/        # --> to refresh token
POST api/v1/token/verify/         # --> to verify a token

GET api/v1/posts/                 # --> to see all posts
GET api/v1/posts/?following=true  # --> to see all posts that the user follow that posts' users
GET api/v1/posts/id               # --> to see deatil of a post with id=id
POST api/v1/posts/create/         # --> to create a post 
PUT api/v1/posts/update/id        # --> to update a post content with id=id
DELETE api/v1/posts/delete/id     # --> to delete a post with id=id
```


## Environment Variables
To run this project, you will need to add the following environment variables to your .env file:
```
SECRET_KEY=
```

## License
[MIT](https://choosealicense.com/licenses/mit/)