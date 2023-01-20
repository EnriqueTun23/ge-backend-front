# GE

### Installation

```sh 
 $ sudo apt-get install python3-pip
 $ pip install virtualenv
```

#### Creation virtual
```sh
 $ virtualenv venv
 $ source venv/bin/activate
```

#### To Deactivate
```sh
 $ deactivate
```


### Run django

##### install 

```sh
 $ pip install -r requirements.txt
```
#### run django

```sh
 $ python manage migrate
 $ python manage createsuperuser
 $ python manage runserver
```