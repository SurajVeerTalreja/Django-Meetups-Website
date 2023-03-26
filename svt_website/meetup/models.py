from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}, {self.address}'



class Participant(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)


    def full_name(self):
        return f'{self.last_name}, {self.first_name}'

    def __str__(self):
        return self.full_name()



class Meetup(models.Model):
    title = models.CharField(max_length=70)
    organizer_email = models.EmailField()
    description = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(Participant, blank=True, null=True)


    def __str__(self):
        return f'{self.title}, Date:{self.date}'
