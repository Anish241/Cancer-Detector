from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
import numpy as np
from tensorflow import keras
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from PIL import Image
import os
import uuid
from register.models import Doctor
import tensorflow 
import cv2
from tensorflow.keras.preprocessing import image


# Create your views here.





    

# Create your views here.
@login_required(login_url='auth/login')
def home(request):
    doctor = Doctor.objects.get(user=request.user)
    return render(request, 'home.html', {'doctor':doctor})
@login_required(login_url='auth/login')
def menu(request):
    return render(request, 'scanner/menu.html')
@login_required(login_url='auth/login')
def brain(request):
    if request.method == 'POST':
        user = request.user
        Patient_Name = request.POST.get('patient-name')
        file = request.FILES['mri-scan']
        scan = Scan(user=user, Patient_Name=Patient_Name)
        scan.save()
        id = scan.id
        #save the image in the media folder with the id as the name and the extension
        unique_filename = str(uuid.uuid4())
        extension = file.name.split('.')[1]
        str_file = unique_filename + '.' + extension
        #save the image in the media folder with the id as the name and the extension
        file = ContentFile(file.read())
        default_storage.save('images/'+str(str_file), file)
        scan.image = 'images/'+str(str_file)

        print(str_file)
    
        scan.save()
        img_url = 'media/images/'+str(str_file)
        model = tensorflow.keras.models.load_model('brain_tumor')
        img = image.load_img(img_url, target_size=(512, 512), color_mode='grayscale')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0

        # Predict the class of the input image
        preds = model.predict(x)
        class_idx = np.argmax(preds)
        class_labels = ['Glioma Tumor Detected', 'Meningiome Tumor Detected', 'No tumor Detected', 'Pitutary Tumor Detected']
        class_name = class_labels[class_idx]
        scan.result = class_name
        scan.save()

        print('Predicted class: ', class_name)
        
        
        return render(request, 'scanner/result.html', {'scan':scan, 'img_url':img_url})


    return render(request, 'scanner/brain.html')

@login_required(login_url='auth/login')
def lung(request):
    if request.method == 'POST':
        user = request.user
        Patient_Name = request.POST.get('patient-name')
        file = request.FILES['mri-scan']
        scan = Scan(user=user, Patient_Name=Patient_Name)
        scan.save()
        id = scan.id
        #save the image in the media folder with the id as the name and the extension
        unique_filename = str(uuid.uuid4())
        extension = file.name.split('.')[1]
        str_file = unique_filename + '.' + extension
        #save the image in the media folder with the id as the name and the extension
        file = ContentFile(file.read())
        default_storage.save('images/'+str(str_file), file)
        scan.image = 'images/'+str(str_file)

        print(str_file)
    
        scan.save()
        img_url = 'media/images/'+str(str_file)
        model = tensorflow.keras.models.load_model('lung_model')
        img = image.load_img(img_url, target_size=(512, 512), color_mode='grayscale')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        preds = model.predict(x)
        class_idx = np.argmax(preds)
        class_labels = ['Benign Cancer Detected', 'Malignant Cancer Detected', 'No Cancer Detected']
        class_name = class_labels[class_idx]
        scan.result = class_name
        scan.save()

        print('Predicted class: ', class_name)
        
        
        return render(request, 'scanner/result.html', {'scan':scan, 'img_url':img_url})



    return render(request, 'scanner/lung.html')

@login_required(login_url='auth/login')
def kidney(request):
     if request.method == 'POST':
        user = request.user
        Patient_Name = request.POST.get('patient-name')
        file = request.FILES['mri-scan']
        scan = Scan(user=user, Patient_Name=Patient_Name)
        scan.save()
        id = scan.id
        #save the image in the media folder with the id as the name and the extension
        unique_filename = str(uuid.uuid4())
        extension = file.name.split('.')[1]
        str_file = unique_filename + '.' + extension
        #save the image in the media folder with the id as the name and the extension
        file = ContentFile(file.read())
        default_storage.save('images/'+str(str_file), file)
        scan.image = 'images/'+str(str_file)
        scan.save()
        
        model = tensorflow.keras.models.load_model('kidney_model')
        img = cv2.imread('media/images/'+str(str_file), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (512, 512))
        img = np.reshape(img, (1, 512, 512, 1))
        img = img.astype('float32') / 255
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions)
        c=0
        if predicted_class == 0:
                scan.result = 'Cyst Detected'
                scan.save()
        elif predicted_class == 1:
                    scan.result = 'No Cancer Detected'
                    scan.save()
                    c=1
        elif predicted_class == 2:
                    scan.result = 'Stone Detected'
                    scan.save()
        else:
                scan.result = 'Tumor Detected'
                scan.save()
        img_url = 'media/images/'+str(str_file)
        
        return render(request, 'scanner/result.html', {'scan':scan, 'img_url':img_url, 'c':c})



     return render(request, 'scanner/kidney.html')


    

