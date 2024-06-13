from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Membership_verification


def subdomain_verification_middleware(get_response):

    """
    Subdomains for courses
    """
    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':

            # get course for the given subdomain
            member_ = 'membership'
            verification_url = reverse('lets-verify-you',
            args=[member_])
            # redirect current request to the course_detail view
            url = '{}://{}{}'.format(request.scheme,
            '.'.join(host_parts[1:]),
            verification_url)
            return redirect(url)
        response = get_response(request)
        return response
    return middleware