from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models
# Register your models here.
# 開発者が完全にオリジナルで作ったダッシュボードは登録が簡単


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    # おそらく順番
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (

            _('Permissions'),
            {

                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.Comment)
