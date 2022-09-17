from django.db import models
from django.core.validators import MinValueValidator,MinLengthValidator,RegexValidator

LOAN_TYPE = [
    ('LS', 'Лизинг'),
    ('CR', 'Кредит'),
]
MARITAL_STATUSES = [
    ('Женат/Замужем', 'Женат/Замужем'),
    ('Разведен', 'Разведен'),
    ('Вдова/Вдовец', 'Вдова/Вдовец'),
    ('Холост/Незамужем', 'Холост/Незамужем'),
]
STATUS = [
    ('Принят','Принят'),
    ('Отказано','Отказано')
]


class Individual(models.Model):     #Физическое лицо
    pass

    class Meta:
        verbose_name = "Документ на КК:"
        verbose_name_plural = "Документы на КК:"


class Entity(models.Model):         #Юридеческое лицо
    pass

    class Meta:
        verbose_name = "Документ на КК:"
        verbose_name_plural = "Документы на КК:"


class Client(models.Model):
    full_name = models.CharField(max_length=100, null=False, verbose_name='ФИО клиента')
    credit_type = models.CharField(max_length=30, choices=LOAN_TYPE, verbose_name='Тип кредита')
    client_status = models.CharField(choices=STATUS, verbose_name='Статус клиента', max_length=30)
    credit_sum = models.CharField(max_length=30, verbose_name='Сумма кредита')
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUSES, verbose_name='Семейное положение')
    credit_history = models.FileField(
            null=True,
            blank=True,
            default='Кредитная история отсутствует',
            upload_to='client_credit_history/%Y/%m/%d',
            verbose_name='Кредитная история')
    phone = models.CharField(max_length=100, unique=True, verbose_name='Номер телефона', help_text='+996 777 777 777')
    address = models.CharField(max_length=100, verbose_name='Адрес прописки')
    client_actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический',
                                             default='Тот же что и по прописке')
    guarantor = models.CharField(max_length=100, verbose_name='Поручитель')
    income_statement = models.FileField(upload_to='client_income_statement/%Y/%m/%d', null=True,
                                        verbose_name='Справка о доходах')
    is_director = models.BooleanField(default=False, verbose_name='Директор компании')
    client_company = models.CharField(max_length=100, verbose_name='Компания клиента')
    mortgaged_property = models.CharField(max_length=255, verbose_name='Залоговое имущество')
    contracts = models.FileField(upload_to='contracts_with_suppliers/%Y/%m/%d', null=True, blank=True,
                                 verbose_name='Договора с подрядчиками и поставщиками')
    report = models.FileField(
        upload_to='reports_with_suppliers/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe'
    )
    monitoring_report = models.FileField(upload_to='media', verbose_name='Oтчет по мониторингу',null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    id_credit_spec = models.ForeignKey('CreditSpecialist', on_delete=models.CASCADE)
    id_guarantor = models.ForeignKey('Guarantor', on_delete=models.CASCADE, null=True, blank=True)
    id_company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    id_property = models.ForeignKey('Property', on_delete=models.CASCADE, null=True, blank=True)
    id_num_parley = models.ForeignKey(
        'TelephoneConversation',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = "Контрагент:"
        verbose_name_plural = "Контрагенты:"


class CreditSpecialist(models.Model):
    pass

    class Meta:
        verbose_name = "Документ на КК:"
        verbose_name_plural = "Документы на КК:"


class Occupation(models.Model):
    name_job_title = models.CharField(max_length=100, verbose_name='Наименование должности')

    def __str__(self):
        return f'{self.name_job_title}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True, verbose_name='Наименование компании')
    legal_address = models.CharField(max_length=100, verbose_name='Юридический адрес')
    actual_address = models.CharField(max_length=100, verbose_name='Фактический адрес')
    telephone = models.CharField(max_length=30, verbose_name='Номер телефона')
    field_activity = models.CharField(max_length=100, verbose_name='Cфера деятельности')
    okpo = models.CharField(max_length=8, unique=True)
    inn = models.CharField(max_length=14, unique=True)
    register_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = "Компании:"


class Guarantor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО залогодателя')

    status = models.CharField(
        max_length=30,
        choices=MARITAL_STATUSES,
        verbose_name="Семейное положение"
    )
    credit_history = models.FileField(upload_to='credit_history/%Y/%m/%d')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес прописки')
    actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический')
    income_statement = models.FileField(upload_to='guarantor_income_statement/%Y/%m/%d')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Поручитель'
        verbose_name_plural = 'Поручители'


class Property(models.Model):
    type = models.CharField(max_length=100, verbose_name="Залоговое имущество")
    address = models.CharField(max_length=100, verbose_name='Местонахождение залога')
    document = models.FileField(upload_to='document/%Y/%m/%d')

    def __str__(self):
        return f'{self.type}'

    class Meta:
        verbose_name = 'Залоговое имущество'
        verbose_name_plural = "Залоговые имущества"


class TelephoneConversation(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Телефонные переговоры'


class MeetConversation(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Личные встречи'


class DataKK(models.Model):
    created_date = models.DateTimeField(
                    auto_now_add=True, verbose_name="Дата создания:")
    credit_spec_report = models.FileField(
                    verbose_name="Заключение кредитного эксперта (скан):",
                    upload_to="credit_spec/%Y/%m/%d")
    committee_decision = models.FileField(
                    verbose_name="Решение КК (скан):",
                    upload_to="decision/%Y/%m/%d")
    all_contracts = models.FileField(
                    verbose_name="Все заключенные договора, перечень и сканы:",
                upload_to="all_contracts/%Y/%m/%d")
    scoring = models.CharField(verbose_name="Скоринг:", max_length=150)
    id_client = models.ForeignKey('Client', on_delete=models.PROTECT)
    id_spec = models.ForeignKey('CreditSpecialist', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Документ на КК:"
        verbose_name_plural = "Документы на КК:"