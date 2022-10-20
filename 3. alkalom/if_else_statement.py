# elágazások
# vezérlő szerkezetek

# osszeg1 = ha a num1 > num3 -> num1 + num2
# osszeg2 = ha num2 > num3 -> num2 + num3
# if else

# if (num1 > num3) {
#   osszeg1 = num1 + num2
# };


# indentációt - indent
# kód block
num1 = 15
num2 = 8
num3 = 10

osszeg1 = 0
osszeg2 = 0

# 
# boolean - logikai érték -> True - Igaz, False - Hamis

is_it_ok = False

if num1 > num3:
    osszeg1 = num1 + num2
else:
    osszeg1 = num1 + num3

#########################################

if num1 > num3:
    osszeg1 = num1 + num2
elif num1 == num3:
    osszeg1 = num1*2
else:
    osszeg1 = num1 + num3  

print(osszeg1)
#########################################
osszeg1 = 0

if num1 > num3:
    osszeg1 = num1 + num2

if num1 == num3:
    osszeg1 = num1*2


print(osszeg1)