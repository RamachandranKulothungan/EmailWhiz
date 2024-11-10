from PyPDF2 import PdfReader
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ResumeSelectionForm, TemplateSelectionForm
import os

import google.generativeai as genai

genai.configure(api_key='AIzaSyDwBGdGTwqP05cx5GdvuQeZ-F9whEQr1uA')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)



def list_resumes(request, user):
    print("G1")
    user_resumes = os.listdir(f"/users/{user}/resumes")
    if request.method == "POST":
        form = ResumeSelectionForm(request.POST, user_resumes=user_resumes)
        if form.is_valid():
            selected_resume = form.cleaned_data['resume']
            request.session['selected_resume'] = selected_resume  # Store selection in session
            return redirect('select_template', user=user)
    else:
        form = ResumeSelectionForm(user_resumes=user_resumes)
    return render(request, 'myapp/list_resumes.html', {'form': form})

def select_template(request, user):
    email_type = request.POST.get("template_type", "")
    user_templates = os.listdir(f"/users/{user}/templates/{email_type}")
    if request.method == "POST":
        form = TemplateSelectionForm(request.POST, templates=user_templates)
        if form.is_valid():
            if form.cleaned_data['use_gemini']:
                # Call Gemini API here and save template choice
                pass
            else:
                selected_template = form.cleaned_data['template_choice']
                request.session['selected_template'] = selected_template
            return redirect('upload_excel', user=user)
    else:
        form = TemplateSelectionForm(templates=user_templates)
    return render(request, 'myapp/select_template.html', {'form': form})

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
        user_email = 'bhuvanthirwani@gmail.com'  # Replace with actual user logic
        selected_resume = request.POST.get('selected_resume')
        
        resume_path = os.path.join(settings.MEDIA_ROOT, user_email, 'resumes', selected_resume)
        print("Resume_PATH: ", resume_path)
        # Extract text from the selected resume
        extracted_text = extract_text_from_pdf(resume_path)
        
        # Create prompt for Gemini
        prompt = f"Giving you my text of resume:\n{extracted_text}\n\nI want you to provide me a cold email template mail which I can send to a recruiter."
        
        # Call Gemini API
        response = call_gemini_api(prompt)
        print("Response: ", response)
        if response.status_code == 200:
            template_text = response.json().get("generated_template", "No template found.")
            return render(request, 'emailwhiz_ui/generated_template.html', {'template_text': template_text})
        else:
            return render(request, 'emailwhiz_ui/generated_template.html', {'error': "Failed to generate template."})
    else:
        return redirect('list_resumes')

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    

    return text

def call_gemini_api(prompt):
    # url = "https://gemini-api-url.com/generate"  # Replace with actual Gemini API endpoint
    # headers = {"Authorization": "Bearer your_gemini_api_key", "Content-Type": "application/json"}
    # data = {"prompt": prompt}
    # return requests.post(url, json=data, headers=headers)

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(prompt)

    print("response.text", response.text)

    return "Hello"
