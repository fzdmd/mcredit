from django.db import models

# CURRENCY_CHOICES = (
#     ('rub', 'Рублей'),
#     ('usb', '€'),
#     ('usd', '$'),
# )

# DATE_CHOICES = (
#     ('days', 'Дней'),
#     ('weeks', 'Недель'),
#     ('months', 'Месяцев'),
#     ('years', 'Лет'),
# )

CONTACTS_CHOICES = (
    ('mail', 'E-mail'),
    ('phone', 'Телефон'),
    ('skype', 'Skype'),
    ('vk', 'Vkontakte'),
)

class Contacts (models.Model):
    value = models.CharField(max_length=20)
    choice = models.CharField(choices=CONTACTS_CHOICES, default="mail", null=True, blank=True, max_length=100)
    borrower = models.ForeignKey('borrower.Borrower', null=True)

    def __str__(self):
        return self.name + ':' + self.contact_value

# class Amountrange (models.Model):
#     kind = models.CharField(choices=CURRENCY_CHOICES, max_length=100)

# class Timerange (models.Model):
#     king = models.CharField(choices=DATE_CHOICES, max_length=100)

# class Loanrange (models.Model):
#     kind = models.CharField(choices=DATE_CHOICES, max_length=100)
