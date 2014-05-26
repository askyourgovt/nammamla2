from django.contrib import admin
from models import Representative, Role, Party, Constituency, Assembly, Session, RepRole, Attendance

class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name' ,'name_l','key' ,'gender','birth_year','has_picture','qualification','all_time_attendance_percentage', 'all_time_no_questions_asked')
    readonly_fields = ('all_time_attendance_percentage', 'all_time_no_questions_asked')
    list_filter = ['gender',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(RepresentativeAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(RepresentativeAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None
    

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name','name_l','key','weightage')
    list_filter = ['name',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(RoleAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(RoleAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name','name_l','key','short_name','short_name_l')
    list_filter = ['name',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(PartyAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(PartyAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None


class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ('name','name_l','key','number')
    list_filter = ['name',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(ConstituencyAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(ConstituencyAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None


class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('name','name_l','key','start', 'end')
    list_filter = ['name',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(AssemblyAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(AssemblyAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None

class SessionAdmin(admin.ModelAdmin):
    list_display = ('name','name_l','key','start', 'end','assembly','total_working_days','average_member_attendance')
    list_filter = ['name',]
    search_fields = ('name',)

    def get_list_display(self, request):
        display_list = list(super(SessionAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(SessionAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None

class RepRoleAdmin(admin.ModelAdmin):
    list_display = ('representative','constituency','party','assembly', 'role','start','end','has_ec_affidavit')
    list_filter = ['party','assembly']
    search_fields = ('representative','constituency')

    def get_list_display(self, request):
        display_list = list(super(RepRoleAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(RepRoleAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('representative','session','repRole','date','attendance')
    list_filter = ['session','attendance']
    search_fields = ('representative',)

    def get_list_display(self, request):
        display_list = list(super(AttendanceAdmin,self).get_list_display(request))
        return display_list

    def get_actions(self, request):
        actions = super(AttendanceAdmin, self).get_actions(request)
        groups = request.user.groups.all().values_list('name',flat=True)
        if request.user.is_superuser  :
            if 'delete_selected' in actions:
                del actions['delete_selected']            
            return actions
        return None


admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Assembly,AssemblyAdmin)
admin.site.register(Session,SessionAdmin)
admin.site.register(RepRole,RepRoleAdmin)
admin.site.register(Constituency,ConstituencyAdmin)
admin.site.register(Party,PartyAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Representative,RepresentativeAdmin)
