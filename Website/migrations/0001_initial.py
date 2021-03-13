# Generated by Django 3.1.7 on 2021-03-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_title', models.TextField(max_length=50, verbose_name='Mission Title')),
                ('mission_short_text', models.TextField(max_length=100, verbose_name='Mission Short text')),
                ('mission_description', models.TextField(max_length=500, verbose_name='Mission Description')),
                ('vission_title', models.TextField(max_length=50, verbose_name='Vission Title')),
                ('vission_short_text', models.TextField(max_length=100, verbose_name='Vission Short text')),
                ('vission_description', models.TextField(max_length=500, verbose_name='Vission Description')),
                ('journey_title', models.TextField(max_length=50, verbose_name='Journey Title')),
                ('journey_short_text', models.TextField(max_length=100, verbose_name='Journey Short text')),
                ('journey_description', models.TextField(max_length=500, verbose_name='Journey Description')),
            ],
        ),
        migrations.CreateModel(
            name='Board_of_directors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20, verbose_name='Name')),
                ('designation', models.TextField(max_length=20, verbose_name='Designation')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Brand Title')),
                ('description', models.TextField(max_length=100, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Brand Image')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.TextField(max_length=50, verbose_name='Job Title')),
                ('Description', models.TextField(max_length=500, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.IntegerField(verbose_name='Total Products')),
                ('active_employees', models.IntegerField(verbose_name='Active Employees')),
                ('active_dealers', models.IntegerField(verbose_name='Active Dealer')),
                ('total_brands', models.IntegerField(verbose_name='Total Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Requester Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('sub_text', models.TextField(blank=True, max_length=100, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField(verbose_name='Address Line 1')),
                ('address2', models.TextField(verbose_name='Address Line 2')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='investor_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Requester Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Requester Email')),
                ('cell', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('sub_text', models.TextField(blank=True, max_length=100, verbose_name='Subject')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsandEvent',
            fields=[
                ('title', models.TextField(max_length=50, verbose_name='News Headline')),
                ('slug', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to=None, verbose_name='News Photo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Our_partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=50, verbose_name='Partner Name')),
                ('partner_logo', models.ImageField(upload_to=None, verbose_name='Partner Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.TextField(verbose_name='Title')),
                ('p_image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Products Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Slide_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_title1', models.TextField(max_length=20, verbose_name='1st Slide Title')),
                ('slide_content1', models.TextField(max_length=50, verbose_name='1st Slide Content')),
                ('slide_image1', models.ImageField(upload_to=None, verbose_name='1st Slide Image')),
                ('slide_title2', models.TextField(max_length=20, verbose_name='2nd Slide Title')),
                ('slide_content2', models.TextField(max_length=50, verbose_name='2nd Slide Content')),
                ('slide_image2', models.ImageField(upload_to=None, verbose_name='2nd Slide Image')),
                ('slide_title3', models.TextField(max_length=20, verbose_name='3rd Slide Title')),
                ('slide_content3', models.TextField(max_length=50, verbose_name='3rd Slide Content')),
                ('slide_image3', models.ImageField(upload_to=None, verbose_name='3rd Slide Image')),
            ],
        ),
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Topbar_footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.TextField(verbose_name='Facebook Link')),
                ('twitter_link', models.TextField(verbose_name='Twitter Link')),
                ('googleplus_link', models.TextField(verbose_name='GooglePlus Link')),
                ('linkedin_link', models.TextField(verbose_name='Linkedin Link')),
                ('copyright_text', models.TextField(max_length=50, verbose_name='Copyright')),
                ('f_address', models.TextField(blank=True, null=True, verbose_name='Footer_address')),
            ],
        ),
    ]
