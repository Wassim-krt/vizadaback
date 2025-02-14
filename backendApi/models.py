from django.db import models


class Course(models.Model):
    Nomc = models.CharField(blank=True,max_length=100)
    Descriptionc = models.CharField(blank=True,max_length=5000)
    prix = models.FloatField(blank=True)
    image = models.ImageField(upload_to='course/', null=True, blank=True)
    Id_sc = models.ForeignKey("SousCategorie",on_delete=models.SET_DEFAULT,default=0,blank=True)
    link = models.URLField(max_length=300, null=True, blank=True)


class SousCategorie (models.Model):
    Nomsouscategorie = models.CharField(max_length=50)
    Id_c = models.ForeignKey("Categorie",on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.Nomsouscategorie


class Categorie (models.Model):
    Nomcategorie = models.CharField(max_length=50)
    Descriptionc = models.CharField(max_length=300,null=True)
    link = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.Nomcategorie

class Favorite(models.Model):
    Id_user = models.ForeignKey("users.User", on_delete=models.CASCADE, default=0)
    Id_c = models.ForeignKey("Course",on_delete=models.CASCADE,default=0)
    date =models.DateField(auto_now_add=True,null=True)




class Subscribe(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]

    Id_user = models.ForeignKey("users.User", on_delete=models.CASCADE, default=0)
    Datesub = models.DateTimeField(auto_now_add=True)
    DateDebSession = models.DateTimeField(null=True)
    active = models.IntegerField(default=0)
    Id_c = models.ForeignKey("Categorie", on_delete=models.CASCADE, default=0)
    typeS = models.CharField(
        max_length=50,
        choices=SUBSCRIPTION_CHOICES,
        default='monthly',
    )

    def get_price(self):
        if self.Id_c_id == 1:
            if self.typeS == 'monthly':
                return 3500
            elif self.typeS == 'yearly':
                return 35000
        elif self.Id_c_id == 2:
            if self.typeS == 'monthly':
                return 3500
            elif self.typeS == 'yearly':
                return 35000
        return 0
    def get_category_display(self):
        if self.Id_c_id == 1:
            return "IT"
        elif self.Id_c_id == 2:
            return "Management"
        return "Unknown"

    def __str__(self):
        return f"Subscription {self.Id_user} - {self.typeS}"
