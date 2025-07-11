from django.db import models

class KainBatik(models.Model):
    nama = models.CharField(max_length=100)
    motif = models.CharField(max_length=100)
    asal_daerah = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama