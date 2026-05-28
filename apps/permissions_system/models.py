from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusinessElement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccessRule(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    element = models.ForeignKey(BusinessElement, on_delete=models.CASCADE)

    read_permission = models.BooleanField(default=False)
    create_permission = models.BooleanField(default=False)
    update_permission = models.BooleanField(default=False)
    delete_permission = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} -> {self.element}"