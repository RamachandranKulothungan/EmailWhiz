from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage



def save_resume(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            upload_dir = os.path.join(settings.MEDIA_ROOT, f'docs/users')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            
            fs = FileSystemStorage(location=upload_dir)
            saved_file_name = file_name if file_name else uploaded_file.name
            saved_file_path = fs.save(saved_file_name, uploaded_file)

            return JsonResponse({'message': 'File uploaded successfully!'})

        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

