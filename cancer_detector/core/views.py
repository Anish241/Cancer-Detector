from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.

def home(request):
    return render(request, 'home.html')
=======
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

import tensorflow


    

# Create your views here.
@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')
@login_required(login_url='/')
def menu(request):
    return render(request, 'scanner/menu.html')
@login_required(login_url='/')
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
        model = tensorflow.keras.models.load_model('brain_model.h5')
    
        #remove spaces and replace ( with _ and delete )
        img = tensorflow.keras.preprocessing.image.load_img('media/images/'+str(str_file), target_size=(256, 256))
        img_array = tensorflow.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, 0) 
        predictions = model.predict(img_array)
        if predictions[0][0] > 0.5:
            scan.result = 'Tumor Detected'
            scan.save()
        else:
            scan.result = 'No Tumor Detected'
            scan.save()
        img_url = 'media/images/'+str(str_file)
        
        return render(request, 'scanner/brain_result.html', {'scan':scan, 'img_url':img_url})


    return render(request, 'scanner/brain.html')
>>>>>>> db5877f (brain model created)
