from django.db import models

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=32, default="plastic duck");

class Feature(models.Model):
    name = models.CharField(max_length=32, default="rainbow fart");

class Trait(models.Model):
    name = models.CharField(max_length=32, default="bisexual");

class Character(models.Model):
    name = models.CharField(max_length=32, default="Toto")
    player_name = models.CharField(max_length=32, blank=True)
    level = models.IntegerField(default=0)
    total_hp = models.IntegerField(default=0)
    current_hp = models.IntegerField(default=0)
    temporary_hp_modifier = models.IntegerField(default=0)
    ac = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)
    char_class = models.CharField(max_length=256, default="hobbo")
    background = models.CharField(max_length=256, default="JustinB")
    alignment = models.CharField(max_length=256, default="Justified")
    speed = models.IntegerField(default=-1)
    weapons = models.ForeignKey(Weapon, blank=True, null=True)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    inteligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    presonality_trait = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)
    features = models.ForeignKey(Feature, blank=True, null=True)
    traits = models.ForeignKey(Trait, blank=True, null=True)
    

    

class Bagpack(models.Model):
    character_id = models.ForeignKey(Character, blank=True, null=True)
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    coper = models.IntegerField(default=0)
    platinum = models.IntegerField(default=0)
    EP = models.IntegerField(default=0)

