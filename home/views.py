from django.shortcuts import redirect

def home(request):
    return redirect('authentication:my_view')