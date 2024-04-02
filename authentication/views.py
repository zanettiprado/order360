import os
from django.shortcuts import render
from order360.env import get_access_token  # Import get_access_token from env.py in the root of your project

def my_view(request):
    # Retrieve client_id and client_secret from environment variables
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    
    # Check if client_id and client_secret are not None
    if client_id and client_secret:
        # Call get_access_token function with client_id and client_secret
        access_token = get_access_token(client_id, client_secret)
        
        # Render your template or return a response
        return render(request, 'authenticator.html', {'access_token': access_token})
    else:
        # Handle case where client_id or client_secret is missing
        return render(request, 'error_template.html', {'error_message': 'Client ID or Client Secret is missing'})