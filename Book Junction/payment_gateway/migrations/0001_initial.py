# Generated by Django 3.1.5 on 2021-07-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RazorPayDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=250, null=True)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=250, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=250, null=True)),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]