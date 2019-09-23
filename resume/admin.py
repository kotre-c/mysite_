from django.contrib import admin
from .models import *


class SkillInlineAdmin(admin.TabularInline):
    model = Skill


class ExperienceInlineAdmin(admin.TabularInline):
    model = Experience


class EducationInlineAdmin(admin.TabularInline):
    model = Education


class ProjectInlineAdmin(admin.TabularInline):
    model = Project


class UserInfoAdmin(admin.ModelAdmin):
    inlines = [SkillInlineAdmin, ExperienceInlineAdmin, EducationInlineAdmin, ProjectInlineAdmin, ]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Program)