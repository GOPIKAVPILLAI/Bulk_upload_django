from django.shortcuts import render
from .models import ImageModel
import random
# views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm,UserFileForm
from rest_framework.response import Response
def upload_images(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for each in request.FILES.getlist("images"):
                print(each)
                ImageModel.objects.create(image=each)
            return render(request, 'success.html')
     

    else:
        form = ImageUploadForm()
    return render(request, 'upload_images.html', {'form': form})

def random_image_view(request):
    # Select a random image from ImageModel
    random_image = random.choice(ImageModel.objects.all())
    
    # Handle form submission
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the random image for the UserFile instance
            user_file = form.save(commit=False)
            user_file.image = random_image
            user_file.save()
            return redirect('random_image')  # Redirect to the same page after form submission
    else:
        form = UserFileForm()

    return render(request, 'random_image.html', {'random_image': random_image, 'form': form})
