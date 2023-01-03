from django.db import models

# Create your models here.

class Issue(models.Model):

    title = models.CharField(max_length=200, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    BUG = "BUG"
    FEATURE_REQUEST = "FR"
    ISSUE_TYPE_CHOICES = [
        (BUG, "Bug"),
        (FEATURE_REQUEST, "Feature Request")
    ]

    issue_type = models.CharField(
        max_length=30,
        choices=ISSUE_TYPE_CHOICES,
        default=BUG,
        )

    def __str__(self) -> str:
        return self.title