from django.db import models

# Create your models here.
class Fighter(models.Model):
	#fighter bio
	#
	full_name = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	
	#measurements made in cm
	height = models.IntegerField()
	#arm reach measured from one fingertip to another cm
	arm_reach = models.IntegerField()
	#leg reach measured from hipbone to heel cm
	leg_reach=models.IntegerField()
	#weight measured in lbs
	weight = models.IntegerField()

	gender = models.CharField(max_length=50)
	dob = models.DateField()
	age = models.IntegerField()
	active = models.BooleanField()
	hometown = models.CharField(max_length=100)
	trains_at = models.CharField(max_length=200)
	fighting_style = models.CharField(max_length=100)
	debut = models.DateField()

	#fighter statistics
	#
	#record
	record_wins = models.IntegerField()
	record_losses = models.IntegerField()
	record_draws = models.IntegerField()
	#no contest 
	record_nc = models.IntegerField()

	#knockout
	wins_by_ko = models.IntegerField()
	#submission
	wins_by_sub = models.IntegerField()
	#decision
	win_by_dec = models.IntegerField()

	#grappling
	#percentage grappling accuracy
	grappling_accuracy = models.IntegerField()
	takedown_landed = models.IntegerField()
	takedown_attempted = models.IntegerField()
	takedown_per_15_minutes = models.FloatField() 
	sub_average_per_15_minutes = models.FloatField()
	#percentage takedown defense
	takedown_defense = models.IntegerField()

	#striking
	#percentage striking accuracy
	striking_accuracy = models.IntegerField()
	strikes_landed = models.IntegerField()
	strikes_attempted = models.IntegerField() 
	sigificant_strikes_landed_per_minute = models.FloatField()
	sigificant_strikes_absorbed_per_minute = models.FloatField()
	#percentage sigificant strikes defense
	sigificant_strikes_defense = models.IntegerField()
	knockdown_ratio = models.FloatField()

	#misc
	average_fight_time = models.TimeField()
	ranking = models.IntegerField(blank=True)
	champion = models.BooleanField()
	


	def __str__(self):
		return self.full_name