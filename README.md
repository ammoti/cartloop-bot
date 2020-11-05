# Cartloop-Chat 

cartloop-chat is a RESTFul API for cartloop chat services 

## Installation

You can use docker for run api services.

```bash
cd project-root
docker-compose up
docker-compose run cartloop python manage.py makemigrations cartloop_chat
docker-compose run cartloop python manage.py migrate
docker-compose run cartloop python manage.py loaddata data
docker-compose run cartloop python manage.py runserver
```

all done. You can hack http//:localhost:8000


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)