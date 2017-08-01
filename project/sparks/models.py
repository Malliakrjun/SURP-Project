from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name

class spark(models.Model):
    spark_name=models.CharField(max_length=100,blank=False)
    spark_locality=models.CharField(max_length=100,default='')
    spark_city=models.CharField(max_length=100,default='')
    spark_mail=models.EmailField()
    spark_info=models.TextField('description',blank=False)
    spark_organization=models.CharField(max_length=200,blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    contri_1=models.TextField(blank=False,default='')
    contri_2=models.TextField(blank=False,default='')
    contri_3=models.TextField(blank=True)
    contri_4=models.TextField(blank=True)
    contri_5=models.TextField(blank=True)

    award_1=models.TextField(blank=False,default='')
    award_2=models.TextField(blank=False,default='')
    award_3=models.TextField(blank=True)
    award_4=models.TextField(blank=True)
    award_5=models.TextField(blank=True)

    hobby1=models.CharField(max_length=100,blank=True)

    idea_1=models.TextField(blank=False,default='')
    idea_2=models.TextField(blank=False,default='')
    idea_3=models.TextField(blank=True)
    idea_4=models.TextField(blank=True)
    idea_5=models.TextField(blank=True)

    image=models.ImageField(upload_to='sparks',blank=True)

    interests_choices = (
        ('All','All'),
        ('Malnutrition', 'Malnutrition'),
        ('Education', 'Education'),
        ('Poverty', 'Poverty'),
        ('Social Welfare', 'Social Welfare'),
        ('Hygiene and Sanitation', 'Hygiene and Sanitation'),
    )
    interests = models.CharField(
        max_length=30,
        choices=interests_choices,
        default='All'
    )
    GENDER_CHOICES = (
        ('N','None'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='N')


    def __str__(self):
        return self.spark_name


# class contact(models.Model):
#     your_name=models.CharField(max_length=100,blank=False)
#     name_of_your_organization=models.CharField(max_length=200,blank=True)
#     your_email=models.EmailField(blank=False)
#     your_info=models.TextField('description',blank=False)
#     subject=models.CharField(max_length=1000,blank=False)
#     message=models.TextField('description',blank=False)
