from django.contrib import admin
from .models.user import User
from .models.profile import Profile
from .models.level import Level
from .models.designation import Designation
from .models.department import Department
from .models.supervisor import Supervisor

admin.site.register((User, Profile, Level, Department, Designation, Supervisor))
