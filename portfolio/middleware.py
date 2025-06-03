from django.shortcuts import redirect

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the user is trying to access the admin and is not staff, redirect them
        if request.path.startswith('_crack_404_@/') and not request.user.is_staff:
            return redirect('/')  # Redirect them to homepage or any other public page
        return self.get_response(request)