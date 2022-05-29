""" admin file"""
import datetime
from datetime import date

from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models import Sum
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils.safestring import mark_safe

from .forms import *
from .models import CompanyLesson, Lessons, EmployeeLesson, Chapters, Intro


# Register your models here.


class IntroAdmin(admin.ModelAdmin):
    """ Doctstring for Intro class"""
    form = Introform
    icon = '<i class="material-icons">cloud_upload</i>'
    list_display = ('filename', 'created_at', 'Preview')

    def Preview(self, obj):
        if obj.chapter != None:
            return mark_safe(
                '<div style="position:relative;top:10px;width:100px;overflow: hidden;direction:ltl;border-top-right-radius: 0.5em 0.5em;border-bottom-right-radius: 1em 0.7em;"><audio controls><source src="{}" type="audio/mpeg"></audio></div>'.format(
                    obj.chapter.url))

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if Intro.objects.all().count():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        """method to remove delete action from admin"""
        # Disable delete
        actions = super(IntroAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


admin.site.register(Intro, IntroAdmin)


class LessonInline(admin.TabularInline):
    """ docstring for class"""
    model = CompanyLesson
    fields = ['lesson', 'expiry_date']
    verbose_name_plural = 'Assigned Lesson'
    readonly_fields = ['logo']

    # By Defalt extra is 3
    def get_extra(self, request, obj, **kwargs):
        return 0

    def logo(self, obj):
        return mark_safe('<img src={} style=height:70px width=70px;></img>'.format('/static/image/img1.jpg'))

    def has_add_permission(self, request):
        return True


class CompaniesModelAdmin(admin.ModelAdmin):
    """ docstring for class"""
    date_hierarchy = 'created_at'
    icon = '<i class="material-icons">work</i>'
    list_display = ("company_name", "id", "Company_Image", "created_at", "status")
    search_fields = ("company_name", "id")
    actions = ['change_access']
    actions_on_top = True
    list_per_page = 10

    def Company_Image(self, obj):
        if obj.logo != None:
            return mark_safe('<img src={} style=height:70px width=70px;></img>'.format(obj.logo.url))
        return mark_safe('<img src={} style=height:70px width=70px;></img>'.format('/static/image/download.jpg'))

    def status(self, obj):
        if obj.is_subscribed:
            return mark_safe('<div><font color="green">Subscribed</font></div>')
        return mark_safe('<div><font color="red">Unsubscribed</font></div>')

    def change_access(self, modeladmin, queryset):
        for obj in queryset:
            if obj.is_subscribed:
                obj.is_subscribed = False
            else:
                obj.is_subscribed = True
            obj.save()

    change_access.short_description = "Change Access"

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.is_superuser == True:  # obj is not None, so this is an edit
            readonly_fields = ['image', ]
        return readonly_fields

    def get_form(self, request, obj, *args, **kwargs):
        self.form = CompanySignUp
        return super(CompaniesModelAdmin, self).get_form(request, obj, *args, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        if obj:
            self.inlines = [LessonInline, ]
            return self.readonly_fields
        self.inlines = []
        return self.readonly_fields


admin.site.register(Companies, CompaniesModelAdmin)


class EmployeeLessonInline(admin.TabularInline):
    """ docstring for class"""
    model = EmployeeLesson
    fields = ['lesson']
    verbose_name_plural = 'Assigned Lesson'

    def get_extra(self, request, obj, **kwargs):
        return 0

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request):
        return False


class EmployeeModelAdmin(admin.ModelAdmin):
    """ docstring for class"""

    form = EmployeeSignUp
    icon = '<i class="material-icons">supervisor_account</i>'
    list_per_page = 10
    search_fields = ('employee_id', 'firstname', 'lastname', 'jobtitle',)


    def get_fieldsets(self, request, obj=None):
        if obj:
            fieldsets = (
            (('Employee details '), {'fields': ['company','employee_id', 'firstname','lastname','jobtitle','date_time','employee_code','is_employee']}),)
        else:
            fieldsets = (
            (('Employee details '), {'fields': ['company','employee_id', 'firstname','lastname','employee_email','jobtitle','date_time','employee_code','is_employee']}),)
        return fieldsets




    def get_list_display(self, request):
        if request.user.is_superuser:
            list_display = ["company", "employee_id", "Employee_Image", "first_name", "last_name", "job_title",
                                "email", "date_time", "is_employee", ]

        else:
            list_display = ["employee_id", "Employee_Image", "first_name", "last_name", "job_title", "email",
                            "date_time", "is_employee", ]

        return list_display

        
    # def change_view(self, request, object_id, extra_context=None):       
    #     self.readonly_fields = ('employee_email', )
    #     return super(EmployeeModelAdmin, self).change_view(request, object_id, extra_context)
    



    def first_name(self, obj):
        return truncatechars(obj.firstname, 10)

    def email(self, obj):
        return truncatechars(obj.employee_email, 10)

    def last_name(self, obj):
        return truncatechars(obj.lastname, 10)

    def job_title(self, obj):
        return truncatechars(obj.jobtitle, 10)

    def Employee_Image(self, obj):
        if obj.image != None:
            return mark_safe('<img src={} style=height:70px width=70px;></img>'.format(obj.image.url))

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = []
        if obj:
            readonly_fields = ['employee_email']
            return self.readonly_fields
        elif request.user.is_superuser:
            self.readonly_fields = ["company"]
            return self.readonly_fields
        else:
            self.inlines = []
            return self.readonly_fields

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def get_queryset(self, request):
        qs = super(EmployeeModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            company = Companies.objects.get(representative_email=request.user)
            qs = Employess.objects.filter(company_id=company.id)
        else:
            qs = Employess.objects.all()
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            if request.user.is_superuser:
                kwargs["queryset"] = Companies.objects.all()
            else:
                kwargs["queryset"] = Companies.objects.filter(representative_email=request.user.email)
        return super(EmployeeModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Employess, EmployeeModelAdmin)


class ChapterModelAdmin(admin.ModelAdmin):
    """ docstring for class"""
    list_display = ["chapter_name", "chapter_Audio", "lesson"]
    form = ChapterAdd

    def get_fieldsets(self, request, obj=None):
        if obj and request.user.is_superuser == True:
            fieldsets = (
                (('Chapter Details'), {'fields': ['lesson', 'chapter_name', 'Audio', 'chapter', ]}),)
        else:
            fieldsets = (
                (('Chapter Details'), {'fields': ['lesson', 'chapter_name', 'chapter', ]}),)
        return fieldsets

    # def chapter_Audio(self, obj):
    #     return mark_safe(
    #         '<div onclick="check()" style="position:relative;top:10px;width:100px;overflow: hidden;direction:ltl;border-top-right-radius: 0.5em 0.5em;border-bottom-right-radius: 1em 0.7em;"><audio controls onpause="check()"><source  type="audio/mpeg"></audio></div>'.format(
    #             obj.chapter.url))

    def Audio(self, obj):
        if obj.chapter != None:
            return mark_safe(
                '<div onclick="check()" style="position:relative;top:10px;width:100px;overflow: hidden;direction:ltl;border-top-right-radius: 0.5em 0.5em;border-bottom-right-radius: 1em 0.7em;"><audio controls onpause="check()"><source  type="audio/mpeg"></audio></div>'.format(
                    obj.chapter.url))

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.is_superuser == True:  # obj is not None, so this is an edit
            readonly_fields = ['Audio', ]
        return readonly_fields


# admin.site.register(Chapters, ChapterModelAdmin)


class ChapterInline(admin.TabularInline):
    """ docstring for class"""
    model = Chapters
    form = ChapterAdd

    def get_extra(self, request, obj, **kwargs):
        return 0

    def get_fields(self, request, obj=None):
        fields = super(ChapterInline, self).get_fields(request, obj)
        if request.user.is_superuser:
            fields = ["chapter_name", "chapter", "lesson", "chapter_Audio"]
        else:
            # l=['chapter','is_complete','status']
            fields.remove('chapter')
            fields.remove('is_complete')
            fields.remove('status')
        return fields

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ['chapter_Audio', ]
        else:
            self.readonly_fields = ['chapter_name', 'chapter_Audio', ]
        return self.readonly_fields

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def chapter_Audio(self, obj):
        return mark_safe(
            '<div style="position:relative;top:10px;width:100px;overflow: hidden;direction:ltl;border-top-right-radius: 0.5em 0.5em;border-bottom-right-radius: 1em 0.7em;"><audio class="" onplay="getcheck(this)" controls><source src="{}" type="audio/mpeg"></audio></div>'.format(
                obj.chapter.url))


class EmployeeInline(admin.TabularInline):
    """ docstring for class"""
    model = EmployeeLesson
    fields = [("employee", "lesson",), "status", "button"]
    readonly_fields = ('employee', 'button', 'status')
    extra = 0
    verbose_name_plural = 'Assigned Employess'

    def status(self, obj):
        if obj.is_access:
            return mark_safe("<font color='green'>Active</font>")
        return mark_safe("<font color='red'>Deactive</font>")

    def button(self, obj, **kwargs):
        if obj.is_access:
            return mark_safe("<a href=" + "/admin/AudioApp/lessons/{}/change/active/{}>".format(obj.lesson_id,
                                                                                                obj.id) + "Click here to Deactivate" + "</a>")
        return mark_safe("<a href=" + "/admin/AudioApp/lessons/{}/change/active/{}>".format(obj.lesson_id,
                                                                                            obj.id) + "Click here to Activate" + "</a>")

    button.allow_tags = True

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return False


class EmployeeInline2(admin.TabularInline):
    """ docstring for class"""
    model = EmployeeLesson
    fields = ["employee", "lesson"]
    verbose_name_plural = ''
    extra = 0

    def get_max_num(self, request, obj, **kwargs):
        total = \
            CompanyLesson.objects.filter(lesson__pk=obj.pk, company__representative_email=request.user.email).aggregate(
                Sum('Employee_slot'))['Employee_slot__sum']
        slots = total - EmployeeLesson.objects.filter(lesson=obj,
                                                      employee__company__representative_email=request.user.email).count()
        return slots

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return True

    def has_delete_permission(self, request, obj=None):
        return True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "employee":
            kwargs["queryset"] = Employess.objects.filter(company_id__representative_email=request.user,
                                                          is_employee=True)
        return super(EmployeeInline2, self).formfield_for_foreignkey(db_field, request, **kwargs)


class LessonModelAdmin(admin.ModelAdmin):
    """ docstring for class"""
    icon = '<i class="material-icons">local_library</i>'
    list_display = ["lesson_name", "Lesson_ID", "image","Created_at"]
    form = LessonsSignUp
    list_per_page = 10

    def Created_at(self,obj):
            return obj.created_at.strftime('%b %d, %Y')

    def Lesson_ID(self, obj):
        return obj.lesson_admin_ID

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = ['image']
            self.inlines = [ChapterInline, ]

        else:
            self.inlines = [ChapterInline, EmployeeInline, EmployeeInline2]
            self.readonly_fields = ['lesson_name', 'image', 'logo',]
        return self.readonly_fields

    def get_fieldsets(self, request, obj=None):
        if obj:
            fieldsets = (
                ((''), {'fields': ['lesson_name', 'lesson_admin_ID', 'image', 'logo',]}),
            )
        else:
            fieldsets = (
                ((''), {'fields': ['lesson_name', 'lesson_admin_ID', 'logo',]}),)
        return fieldsets

    def image(self, obj):
        if obj.logo != None:
            return mark_safe('<img src={} style=height:70px width=70px;></img>'.format(obj.logo.url))

    def Actions(self, obj):
        return mark_safe(
            "<a href=" + "/admin/AudioApp/chapters/{}>".format(obj.id) + "View</a>&nbsp;&nbsp;&nbsp;<a href=" + str(
                obj.id) + ">Edit</a>")

    def get_queryset(self, request):
        """ docstring for class"""
        qs = super(LessonModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            lessons = CompanyLesson.objects.filter(company__representative_email=request.user.email).filter(
                Q(expiry_date__gte=datetime.datetime.today())).values('lesson')
            lesson_Array = [x['lesson'] for x in lessons]
            qs = Lessons.objects.filter(id__in=lesson_Array)
        return qs

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif request.user.is_staff:
            company = Companies.objects.get(representative_email=request.user.email)
            if company.is_subscribed:
                return True
            return False

    def has_change_permission(self, request, obj=None):
        return True
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_actions(self, request):
        # Disable delete
        actions = super(LessonModelAdmin, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Lessons, LessonModelAdmin)


class CompaniesLesson(admin.ModelAdmin):
    """ docstring for class"""
    form = Purchaseform
    icon = '<i class="material-icons"> history </i >'

    def get_list_display(self, request):
        if request.user.is_superuser:
            list_display = ["lesson", "company", "Employee_slot", "Slot_status", "fee", "Created_at", "Expiry_date"]
            # self.list_display_links = (None,)
            self.request = request
        else:
            list_display = ["lesson", "Employee_slot", "fee", "Created_at", "Expiry_date"]
            # self.list_display_links = (None,)
            self.request = request
        return list_display


    def Created_at(self,obj):
            return obj.created_at.strftime('%b %d, %Y')

    def Expiry_date(self, obj):
        user = self.request.user
        if obj.expiry_date >= date.today():
            return obj.expiry_date
        d = obj.expiry_date.strftime('%b %d, %Y')
        if user.is_superuser:
            return mark_safe('<font color="red">{}</font>&nbsp;&nbsp;&nbsp;&nbsp;<a href='.format(
                d) + '/admin/AudioApp/companylesson/{}/change/>Re-subscribe</a>'.format(obj.id))
        return mark_safe('<font color="red">{}</font>'.format(d))

    def Slot_status(self, obj):
        total = CompanyLesson.objects.filter(lesson=obj.lesson, company=obj.company).aggregate(Sum('Employee_slot'))[
            'Employee_slot__sum']
        slot = total - EmployeeLesson.objects.filter(lesson=obj.lesson, employee__company=obj.company).count()
        return mark_safe('<font color="green">' + str(slot) + ' / ' + str(total) + ' slots remain </font>')

    def get_queryset(self, request):
        qs = super(CompaniesLesson, self).get_queryset(request)
        self.request = request
        if not request.user.is_superuser:
            qs = CompanyLesson.objects.filter(company__representative_email=request.user.email)
        return qs

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_actions(self, request):
        actions = super(CompaniesLesson, self).get_actions(request)
        if not request.user.is_superuser:
            del actions['delete_selected']
            return actions
        return actions


admin.site.register(CompanyLesson, CompaniesLesson)


class EmployiesLesson(admin.ModelAdmin):
    """ docstring for class"""
    list_display = ["lesson", "employee"]
    list_per_page = 10

    def has_module_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        company = Companies.objects.filter(representative_email=request.user.email)
        if db_field.name == "employee":
            kwargs["queryset"] = Employess.objects.filter(company=company)
        elif db_field.name == "lesson":
            lessons = CompanyLesson.objects.filter(company__representative_email=request.user.email).values('lesson')
            lesson_Array = [x['lesson'] for x in lessons]
            kwargs["queryset"] = Lessons.objects.filter(id__in=lesson_Array)
        return super(EmployiesLesson, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(EmployiesLesson, self).get_queryset(request)
        if not request.user.is_superuser:
            Employess = EmployeeLesson.objects.filter(
                employee__company__representative_email=request.user.email).values('employee')
            Employee_Array = [x['employee'] for x in Employess]
            qs = EmployeeLesson.objects.filter(employee__in=Employee_Array)

        return qs


admin.site.unregister(Group)
