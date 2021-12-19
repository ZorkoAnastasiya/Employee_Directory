from django.db import models


class Positions(models.Model):
    objects = models.Manager()

    job_title = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "position"
        verbose_name_plural = "positions"
        ordering = ["id"]


class Employees(models.Model):
    objects = models.Manager()

    full_name = models.TextField()
    date_start = models.DateTimeField()
    position = models.ForeignKey(Positions, on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    chief = models.ForeignKey("self", null=True, on_delete=models.PROTECT, related_name="employees")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
        ordering = ["full_name", "id"]


class Payments(models.Model):
    objects = models.Manager()

    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    accrued = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.accrued

    class Meta:
        verbose_name = "payout"
        verbose_name_plural = "payments"
        ordering = ["-id"]
