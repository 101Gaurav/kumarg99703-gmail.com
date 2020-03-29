from django.db import models


# Create your models here.
class covid:
    id: int
    country: str
    flag = str
    total_cases: int
    cured: int
    deaths: int

c1=covid()
c1.id=1
c1.country="China"
c1.flag = "china.jpg"
c1.total_cases= 80000
c1.cured= 50000
c1.deaths = 3300

c2=covid()
c2.id=1
c2.country="India"
c2.flag = "India.jpg"
c2.total_cases= 1000
c2.cured= 80
c2.deaths = 25

cov=[c1,c2]
