import torch
import urllib
import os
from PIL import Image
from torchvision import transforms, models 

class ImageRecognition():
    def __init__(self, image_file, device='cpu'):
        # Process the image input file
        # self.image_file = os.path.join(root_dir, image_file)
        # Asses the internal device: cpu or gpu:
        if device == 'cuda' and torch.cuda.is_available():
            self.device = 'cuda'
        if device == 'cpu':
            self.device = 'cpu'

        self.preprocess = transforms.Compose([              
            transforms.Resize(256),                    
            transforms.CenterCrop(224),                
            transforms.ToTensor(),                     
            transforms.Normalize(                      
            mean=[0.485, 0.456, 0.406],                
            std=[0.229, 0.224, 0.225]                  
        )])

        # def download_file(url, filename):
        #     try: 
        #         urllib.URLopener().retrieve(url, filename)
        #     except: 
        #         urllib.request.urlretrieve(url, filename)

        self.image_file = image_file
        syncsets_file = "/Users/chloe/git/neural-network/imagerecognition/api/imagenet_synsets.txt"
        classes_file = "/Users/chloe/git/neural-network/imagerecognition/api/imagenet_classes.txt"
        
        
        # download_file(image_url, self.image_file)
       
        self.labels = None
        with open(classes_file) as f:
            self.labels = [line.strip() for line in f.readlines()]

        self.dic = {}
        with open(syncsets_file) as s:
            for line in s:
                (key, val) = line.split(' ', 1)
                self.dic[key] = val

    def get_prediction(self):
        input_image = Image.open(self.image_file)
        input_tensor = self.preprocess(input_image)
        inception_v3 = models.inception_v3(pretrained=True)
        inception_v3.eval()

        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = inception_v3(input_batch)

        _, y_hat = torch.max(output, 1) # top probability
        
        return self.dic[self.labels[y_hat]]
 