# Steps
1. create virtual env. `python3 -m venv <virtual env. name>`
1. go to the directory "imagerecognition" where `manager.py` is located
1. install packages `pip install -r requirements.txt `
1. migrate data model `python3 manage.py migrate`
1. create superuser for running POST request `python3 manage.py createsuperuser`
1. run django on your local `python3 manage.py runserver`
 
Please Note: it takes a while to download pre-trained model after running `python3 manage.py runserver`
```shell
> Downloading: "https://download.pytorch.org/models/inception_v3_google-1a9a5a14.pth" to /Users/chloe/.cache/torch/hub/checkpoints/inception_v3_google-1a9a5a14.pth
```



# Test
http://127.0.0.1:8000/api/

# reference
https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f