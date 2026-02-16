from django.db import models

# Create your models here.

class Poll(models.Model):       #飲料店
    subject = models.CharField(max_length=200)
    data_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+ ")" + self.subject
class Option(models.Model):         #飲料
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(max_length=200)#飲料名稱
    count = models.IntegerField(default=0)#計數
    price = models.IntegerField(default=0)#價格
    def __str__(self):
        return self.title
# 甜度選項）
class SugarLevel(models.Model):
    level = models.CharField(max_length=50) 

    def __str__(self):
        return self.level

# 冰塊選項
class IceLevel(models.Model):
    level = models.CharField(max_length=50) 

    def __str__(self):
        return self.level

# 加料選項
class Topping(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=10) # 加料通常要錢

    def __str__(self):
        return f"{self.name} (+${self.price})"

# 訂單（把上面所有東西組合起來）
class Order(models.Model):
    drink = models.ForeignKey(Option, on_delete=models.CASCADE)
    sugar = models.ForeignKey(SugarLevel, on_delete=models.SET_NULL, null=True)
    ice = models.ForeignKey(IceLevel, on_delete=models.SET_NULL, null=True)
    toppings = models.ManyToManyField(Topping, blank=True) # 可以選多個料或不加
    customer_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.customer_name} 點了 {self.drink.title}"