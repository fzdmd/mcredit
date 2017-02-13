from django.db import models

class Creditor(models.Model):
    name = models.CharField(max_length=500, blank=False)
    slug = models.SlugField(unique=True, null=True)
    verifed = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    legal_entity = models.BooleanField(blank=True, default=False)
    address = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return 'borrow', (self.slug,)

class Documents (models.Model):
    passport = models.BooleanField()
    snils = models.BooleanField() # Страховое свидетельство государственного пенсионного страхования
    ndfl = models.BooleanField() # Справка о доходе по форме 2-НДФЛ или по форме банка, подписанная руководителем организации и заверенная печатью.
    employment_history = models.BooleanField() # документ, подтверждающий трудовую занятость заемщика/поручителя 
    insurance = models.BooleanField() # Страховой полис (на заемщика, объект недвижимости или транспортное средство в зависимости от формы кредита)
    estate = models.BooleanField() #Документы, подтверждающие наличие у заёмщика/залогодателя объекта залога (недвижимости);

class Requirements (models.Model):
    age_begin = models.IntegerField()
    age_end = models.IntegerField()
    revenue = models.IntegerField()
    credit_history = models.CharField(max_length=200)
    bail = models.BooleanField()
    pledge = models.BooleanField()
    documents = models.ForeignKey(Documents)

CURRENCY_CHOICES = (
    ('rub', 'Рублей'),
    ('usb', '€'),
    ('usd', '$'),
)

DATE_CHOICES = (
    ('days', 'Дней'),
    ('weeks', 'Недель'),
    ('months', 'Месяцев'),
    ('years', 'Лет'),
)

CONTACTS_CHOICES = (
    ('mail', 'E-mail'),
    ('phone', 'Телефон'),
    ('skype', 'Skype'),
    ('vk', 'Vkontakte'),
)

class Offer (models.Model):
    name = models.CharField(max_length=500, blank=False)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    requirements = models.ForeignKey(Requirements)
    amount = models.CharField(choices=CURRENCY_CHOICES, max_length=100)
    amount_begin = models.IntegerField(null=True, verbose_name="Минимальная сумма займа")
    amount_end = models.IntegerField(null=True, verbose_name="Максимальная сумма займа")
    time = models.CharField(choices=DATE_CHOICES, max_length=100)
    time_begin = models.IntegerField(null=True, verbose_name="Минимальный возраст")
    time_end = models.IntegerField(null=True, verbose_name="Максимальный возраст")
    loan_begin = models.IntegerField(null=True, verbose_name="Минимальная процентная ставка")
    loan_end = models.IntegerField(null=True, verbose_name="Максимальная процентная ставка")
    creditor = models.ForeignKey(Creditor, null=True)
