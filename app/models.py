from django.db import models

# Create your models here.

class Todo(models.Model):
    """Model definition for Todo."""

    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    create_add = models.DateTimeField(auto_now_add=True)    

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.name
