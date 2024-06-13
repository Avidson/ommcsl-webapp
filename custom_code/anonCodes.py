  
  """ Erase code, may be considered in the future """
  
  
  user_profile = Profile.objects.get(profile_owner=request.user)
            if user_profile.account_balance >= minimum_balance:
                user_profile.account_balance -= Decimal(amount)
                user_profile.save()
                
                create_share_payment_instance = Payment_for_Share.objects.create(
                    client_name = request.user,
                    amount = amount,)

                if create_share_payment_instance:
                    return redirect('main:dashboard')
            else:
                return HttpResponseRedirect('/insufficient-fund/')