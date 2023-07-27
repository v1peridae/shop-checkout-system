total_reject = 0
total_accept = 0
total_weight = 0
total_price = 0

num_parcels = int(input("Enter the number of parcels you want >>>"))

for parcel in range(num_parcels):
    parcel_weight = float(input(f"Input the weight of parcel {parcel+1} >>> "))
    parcel_height = float(input("Input the height of your parcel >>> "))
    parcel_width = float(input("Input the width of your parcel >>> "))
    parcel_length = float(input("Input the length of your parcel >>> "))

    if parcel_height > 80 or parcel_width > 80 or parcel_length > 80:
        total_reject += 1
        print("Parcel is either too high, wide or long")
    elif parcel_height + parcel_width + parcel_length > 200:
        total_reject += 1
        print("Parcel is too large")
    elif parcel_weight < 1 or parcel_weight > 10:
        total_reject += 1
        print("Parcel is too heavy")
    else:
        total_accept += 1
        total_weight += parcel_weight

        base_price = 10
        extra_price_per_100g = 0.10
        if parcel_weight <= 5:
            price = base_price
        else:
            extra_weight = parcel_weight - 5
            extra_price = (extra_weight // 0.1) * extra_price_per_100g
            price = base_price + extra_price

        total_price += price
        print("Accepted Parcels - ",total_accept,"\nPrice $",price)

print("Accepted Parcels - ",total_accept,"\nTotal price $",total_price)


