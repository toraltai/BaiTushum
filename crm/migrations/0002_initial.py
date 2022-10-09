from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
     migrations.swappable_dependency(settings.AUTH_USER_MODEL),
                       ('crm', '0001_initial'),
    ('crm', '0001_initial'),
    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='datakk',
            name='id_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='field_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.activity',
                                    verbose_name='Cфера деятельности'),
        ),
        migrations.AddField(
            model_name='client',
            name='id_credit_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                    verbose_name='Кредитный специалист'),
        ),
        migrations.AddField(
            model_name='client',
            name='id_guarantor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='crm.guarantor', verbose_name='Поручитель'),
        ),
        migrations.AddField(
            model_name='client',
            name='id_num_parley',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='crm.conversation', verbose_name='Переговоры'),
        ),
        migrations.AddField(
            model_name='client',
            name='id_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='crm.property', verbose_name='Залоговое имущество'),
        ),
        migrations.AddField(
            model_name='entity',
            name='id_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='crm.company'),
        ),
        migrations.AddField(
            model_name='entity',
            name='souce_of_income',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.activity',
                                    verbose_name='Источник дохода'),
        ),
        migrations.AddField(
            model_name='datakk',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.entity'),
        ),
    ]
