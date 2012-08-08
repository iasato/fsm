# -*- coding: utf-8 -*-
from django.contrib import admin
from models import (Technician, Task, TaskType)

admin.site.register(Technician)
admin.site.register(Task)
admin.site.register(TaskType)
