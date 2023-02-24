#ajabubakari
# Name: ABUBAKARI AZIZ JUNIOR
# Index Number: 6921621
# CE257 ASSIGNMENT 3

# a sript to determine the prices of cars of different brands available
# carPrices are in U.S Dollars,$
#types of cars available
carTypes=['limousine', 'convertible', 'microCars', 'cityCars', 'hatchbacks', 'SUV',
          'sedans', 'CUV','subcompactCars','familyCars', 'estateCars', 'grandTower',
          'muscleCars', 'superCars','roadsters', 'minivan', 'pickup', 'coupe', 
          'sportsCar', 'raceCars', 'stationWagon', 'van','jeep', 'luxuryCars',
          'compactCars', 'BMW', 'commercialVehicles', 'mercedesBenz', 'kia',
          'chevrolet']
''''car brand with it equivalent price'''
carPrices={'tesla':96500,'ferrari':12000,'ford':37000,'porsche':4850,'honda':4600,
           'lamborhhini':98070,'toyota':6120,'bentley':10750,'maserati':9770,
           'subaru':8000,'hyundai':9220,'cadillac':8549,'nissan':16000,'acura':5500,
           'jaguar':7000,'scania':6500,'dodge':4700,'daimler':7300,'lexus':7600,
           'saleen':8908.44,'mazda':5600,'tata':5300,'saturn':71900,'KTM':8800,
           'lotus':25000,'hummer':115000,'pagani':3800,'rover':23000,'hino':5400,
           'packard':6600,'scion':4400,'mayback':7200.45,'audi':7600}
name=input('What is your name? ')
print()
print('hello! ' + name )
a=input('please which type of car do you want? ')
b=input('please specify the brand name ')
print()
if b in carPrices:
    print(f'The price of {a} with brand name {b} is ${carPrices[b]:,}')
else:
    print('sorry the brand specified is currently not available ')

         