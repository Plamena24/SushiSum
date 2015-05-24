from django.db import models

# Create your models here.
class SushiSitting(models.Model):
	sitting_date = models.DateTimeField('date of sitting')
	location_name = models.CharField(max_length = 200)

class SushiType(models.Model):
	name_english = models.CharField(max_length = 200)
	name_japanese = models.CharField(max_length = 200)
	sushi_picture = models.ImageField()

	def __unicode__(self):
		return self.name_english

class SushiPieces(models.Model):
	sitting = models.ForeignKey(SushiSitting)
	sushi_type = models.ForeignKey(SushiType)
	sushi_tally = models.IntegerField(default=0)