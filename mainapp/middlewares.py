import datetime


from pytz import utc


class LastRequestUser:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            today = datetime.datetime.utcnow().replace(tzinfo=utc)
            request.user.last_login = today
            request.user.save()
        response = self.get_response(request)
        return response
