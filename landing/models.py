from django.db import models

# Create your models here.
class Order(models.Model):
    Name = models.CharField(max_length=128)
    Email = models.EmailField()
    Phone = models.CharField(max_length=30)
    SERVICE_CHOICE = (
        ('Оценка активов', 'Оценка активов'),
        ('Бизнес планирование', 'Бизнес планирование'),
        ('Стратегический консалтинг', 'Стратегический консалтинг'),
        ('Анализ банков', 'Анализ банков'),
        ('Маркетинговые исследования', 'Маркетинговые исследования'),
    )
    Service = models.CharField(max_length=100, choices=SERVICE_CHOICE)

    def __str__(self):
        return "ФИО: %s Адрес электронной почты: %s Вид услуги: %s" % (self.Name, self.Email, self.Service)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "List of Orders"