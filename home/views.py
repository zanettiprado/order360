from django.shortcuts import redirect

def home(request):
    # Redirect to the authentication view
    return redirect('authentication:my_view')