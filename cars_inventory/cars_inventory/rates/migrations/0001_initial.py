from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rates_typ', models.CharField(choices=[('regular', 'regular'), ('VIP', 'VIP'), ('premium', 'premium')], max_length=20)),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=5)),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='event.event')),
            ],
        ),
    ]
