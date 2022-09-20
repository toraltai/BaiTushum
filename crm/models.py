from django.db import models

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
    ('Принят', 'Принят'),
    ('Отказано', 'Отказано')
]



class Client(models.Model):     #Физическое лицо
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
    phone = models.CharField(max_length=100, unique=True, default='+996', verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес прописки')
    client_actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический',
                                             default='Тот же что и по прописке')
    guarantor = models.CharField(max_length=100, verbose_name='Поручитель')
    income_statement = models.FileField(upload_to='client_income_statement/%Y/%m/%d', null=True, blank=True,
                                        verbose_name='Справка о доходах')
    mortgaged_property = models.CharField(max_length=255, verbose_name='Залоговое имущество')
    contracts = models.FileField(upload_to='contracts_with_suppliers/%Y/%m/%d', null=True, blank=True,
                                 verbose_name='Договора с подрядчиками и поставщиками')
    report = models.FileField(
        upload_to='reports_with_suppliers/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe'
    )
    monitoring_report = models.FileField(upload_to='media', verbose_name='Oтчет по мониторингу', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    id_credit_spec = models.ForeignKey('CreditSpecialist', on_delete=models.CASCADE)
    id_guarantor = models.ForeignKey('Guarantor', on_delete=models.CASCADE, null=True, blank=True)
    id_property = models.ForeignKey('Property', on_delete=models.CASCADE, null=True, blank=True)
    id_num_parley = models.ForeignKey(
        'TelephoneConversation',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        if not self.client_company:
            return self.full_name
        else:
            return f'{self.client_company} -- {self.full_name}'

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"


class Entity(Client):  # Юридеческое лицо
    client_company = models.CharField(max_length=50,
                                            verbose_name="Компания клиента", auto_created=True,)
    id_company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    inn = models.CharField(max_length=20, verbose_name="ИНН")
    souce_of_income = models.ForeignKey('Activity', verbose_name='Источник дохода', on_delete=models.CASCADE)
    average_salary = models.IntegerField(verbose_name='Cредний доход')
    own_contribution = models.IntegerField(verbose_name='Размер собвственного вклада')
    current_loan = models.CharField(verbose_name='Текущие кредиты', max_length=50)

    class Meta:
        verbose_name = "Юридеческое лицо"
        verbose_name_plural = "Юридеческое лицо"


class CreditSpecialist(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО кредитного специалиста')
    job_title = models.OneToOneField('Occupation', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} -- {self.job_title}'

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = "Специалисты"


class Occupation(models.Model):
    OCCUPATION = [
        ('CreditSpecialist', 'Кредитный специалист'),
        ('Creditadministrator', 'Кредитный администратор')
    ]
    name_job_title = models.CharField(max_length=100, choices=OCCUPATION, verbose_name='Наименование должности',
                                      null=True, blank=True)
    name_job_title_add = models.CharField(max_length=100, verbose_name='Добавить должность', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name_job_title_add:
            res = (str(self.name_job_title_add), str(self.name_job_title_add))
            self.OCCUPATION.append(res)
            self.name_job_title = self.name_job_title_add
            super(Occupation, self).save(*args, **kwargs)
        else:
            super(Occupation, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name_job_title}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Activity(models.Model):
    ACTIVITES = [
        ('1','сельское хозяйство'),
        ('2','торговля'),
        ('3','производство'),
        ('4','заготовка и переработка'),
        ('5','промышленность'),
        ('6','торговля и коммерция'),
        ('7','строительство'),
        ('8','транспорт'),
        ('9','услуги'),
        ('10','прочие')
    ]
    activites = models.CharField(max_length=100, choices=ACTIVITES, verbose_name='Источник дохода', null=True, blank=True)
    activites_add = models.CharField(max_length=100, verbose_name='Добавить источник дохода', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.activites_add:
            res = (str(self.activites_add), str(self.activites_add))
            self.ACTIVITES.append(res)
            self.activites = self.activites_add
            super(Activity, self).save(*args, **kwargs)
        else:
            super(Activity, self).save(*args, **kwargs)

    def __str__(self):
        if self.activites_add:
            return self.activites_add
        else:
            return str(self.activites)

    class Meta:
        verbose_name_plural = 'Сфера деятельности'


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True, verbose_name='Наименование компании')
    inn = models.CharField(max_length=14, unique=True)
    legal_address = models.CharField(max_length=100, verbose_name='Юридический адрес')
    actual_address = models.CharField(max_length=100, verbose_name='Фактический адрес')
    telephone = models.CharField(max_length=30, verbose_name='Номер телефона')
    field_activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Cфера деятельности')
    okpo = models.CharField(max_length=8, unique=True)
    register_number = models.CharField(max_length=30, unique=True)
    document = models.FileField(upload_to='company_files/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = "Компании"


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
        verbose_name = "Документ на КК"
        verbose_name_plural = "Документы на КК"


'''
Должности:
    1) Создать юзера со всеми его атрибутами
    2) Сделать возможность присваивать должности зарегестрированным юзерам
    3) Дать эту возможность только кредитному админу
    4) Возможность вбивать или выбирать должность
    
Компании:
    5) Разделить физ.лиц от юр.лиц
    6) Создать модельку для сфер деятельности
    7) В модель Company добавить возможность прикрепления документа
    8) В модель Company добавить поле для прикрепления файла
    
Контрагент (Client):
    9) Добавить поле связанное (foreignkey) с моделью CreditSpecialist
    10) Choices на статус клиента

Кредный специалист:
    11) Поменять название на "Специалист"
    12) Возможность выбирать юзера и должность
    
Поручители:
    13) Убрать из бутерброда и добавить в раздел "Контрагент"
    14) В разделе "Контрагент" поле поручитель должно перенаправлять на API создания поручителя

В мониторинг залога нужно добавить поля:
    1.отчет по мониторингу (возможно несколько документов)
    2.фотографии залога
    3.нужно уточнить куда добавлять вышеуказанные два поля в модель Залогового имущества или в Контрагенты
    
    Уточнено: в Залоговое имущество 5-6 документов, 10-15 фотографий
'''
