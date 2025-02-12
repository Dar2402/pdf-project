from django.shortcuts import render
from django.http import HttpResponse
from .forms import PdfForm
from .utils import generate_pdf
from django.contrib import messages

# Create your views here.



def form_view(request):
    if request.method == "POST":
        form = PdfForm(request.POST)
        if form.is_valid():
            pdf_buffer = generate_pdf(form.cleaned_data)
            response = HttpResponse(pdf_buffer, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="form_data.pdf"'
            messages.success(request, "Form submitted successfully!")
            return response
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = PdfForm()

    return render(request, "pdf_app/form_template.html", {"form": form})

"""
scp -i your-key.pem -r D:\AE\pdf_project ubuntu@your-ec2-public-ip:/home/ubuntu/

"""
