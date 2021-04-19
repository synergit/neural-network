# Image Recognition
This is an image recognition project with API:
- [Inception_v3](https://pytorch.org/hub/pytorch_vision_inception_v3/) model pre-trained with images on ImageNet
- [Django REST Framework](https://www.django-rest-framework.org/)

Quick video to see how easy you can run image recognition on your local machine:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/TC3C5jirBxU/0.jpg)](https://www.youtube.com/watch?v=TC3C5jirBxU)

## Installation
- Python v3.6 and above
- Django 
- Django REST Framework
- PyTorch

## Usage
1. Simply run 
    ```shell
    . start-api.sh
    ```
1. Open `localhost:8000`, click the link `"api": "http://localhost:8000/api/"` in as marked in following screenshot
![Screen Shot 2021-04-18 at 10 29 50 PM](https://user-images.githubusercontent.com/10833201/115173864-2b7bbc00-a096-11eb-8c65-1e1806f72000.png)
1. Enter the image path into following `Imagepath` and click `POST` button
![Screen Shot 2021-04-18 at 10 29 42 PM](https://user-images.githubusercontent.com/10833201/115173878-346c8d80-a096-11eb-81b2-b78749df84f3.png)

The image is recognized by AI model and return the top 1 result to you

## Support
- Contact engineer: syner.wang@gmail.com

## Roadmap
- display top 3 result with confidence score
- deploy to DigitalOcean, host it on server
- merge other pre-trained model for fun! 

## Authors
Chloe Wang
* [GitHub](https://github.com/synergit/)
* [LinkedIn](https://www.linkedin.com/in/xwang-1a/)
* [Twitter](https://twitter.com/chloe_wang1)

## Contributing
pull requests are welcome. for major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgement
Thanks to [readme](https://www.makeareadme.com/) for this template and tools. 
