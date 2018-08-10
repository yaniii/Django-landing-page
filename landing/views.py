from django.shortcuts import render
from .forms import CallForm
from .models import Order

def index(request):
      form = CallForm(request.POST or None)
      if request.method == "POST" and form.is_valid():
            print(request.POST)
            print(form.cleaned_data)
            new_form = form.save()
      return render(request, 'index.html', locals())

#def create_order(request):
      #if request.method == "POST":
            #post_name = request.POST.get('the_Name')
            #post_email = request.POST.get('the_Email')
            #post_phone = request.POST.get('the_Phone')
            #post_service = request.POST.get('the_Service')

            #response_data = {}

            #post = CallForm(Name=post_name,Email=post_email,Phone=post_phone, Service=post_service)
            #post.save()


