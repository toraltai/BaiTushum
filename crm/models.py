import datetime

from django.db import models

from users.models import User

LOAN_TYPE = [
    ('LS', 'Лизинг'),
    ('CR', 'Кредит'),
]
MARITAL_STATUSES = [
    ('married', 'Женат/Замужем'),
    ('divorced', 'Разведен'),
    ('widow/widower', 'Вдова/Вдовец'),
    ('single', 'Холост/Незамужем'),
]
STATUS = [
    ('success', 'Выдан'),
    ('processing', 'Обработка'),
    ('discussion', 'На рассмотрении'),
    ('denied', 'Отказано'),
    ('payback', 'Погашен за счет отступных'),
    ('judicial', 'Судебный'),
]


class Client(models.Model):  # Физическое лицо
    full_name = models.CharField(max_length=100, null=False, verbose_name='ФИО клиента')
    credit_type = models.CharField(max_length=30, choices=LOAN_TYPE, verbose_name='Тип кредита')
    status = models.CharField(choices=STATUS, verbose_name='Статус клиента', max_length=30)
    credit_sum = models.CharField(max_length=30, verbose_name='Сумма кредита')
    # ===================================================================
    repaid_by_redemption = models.FileField(verbose_name='Отступные документы', null=True, blank=True,
                                            upload_to='Отступные документы/%Y/%m/%d')
    court_documents = models.FileField(verbose_name='Судебные документы', null=True, blank=True,
                                       upload_to='Судебные документы/%Y/%m/%d')
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUSES, verbose_name='Семейное положение')
    credit_history = models.FileField(null=True,  blank=True, default='Кредитная история отсутствует',
                                      upload_to='client_credit_history/%Y/%m/%d', verbose_name='Кредитная история')
    phone = models.CharField(max_length=100, unique=True, default='+996', verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес прописки')
    client_actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический',
                                             default='Тот же что и по прописке')
    # guarantor = models.CharField(max_length=100, verbose_name='Поручитель')
    income_statement = models.FileField(upload_to='client_income_statement/%Y/%m/%d', null=True, blank=True,
                                        verbose_name='Справка о доходах')
    # mortgaged_property = models.CharField(max_length=255, verbose_name='Залоговое имущество')
    contracts = models.FileField(upload_to='contracts_with_suppliers/%Y/%m/%d', null=True, blank=True,
                                 verbose_name='Договора с подрядчиками и поставщиками')
    report = models.FileField(upload_to='reports_with_suppliers/%Y/%m/%d', null=True, blank=True,
                              verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe')
    monitoring_report = models.FileField(upload_to='media', verbose_name='Oтчет по мониторингу', null=True, blank=True,
                                         )
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    id_credit_spec = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Кредитный специалист', null=True,
                                       blank=True)
    id_guarantor = models.ForeignKey('Guarantor', verbose_name='Поручитель', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    id_property = models.ForeignKey('Property', verbose_name='Залоговое имущество', on_delete=models.CASCADE, null=True,
                                    blank=True, related_name='Property')

    def __str__(self):
        return f'{self.id}. {self.full_name}'

    class Meta:
        verbose_name = "ЧП/ИП"
        verbose_name_plural = "ЧП/ИП"


class Entity(models.Model):  # Юридическое лицо
    full_name_director = models.CharField(max_length=100, verbose_name='ФИО представителя')
    client_company = models.CharField(max_length=50, verbose_name="Компания клиента", auto_created=True, )
    id_company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Компания')
    inn = models.CharField(max_length=20, verbose_name="ИНН")
    credit_type = models.CharField(max_length=30, choices=LOAN_TYPE, verbose_name='Тип кредита')
    # ===================================================================
    repaid_by_redemption = models.FileField(verbose_name='Отступные документы юр.лица', null=True, blank=True,
                                            upload_to='Отступные документы/%Y/%m/%d')
    court_documents = models.FileField(verbose_name='Судебные документы юр.лица', null=True, blank=True,
                                       upload_to='Судебные документы/%Y/%m/%d')

    status = models.CharField(choices=STATUS, verbose_name='Статус клиента', max_length=30)
    credit_sum = models.CharField(max_length=30, verbose_name='Сумма кредита')
    credit_history = models.FileField(null=True, default='Кредитная история отсутствует', blank=True,
                                      upload_to='client_credit_history/%Y/%m/%d', verbose_name='Кредитная история')
    phone = models.CharField(max_length=100, unique=True, default='+996', verbose_name='Телефон компании')
    address = models.CharField(max_length=100, verbose_name='Юр. адрес')
    client_actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический',
                                             default='Тот же что и юр. адрес')
    # mortgaged_property = models.CharField(max_length=255, verbose_name='Залоговое имущество')
    contracts = models.FileField(upload_to='contracts_with_suppliers/%Y/%m/%d', null=True, blank=True,
                                 verbose_name='Договора с подрядчиками и поставщиками')
    report = models.FileField(upload_to='reports_with_suppliers/%Y/%m/%d', null=True, blank=True,
                              verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe')
    monitoring_report = models.FileField(upload_to='media', verbose_name='Oтчет по мониторингу', null=True, blank=True, )
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    souce_of_income = models.ForeignKey('Activity', verbose_name='Источник дохода', on_delete=models.CASCADE, null=True,
                                        blank=True)
    average_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Средний доход в месяц')
    own_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Размер собвственного взноса', null=True, blank=True,)
    assets = models.TextField(help_text='Актив - стоимость – дата приобретения',
                              verbose_name='Активы на момент анализа')
    current_loan = models.CharField(verbose_name='Текущие кредиты', max_length=200)
    id_credit_spec = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Кредитный специалист', null=True)
    id_property = models.ForeignKey('Property', verbose_name='Залоговое имущество', on_delete=models.CASCADE, null=True,
                                    blank=True, related_name='Entity')

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

    def __str__(self):
        return f'{self.id}. {self.client_company} -- {self.full_name_director}'


class Activity(models.Model):
    activites_add = models.CharField(max_length=100, verbose_name='Добавить источник дохода')

    def __str__(self):
        return f'{self.id} - {self.activites_add}'

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сфера деятельности'


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True, verbose_name='Наименование компании')
    inn = models.CharField(max_length=14, unique=True, verbose_name='ИНН Компании')
    legal_address = models.CharField(max_length=100, verbose_name='Юридический адрес')
    actual_address = models.CharField(max_length=100, verbose_name='Фактический адрес')
    telephone = models.CharField(max_length=30, verbose_name='Номер телефона')
    field_activity = models.ForeignKey(Activity, verbose_name='Cфера деятельности', on_delete=models.CASCADE, )
    okpo = models.CharField(max_length=8, unique=True, verbose_name='ОКПО')
    register_number = models.CharField(max_length=30, unique=True, verbose_name='Номер регистрации')
    document = models.FileField(upload_to='company_files/%Y/%m/%d', verbose_name='Документ компании', null=True)

    def __str__(self):
        return f'{self.id}. {self.company_name}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = "Компании"


class Guarantor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО залогодателя')
    status = models.CharField(max_length=30, choices=MARITAL_STATUSES, verbose_name="Семейное положение")
    credit_history = models.FileField(upload_to='credit_history/%Y/%m/%d', null=True, verbose_name='Кредитная история')
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес прописки')
    actual_address = models.CharField(max_length=100, verbose_name='Адрес фактический')
    income_statement = models.FileField(upload_to='guarantor_income_statement/%Y/%m/%d', null=True,
                                        verbose_name='Справка о доходах')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Поручителя'
        verbose_name_plural = 'Поручители'


class Property(models.Model):
    type = models.CharField(max_length=100, verbose_name="Залоговое имущество")
    address = models.CharField(max_length=100, verbose_name='Местонахождение залога')

    def __str__(self):
        return f'{self.id}. {self.type}'

    class Meta:
        verbose_name = 'Залоговое имущество'
        verbose_name_plural = "Залоговые имущества"


class Files(models.Model):
    file = models.FileField(verbose_name='Файл', upload_to='company_files/%Y/%m/%d')
    property = models.ForeignKey(Property, verbose_name='Залоговое имущество', on_delete=models.CASCADE,
                                 related_name='files')

    def __str__(self):
        return f'{self.property.type}. {self.file}'

    class Meta:
        verbose_name = 'Документ на залоговое имущество'
        verbose_name_plural = 'Документы на залоговое имущество'


class Images(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='company_images/%Y/%m/%')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images',
                                 verbose_name='Залоговое имущество')

    def __str__(self):
        return f'{self.property.type}. {self.image}'

    class Meta:
        verbose_name_plural = 'Фотографии залогового имущества'


class Conversation(models.Model):
    date = models.DateField(default=datetime.date.today())
    is_meeting = models.BooleanField(default=False, verbose_name='Личная встреча')
    client = models.CharField(max_length=100, verbose_name='Клиент')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', default='+996')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    desc = models.TextField(max_length=200, verbose_name='Содержание')
    results_report = models.FileField(null=True,
                                      verbose_name="Очет по результатам",
                                      upload_to="results_report/%Y/%m/%d")

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='conversation', verbose_name='ЧП/ИП', null=True, blank=True)
    entity_id = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name='conversation', verbose_name='Юр.лицо', null=True, blank=True)

    def __str__(self):
        return f'{self.id}. {self.client}'

    class Meta:
        verbose_name = 'Переговоры'
        verbose_name_plural = 'Переговоры'


class DataKK(models.Model):
    created_date = models.DateTimeField(null=True, blank=True,
                                        auto_now_add=True, verbose_name="Дата создания:")
    credit_spec_report = models.FileField(null=True,
                                          verbose_name="Заключение кредитного эксперта (скан):",
                                          upload_to="credit_spec/%Y/%m/%d")
    committee_decision = models.FileField(null=True,
                                          verbose_name="Решение КК (скан):",
                                          upload_to="decision/%Y/%m/%d")
    all_contracts = models.FileField(null=True,
                                     verbose_name="Все заключенные договора, перечень и сканы:",
                                     upload_to="all_contracts/%Y/%m/%d")

    scoring = models.CharField(verbose_name="Скоринг:", max_length=150, null=True, blank=True)
    id_entity = models.ForeignKey('Entity', verbose_name='Юридическое лицо', on_delete=models.CASCADE, null=True, )
    id_client = models.ForeignKey('Client', verbose_name='ЧП/ИП', on_delete=models.CASCADE, null=True, blank=True)
    id_spec = models.ForeignKey(User, verbose_name='Кредитный спец', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Документ на КК"
        verbose_name_plural = "Документы на КК"

    # def __str__(self):
    #     if self.id_entity:
    #         return f'{self.id}. {self.id_entity.full_name_director}'
    #     else:
    #         return f'{self.id}. {self.id_client.full_name}'




