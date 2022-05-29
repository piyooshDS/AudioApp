from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import *


# Register your models here.


# --#----admin information regarding AboutUs table---#
class AboutUsModelAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">touch_app</i>'
    list_display = ["company", "heading"]
    form = AboutUsModelAdmin
    actions = None

    def contents(self, obj):
        return mark_safe(obj.content)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            readonly_fields = ['company']
        else:
            readonly_fields = []
        return readonly_fields

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if request.user.is_active and not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = AboutUs.objects.filter(company_id=company.id).count()
            if qs:
                return False
        return True

    def get_queryset(self, request):
        qs = super(AboutUsModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user.email)
            qs = AboutUs.objects.filter(company_id=company.id)
        else:
            qs = AboutUs.objects.all()
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if not request.user.is_superuser:
                kwargs["queryset"] = Companies.objects.filter(representative_email=request.user.email)
        return super(AboutUsModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(AboutUs, AboutUsModelAdmin)


# --#----admin information regarding Terms and Services table---#
@admin.register(TermServices)
class TermsServicesModelAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">style</i>'
    list_display = ["company", "heading"]
    form = TermsServicesModelAdmin
    actions = None

    def get_readonly_fields(self, request, obj=None):
        if obj:
            readonly_fields = ['company']
        else:
            readonly_fields = []
        return readonly_fields

    def contents(self, obj):
        return mark_safe(obj.content)

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if request.user.is_active and not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = TermServices.objects.filter(company_id=company.id).count()
            if qs:
                return False
        return True

    def get_queryset(self, request):
        qs = super(TermsServicesModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = TermServices.objects.filter(company_id=company.id)
        else:
            qs = TermServices.objects.all()
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if not request.user.is_superuser:
                kwargs["queryset"] = Companies.objects.filter(representative_email=request.user.email)
        return super(TermsServicesModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # --#----admin information regarding Privacy Policy table---#


@admin.register(PrivacyPolicy)
class PrivacyPolicyModelAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">lock_outline</i>'
    list_display = ["company", "heading"]
    form = PrivacyPolicyModelAdmin
    actions = None

    def get_readonly_fields(self, request, obj=None):
        if obj:
            readonly_fields = ['company']
        else:
            readonly_fields = []
        return readonly_fields

    def contents(self, obj):
        return mark_safe(obj.content)

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if request.user.is_active and not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = PrivacyPolicy.objects.filter(company_id=company.id).count()
            if qs:
                return False
        return True

    def get_queryset(self, request):
        qs = super(PrivacyPolicyModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = PrivacyPolicy.objects.filter(company_id=company.id)
        else:
            qs = PrivacyPolicy.objects.all()
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if not request.user.is_superuser:
                kwargs["queryset"] = Companies.objects.filter(representative_email=request.user.email)
        return super(PrivacyPolicyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
