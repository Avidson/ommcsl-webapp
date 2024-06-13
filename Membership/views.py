from django.shortcuts import render,  redirect, get_object_or_404
from Membership.models import Membership_verification, Membership_Registration
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .form import AccountCreationForm
from django.contrib.auth.decorators import login_required
from main.models import Profile
from custom_code import pass_code as encrypter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



#Membership registration

@login_required
def verification_view(request):


    if Membership_verification.objects.filter(client_name=request.user).exists():
        obj = get_object_or_404(Membership_verification, client_name=request.user)
        if obj.verification_status == True:
            return HttpResponseRedirect('/Membership/verified/')
        elif obj.verification_status == False:
            return HttpResponseRedirect('/Membership/pending/')
    else:
        if request.method == 'POST' and request.FILES:

            id_type = request.POST['id-type']
            id_image = request.FILES['id-image']
            phone = request.POST['phone-number']

            fs = FileSystemStorage()
            filename = fs.save(id_image.name, id_image)
            upload_media = fs.url(filename)

            membership_verification, created = Membership_verification.objects.get_or_create(
                client_name = request.user,
                id_type = id_type,
                id_image = id_image,
                phone = phone
            )

            if created:
                return redirect('/data-submitted/')
    context = {
        
    }

    return render(request, 'verification/verification.html', context=context)


def member_registration(request, *args, **kwargs):

    form = Membership_Registration(request.POST)
    if request.method == 'POST'and request.FILES:
        first_name = request.POST['first']
        surname = request.POST['surname']
        gender = request.POST['gender']
        age = request.POST['age']
        next_of_kin = request.POST['kin']
        next_of_kin_phone = request.POST['kin-phone']
        date = request.POST['date']
        id_type = request.POST['id-type']
        occupation = request.POST['occupation']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        passport = request.FILES['passport']

        fs = FileSystemStorage()
        filename = fs.save(passport.name, passport)
        upload_media = fs.url(filename)

        new_entry = Membership_Registration.objects.create(
            first_name = first_name,
            surname = surname,
            gender = gender,
            age = age,
            next_of_kin = next_of_kin,
            next_of_kin_phone = next_of_kin_phone,
            reg_date = date,
            identification = id_type,
            occupation = occupation,
            address = address,
            city = city,
            state = state,
            telephone = phone,
            email = email,
            passport = passport
        )

        if new_entry:
            return redirect('Membership:success')


    context = {
        'form' : form,
    }
    return render(request, 'register.html', context=context)


def successful(request, *args, **kwargs):
    return render(request, 'thanks.html', {})

from main.models import Profile
#New account creation part
def create_account(request, *args, **kwargs):

    form = AccountCreationForm()

    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()

            return redirect('Membership:success')
        else:
            messages.info(request, """Your password didn't match. 
            Password should contain upper and lower
            cases and special characters like @$# etc; let's try it again""")

            redirect('Membership:create_account')

    else:
        form = AccountCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/create_account.html', context=context)


#Login part of our application.
def login(request, *args, **kwargs):

    return render(request, '', {})