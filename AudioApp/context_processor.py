from AudioApp.models import *


def Divdata(request):
    if not request.user.is_superuser:
        total = Employess.objects.filter(company__representative_email=request.user)
        active = total.filter(is_employee=True).count()
        lessons = CompanyLesson.objects.filter(company__representative_email=request.user).count()
        return {"active": active, "total": total.count(), "lessons": lessons}
    companies = Companies.objects.all()
    subscribed = companies.filter(is_subscribed=True).count()
    lessons = Lessons.objects.all().count()
    return {"companies": companies.count(), "subscribed": subscribed, "lessons": lessons}
