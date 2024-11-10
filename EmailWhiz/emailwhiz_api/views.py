from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
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

def generate_emails(request):
    if request.method == 'POST':
        data = []
        print(request.POST)
        rows = len(request.POST.getlist('first_name'))  # Get the number of rows
        print(rows)
        resume = request.POST.get('resume')

        for i in range(rows):
            first_name = request.POST.getlist('first_name')[i]
            last_name = request.POST.getlist('last_name')[i]
            recruiter_email = request.POST.getlist('email')[i]
            company = request.POST.getlist('company')[i]
            job_role = request.POST.getlist('job_role')[i]

            # details = get_user_details(request.user)
            details = {
                "first_name":"abc",
                "last_name":"def",
                "university":"asd",
                "linkedin": "asas",
                "phone":"123",
                "regist":"sad",
                "degree":"asda"
            }

            emp_data = {
                'first_name': first_name,
                'last_name': last_name,
                'recruiter_email': recruiter_email,
                'target_company': company,
                'target_role': job_role
            }

            # Collecting data into a dictionary
            employer_data = {
                'recruiter_name': first_name + " "+ last_name,
                'recruiter_email': recruiter_email,
                'target_company': company,
                'target_role': job_role
            }

            user_email = 'bhuvanthirwani@gmail.com'
            # details = get_user_details(request.user)
            # username = details['username']
            
            resume_path = os.path.join(settings.MEDIA_ROOT, user_email, 'resumes', resume)
            print("Resume_PATH: ", resume_path)
            # Extract text from the selected resume
            # extracted_text = extract_text_from_pdf(resume_path)
            extracted_text = "resume text"
            # print("extracted_text: ", extracted_text)

            # Create prompt for Gemini
            details.update(employer_data)
            details['resume'] = extracted_text
            # prompt = get_template(details)
            print(details)
            # Call Gemini API
            # response = call_gemini_api(prompt)
            response = "email content"
            emp_data["email_content"] = response
            data.append(emp_data)
            # print("Response: ", response)
            # if response:
            #     template_text = response.text
            #     return render(request, 'generated_template.html', {'template_text': template_text})
            # else:
            #     return render(request, 'generated_template.html', {'error': "Failed to generate template."})
        print(data)
        return render(request, "view_generated_emails.html", {"data":data})


        # Placeholder: Handle the data (e.g., generate emails)
        print(f"Generated emails for {len(data)} entries")

        # Redirecting to another page after processing
        return HttpResponse("Success")

    return JsonResponse({'error': 'Invalid request method'}, status=405)

# def generate_emails(request):
#     print(json.loads(request.body))
#     return JsonResponse(json.loads(request.body))

def send_emails(request):
    print(json.loads(request.body))
    return HttpResponse("Email Sent")