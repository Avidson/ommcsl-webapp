from django.shortcuts import render, redirect
from waitlist.models import waitlist
# Create your views here.


def waitlist_view(request, *args, **kwargs):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        add_to_waitlist = waitlist.objects.create(
            name = name,
            email = email,
            phone_number = phone
        )

        if add_to_waitlist:
            return redirect('Membership:success')

    context = {

    }
    return render(request, 'index.html', context=context)