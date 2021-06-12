from django.db import models
from .user import User
from .department import Department
from .designation import Designation
from .level import Level
from .supervisor import Supervisor


class Profile(models.Model):
    WORK_MAIL = f'staff@workmail.com'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.IntegerField()
    work_mail = models.CharField(max_length=50, default=WORK_MAIL)
    state_of_origin = models.CharField(max_length=50)
    home_address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name}\'s profile'
