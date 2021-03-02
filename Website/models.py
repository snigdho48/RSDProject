from django.db import models
from django.db.models.fields import TextField


# Create your models here.


class Contact_Info(models.Model):
    address1 = models.TextField(verbose_name="Address Line 1")
    address2 = models.TextField(verbose_name="Address Line 2")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.address1


class Slide_Images(models.Model):
    slide_title1 = models.TextField(max_length=20, verbose_name="1st Slide Title")
    slide_content1 = models.TextField(max_length=50, verbose_name="1st Slide Content")
    slide_image1 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                                     verbose_name="1st Slide Image")

    slide_title2 = models.TextField(max_length=20, verbose_name="2nd Slide Title")
    slide_content2 = models.TextField(max_length=50, verbose_name="2nd Slide Content")
    slide_image2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                                     verbose_name="2nd Slide Image")

    slide_title3 = models.TextField(max_length=20, verbose_name="3rd Slide Title")
    slide_content3 = models.TextField(max_length=50, verbose_name="3rd Slide Content")
    slide_image3 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                                     verbose_name="3rd Slide Image")

    def __str__(self):
        return "Banners"


class Brands(models.Model):
    title = models.TextField(max_length=50, verbose_name="Brand Title")
    description = TextField(max_length=200,verbose_name="Description")

    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True,
                              blank=True,verbose_name="Brand Image")


    def __str__(self):
        return self.title


class Topbar_footer(models.Model):
    facebook_link = models.TextField(verbose_name="Facebook Link")
    twitter_link = models.TextField(verbose_name="Twitter Link")
    googleplus_link = models.TextField(verbose_name="GooglePlus Link")
    linkedin_link = models.TextField(verbose_name="Linkedin Link")
    copyright_text = models.TextField(max_length=50, verbose_name="Copyright")

    def __str__(self):
        return self.facebook_link


class Company_Overview(models.Model):
    total_products = models.IntegerField(verbose_name="Total Products")
    active_employees = models.IntegerField(verbose_name="Active Employees")
    active_dealers = models.IntegerField(verbose_name="Active Dealer")
    total_brands = models.IntegerField(verbose_name="Total Brands")

    def __str__(self):
        return f'Total Products:{str(self.total_products)}'


class Products(models.Model):
    p_title = models.TextField(verbose_name="Title")

    p_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True,
                              blank=True, verbose_name="Products Image")


    description = TextField(max_length=200,verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.p_title


class Board_of_directors(models.Model):

    name = models.TextField(max_length=20,verbose_name="Name")
    designation = models.TextField(max_length=20,verbose_name="Designation")
    image = models.ImageField(upload_to=None,null=True,blank=True, height_field=None, width_field=None, max_length=100)


    def __str__(self):
        return self.name


class Our_partner(models.Model):
    company = models.TextField(max_length=50, verbose_name="Partner Name")
    partner_logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                                     verbose_name="Partner Logo")

    def __str__(self):
        return self.company


class subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class NewsandEvent(models.Model):
    title = models.TextField(max_length=50, verbose_name="News Headline")
    slug = models.SlugField(max_length=200, unique=True)
    description = TextField(verbose_name="Description")
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                              verbose_name="News Photo")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About_us(models.Model):
    mission_title = models.TextField(max_length=50, verbose_name="Mission Title")
    mission_short_text = models.TextField(max_length=100, verbose_name="Mission Short text")
    mission_description = models.TextField(max_length=500, verbose_name="Mission Description")

    vission_title = models.TextField(max_length=50, verbose_name="Vission Title")
    vission_short_text = models.TextField(max_length=100, verbose_name="Vission Short text")
    vission_description = models.TextField(max_length=500, verbose_name="Vission Description")

    journey_title = models.TextField(max_length=50, verbose_name="Journey Title")
    journey_short_text = models.TextField(max_length=100, verbose_name="Journey Short text")
    journey_description = models.TextField(max_length=500, verbose_name="Journey Description")

    def __str__(self):
        return self.mission_title


class Contact(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text=models.TextField(max_length=100,blank=True,verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} {self.created_at}'


class Career(models.Model):
    job_title = models.TextField(max_length=50, verbose_name="Job Title")
    Description = TextField(max_length=200,verbose_name="Description")

    def __str__(self):
        return self.job_title

    # Machine Xtreme IT
    # Team Touhid,Rafi,Tareq,Snigdho