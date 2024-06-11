
# from django.contrib import admin
# from .models import *
# from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email', 'u_id', 'name', 'college', 'phoneNO', 'is_staff', 'is_active', 'date_joined', 'password')
#     ordering = ('-date_joined', 'u_id')  # Order by date_joined in descending order and then by u_id
#     # Add the delete action explicitly
#     actions = ['delete_selected']
#     readonly_fields = ('password',)  # Make the password field read-only

#     # Override the default password widget to display the password hash
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'password':
#             kwargs['widget'] = admin.widgets.AdminTextInputWidget()
#             kwargs['readonly'] = True
#         return super().formfield_for_dbfield(db_field, **kwargs)
    
#     # def has_view_permission(self, request, obj=None):
#     #     return request.user.is_superuser            # for non super user is show the hashed password

# # Register your custom user model with the custom admin class
# admin.site.register(Users_INFO, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users_INFO
from Spoorti.models import Team

class TeamInline(admin.TabularInline):
    model = Team
    extra = 0  # To avoid displaying an empty form for adding a new team in the inline

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'u_id', 'name', 'college', 'phoneNO', 'is_staff', 'is_active', 'date_joined', 'password')
    ordering = ('-date_joined', 'u_id')  # Order by date_joined in descending order and then by u_id
    actions = ['delete_selected']
    readonly_fields = ('password',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'password':
            kwargs['widget'] = admin.widgets.AdminTextInputWidget()
            kwargs['readonly'] = True
        return super().formfield_for_dbfield(db_field, **kwargs)

# Define a new admin class for the Users_INFO model that includes the TeamInline
class CustomUsers_INFOAdmin(admin.ModelAdmin):
    list_display = ('email', 'u_id', 'name', 'college', 'phoneNO', 'is_staff', 'is_active', 'date_joined', 'password')
    ordering = ('-date_joined', 'u_id')
    actions = ['delete_selected']
    readonly_fields = ('password',)
    inlines = [TeamInline]  # Include the TeamInline to display related teams

# Register your custom admin class for Users_INFO model
admin.site.register(Users_INFO, CustomUsers_INFOAdmin)



