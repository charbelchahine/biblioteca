from django.utils.timezone import now
from .gateways import update_user

# Doesn't update the model as well. Works fine at the time of writing. 
# If weird behaviour occurs in the future, look here.
def set_last_visit_middleware(get_response):
    def middleware(request):
        if request.user.is_authenticated:
            # Update last visit time after request finished processing.
            key = request.user.user_id
            time = now().strftime("%Y-%m-%d %H:%M:%S")
            update_user(user_id = key, last_visited = time)
        response = get_response(request)
        return response
    return middleware