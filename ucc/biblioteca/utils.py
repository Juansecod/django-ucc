from django.shortcuts import redirect
from django.contrib import messages

def validate_session(request, message = None):
    user = request.session.get("user_logged", None)
    if user is None:
        if message is not None:
            messages.warning(request, message) 
        return redirect("login")
    else:
        return None