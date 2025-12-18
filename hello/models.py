from django.db import models

# Model do liczenia wizyt
class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit at {self.created_at}"