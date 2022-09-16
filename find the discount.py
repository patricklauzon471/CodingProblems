def disc(price, discount):
    FinalPrice = price*((100-discount)/100)
    return FinalPrice


print(disc(123, 20))
