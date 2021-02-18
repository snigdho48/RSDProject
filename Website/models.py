from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.




class Contact_Info(models.Model):

    address=models.TextField(verbose_name="Address")
    cell = models.CharField(max_length = 14,verbose_name="Phone Number")
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.address

class Slide_Images(models.Model):

    slide_title1=models.TextField(max_length=20,verbose_name="1st Slide Title")
    slide_content1 = models.TextField(max_length=50,verbose_name="1st Slide Content")
    slide_image1 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="1st Slide Image")

    slide_title2=models.TextField(max_length=20,verbose_name="2nd Slide Title")
    slide_content2 = models.TextField(max_length=50,verbose_name="2nd Slide Content")
    slide_image2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="2nd Slide Image")

    slide_title3=models.TextField(max_length=20,verbose_name="3rd Slide Title")
    slide_content3 = models.TextField(max_length=50,verbose_name="3rd Slide Content")
    slide_image3 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="3rd Slide Image")

    def __str__(self):
        return "Banners"

class Brands(models.Model):
    title = models.TextField(max_length=50,verbose_name="Brand Title")
    description = RichTextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="Brand Image")

    def __str__(self):
        return self.title


class Topbar_footer(models.Model):
    slogan_text = models.TextField(max_length=50,verbose_name="Slogan Text")
    facebook_link = models.TextField(verbose_name="Facebook Link")
    twitter_link = models.TextField(verbose_name="Twitter Link")
    googleplus_link = models.TextField(verbose_name="GooglePlus Link")
    linkedin_link = models.TextField(verbose_name="Linkedin Link")
    copyright_text = models.TextField(max_length=50,verbose_name="Copyright")

    def __str__(self):
        return self.slogan_text


class Company_Overview(models.Model):
    total_products = models.IntegerField(verbose_name="Total Products")
    active_employees = models.IntegerField(verbose_name="Active Employees")
    active_dealers = models.IntegerField(verbose_name="Active Dealer")
    total_brands = models.IntegerField(verbose_name="Total Brands")

    def __str__(self):
        return self.total_products

class Products(models.Model):
    p_title = models.TextField(verbose_name="Title")
    p_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,name="image",verbose_name="Product Image")
    p_description = models.TextField(max_length=500,verbose_name="Product Descreption")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created At")

    def __str__(self):
        return self.p_title

class Board_of_directors(models.Model):
    name = models.TextField(max_length=20,verbose_name="Name")
    designation = models.TextField(max_length=20,verbose_name="Designation")
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

class Our_partner(models.Model):
    company = models.TextField(max_length=50,verbose_name="Partner Name")
    partner_logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="Partner Logo")

    def __str__(self):
        return self.compnay
class subscribe(models.Model):
    sub_text = models.TextField(max_length=20,verbose_name="Subscription Text")
    email = models.EmailField()

    def __str__(self):
        return self.sub_text

class NewsandEvent(models.Model):
    title = models.TextField(max_length=50,verbose_name="News Headline")
    description = models.TextField(max_length=500,verbose_name="News Content")
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,verbose_name="News Photo")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

class About_us(models.Model):
    mission_title = models.TextField(max_length=50,verbose_name="Mission Title")
    mission_short_text = models.TextField(max_length=100,verbose_name="Mission Short text")
    mission_description= models.TextField(max_length=500,verbose_name="Mission Description")

    vission_title = models.TextField(max_length=50,verbose_name="Vission Title")
    vission_short_text = models.TextField(max_length=100,verbose_name="Vission Short text")
    vission_description= models.TextField(max_length=500,verbose_name="Vission Description")

    journey_title = models.TextField(max_length=50,verbose_name="Journey Title")
    journey_short_text = models.TextField(max_length=100,verbose_name="Journey Short text")
    journey_description= models.TextField(max_length=500,verbose_name="Journey Description")    

    def __str__(self):
        return self.mission_title

class Contact(models.Model):
    name = models.TextField(max_length=50,verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length = 14,verbose_name="Phone Number")
    message = models.TextField(max_length=500,verbose_name="Message")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.created_at


    #Machine Xtreme IT
    #Team Touhid,Rafi,Tareq,Snigdho
