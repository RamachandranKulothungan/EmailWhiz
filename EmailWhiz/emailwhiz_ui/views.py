# EmailWhiz/emailwhiz_ui/views.py
from django.shortcuts import redirect, render
from django.conf import settings
import os
from PyPDF2 import PdfReader
import requests
import os


def home(request):
    return render(request, 'base.html')

def list_resumes(request):
    user_email = 'bhuvanthirwani@gmail.com'  # Placeholder: Replace with the actual user's email
    print("user_email:", user_email)
    resumes_dir = os.path.join(settings.BASE_DIR, 'emailwhiz_api', 'users', user_email, 'resumes')
    print("resume_dir: ", resumes_dir, settings.BASE_DIR)
    resumes = [f for f in os.listdir(resumes_dir) if f.endswith('.pdf')]
    print("resumes: ", resumes)
    return render(request, 'list_resumes.html', {'resumes': resumes, 'user_email': user_email})

def select_template(request):
    user_email = 'bhuvanthirwani@gmail.com'  # Placeholder: Replace with the actual user's email
    templates_dir = os.path.join(settings.BASE_DIR, 'emailwhiz_api', 'users', user_email, 'templates')
    
    first_email_templates = os.listdir(os.path.join(templates_dir, 'first_email'))
    followup_email_templates = os.listdir(os.path.join(templates_dir, 'followup_email'))
    
    context = {
        'first_email_templates': first_email_templates,
        'followup_email_templates': followup_email_templates
    }
    return render(request, 'emailwhiz_ui/select_template.html', context)


def upload_excel(request, user):
    if request.method == "POST":
        excel_file = request.FILES['excel']
        # Process Excel data and render table
        request.session['excel_data'] = ...  # Save processed data in session for preview
        return redirect('preview_template', user=user)
    return render(request, 'myapp/upload_excel.html')

def preview_template(request, user):
    selected_resume = request.session.get('selected_resume')
    selected_template = request.session.get('selected_template')
    excel_data = request.session.get('excel_data')
    if request.method == "POST":
        # Send the email here
        return redirect('success_page')
    return render(request, 'myapp/preview_template.html', {
        'resume': selected_resume,
        'template': selected_template,
        'excel_data': excel_data,
    })


def generate_template(request):
    if request.method == 'POST':
        # (Your existing code to generate the template text)
        template_text = "Your generated email template content here"  # Example content

        return render(request, 'emailwhiz_ui/generated_template.html', {'template_text': template_text})
    else:
        return redirect('list_resumes')