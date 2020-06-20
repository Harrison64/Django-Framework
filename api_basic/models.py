from django.db import models

#Modelo departamento
class departamento(models.Model):
    id = models.AutoField(primary_key = True)
    dep_cod = models.IntegerField()
    dep_nom = models.CharField(max_length=20)
    dep_tel =  models.IntegerField()
    dep_ubica = models.CharField(max_length=5)
    dep_mod =  models.IntegerField()
    
    def __str__(self):
        return '{0},{1}'.format(self.dep_nom,self.dep_nom)

#Modelo trabajador
class trabajador(models.Model):
    id = models.AutoField(primary_key = True)
    tra_cod = models.IntegerField()
    tra_nom = models.CharField(max_length=20)
    tra_apell = models.CharField(max_length=20)
    tra_tel = models.IntegerField()
    tra_cargo = models.CharField(max_length=20)
    tra_sal = models.IntegerField()
    
    def __str__(self):
        return '{0},{1}'.format(self.tra_apell,self.tra_nom)
        
#Modelo cliente
class cliente(models.Model):
    id = models.AutoField(primary_key = True)
    cli_cod = models.IntegerField()
    cli_nom = models.CharField(max_length=20)
    cli_apell = models.CharField(max_length=20)
    cli_tel = models.IntegerField()
    
    def __str__(self):
        return '{0},{1}'.format(self.cli_apell,self.cli_nom)

#Modelo ventas
class ventas(models.Model):
    id = models.AutoField(primary_key = True)
    ven_codp = models.IntegerField()
    ven_nom = models.CharField(max_length=20)
    ven_descrip = models.CharField(max_length=20)
    ven_costo = models.IntegerField()
    
    def __str__(self):
        return '{0}'.format(self.ven_nom)        
        