from django.contrib import admin

# Register your models here.
from portfolio.apps.info.models import Education, Project, Experience, Company, Institution, Skill, Technology, \
    SkillType
from portfolio.apps.info.models.contact import Contact, SocialProfile

admin.site.register(
    [
        Institution,
        Education,
        Project,
        Company,
        Experience,
        Contact,
        SocialProfile,

        SkillType,
        Skill,
        Technology,
    ]
)