from django.contrib import admin
from .models import *   

# Register your models here.

# admin.site.register(Distribution)
admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(MedicalRecord)
admin.site.register(Symptom)
admin.site.register(Recommendation)







