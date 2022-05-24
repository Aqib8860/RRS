from django.db import models

# Create your models here.


BOOKING_TYPE = (
	("Per Hour", "Per Hour"),
	("Per Person", "Per Person"),
	("Per Day", "Per Day"),
)

BOOKING_STATUS = (
	("Open", "Open"),
	("Close", "Close"),
	("Not Available", "Not Available"),
)

WIFI_STATUS = (
	("Free", "Free"),
	("Paid", "Paid"),
	("Not Available", "Not Available"),
)

CAFETERIA_STATUS = (
    ("Available", "Available"),
    ("Not Available", "Not Available"),
)

class Resturent(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    address = models.CharField(max_length=180)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    
    booking_type = models.CharField(max_length=16, choices=BOOKING_TYPE)
    booking_price = models.PositiveIntegerField()
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS)
    timing_days_available = models.CharField(max_length=40)

    cafeteria = models.CharField(max_length=15, choices=CAFETERIA_STATUS)
    cafeteria_details = models.TextField(blank=True, null=True)

    wifi = models.CharField(max_length=15, choices=WIFI_STATUS)

    sitting_details = models.TextField()

    resturent_other_details = models.TextField()
    add_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="resturents")


    def __str__(self):
        return str(self.name)

    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
