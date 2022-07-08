maxitema=15
maxitemb=7
nitemsa=input("Inventory of pants:")
nitemsb=input("Inventory of shirts:")
def garage_sale_items(maxitema,maxitemb,nitemsa,nitemsb):
    if float(nitemsa) % 1!=0:
        return("ERROR WRONG NUMBER INPUT. You entered", str(nitemsa), "\n Only add whole numbers up to ", maxitema, ", no negative or fractional numbers accepted.")
    elif float(nitemsb) % 1!=0:
        return("ERROR WRONG NUMBER INPUT. You entered", str(nitemsb), "\n Only add whole numbers up to ", maxitemb, ", no negative or fractional numbers accepted.")
    elif nitemsa == str(nitemsa) or int(nitemsa) < 0:
        return("ERROR WRONG NUMBER INPUT. You entered", str(nitemsa), "\n Only add whole numbers up to ", maxitema, ", no negative or fractional numbers accepted.")
    elif nitemsb == str(nitemsb) or int(nitemsb) < 0:
        return("ERROR WRONG NUMBER INPUT. You entered", str(nitemsb), "\n Only add whole numbers up to ", maxitemb, ", no negative or fractional numbers accepted.")
    else:
        return("You will sell ",int(nitemsa)+int(nitemsb), "today.")

garage_sale_items(maxitema,maxitemb,nitemsa,nitemsb)
