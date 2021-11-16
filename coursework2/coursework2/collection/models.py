from django.db import models
from django.urls import path, reverse

class Console(models.Model):
    console_name = models.CharField(max_length=200)
    release_date = models.DateField('date released')
    price = models.IntegerField()
    developer = models.CharField(max_length=200)
    def __str__(self):
            return self.console_name

    def to_dict(self):
            return {
                'id': self.id,
                'name': self.console_name,
                'release_date':self.release_date,
                'price':self.price,
                'developer':self.developer,
                'api': reverse('console api', kwargs={'id': self.id}),

            }

class Game(models.Model):
    game_name = models.CharField(max_length=200)
    game_release_date = models.DateField('date released')
    price = models.IntegerField()
    genre = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    compatible_consoles = models.ManyToManyField(Console)
    def __str__(self):
                return self.game_name

    def to_dict(self):
        listOfConsoles = []
        temp = self.compatible_consoles.all()
        for i in range(len(temp)):
            listOfConsoles.append (temp[i].console_name)
        return {
            'id': self.id,
            'name': self.game_name,
            'release_date':self.game_release_date,
            'price':self.price,
            'company':self.company,
            'compatible_consoles' : listOfConsoles,

            'api': reverse('game api', kwargs={'id': self.id}),

        }
