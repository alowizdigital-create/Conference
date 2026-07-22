from django.shortcuts import render,redirect
from .forms import CompanyForm
# from participants.models import Participant


# def dashboard(request):

#     context = {
#         "participants_count": Participant.objects.count(),

#         "responsables_count": Participant.objects.filter(
#             quality="responsable"
#         ).count(),

#         "pasteurs_count": Participant.objects.filter(
#             quality="pasteur"
#         ).count(),

#         "etudiants_count": Participant.objects.filter(
#             quality="etudiant"
#         ).count(),

#         "participants": Participant.objects.order_by("-created_at")[:5],
#     }

#     return render(request, "dashboard/index.html", context)



# Create your views here.

def company_create(request):

    form = CompanyForm()

    if request.method == "POST":
        form = CompanyForm(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()

            return redirect("company_list")

    return render(request, "company/add.html", {
        "form": form
    })

def company_list(request):

    categories = Category.objects.filter(company=request.company)

    return render(request, "products/category_list.html", {
        "categories": categories
    })
