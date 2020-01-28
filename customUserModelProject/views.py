from django.views.generic import TemplateView
from django.shortcuts import render



def agv_landing_page(request):
    user_groups = request.user.groups.all()
    for group in user_groups:
        print(group)

    context = {
        "user_groups": user_groups,
        "group": group
    }
    return render(request, 'home.html', context)

class AccountsHomeView(TemplateView):
    pass

class AGVAccountsHomeView(TemplateView):
    template_name = "agv_accounts.html"