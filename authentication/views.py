
from django.shortcuts import render
from .utils import get_access_token

def my_view(request):
    # Call the function to get the access token
    access_token = get_access_token()
    
    # Use the access token as neededs
    # Example: Pass it to the template
    return render(request, 'authentication/authenticator.html', {'access_token': access_token})
