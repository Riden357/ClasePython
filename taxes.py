print( "\t\t\t" "╔", 75*"═", "╗" )
print( "\t\t\t\t\t Calcul du montant total toutes taxes comprises")
print( "\t\t\t" "╚", 75*"═", "╝" )


article1 = float(input("\t\t\t\t\t Saisir le prix de l'article 1 : "))
article2 = float(input("\t\t\t\t\t Saisir le prix de l'article 2 : "))
article3 = float(input("\t\t\t\t\t Saisir le prix de l'article 3 : "))
print("\n")

print("Hola a Todos!!!")

shipping = 30
tps = 0.05
tvq = 0.09975
adition_article = article1 + article2 + article3


if adition_article < 200:
    print("\t\t\t\t\t Le montant sans taxes est :\t", adition_article, "$")
    print("\t\t\t\t\t Plus shipping :\t\t", shipping, "$")
    montant_sans_taxes = round(adition_article + shipping,2)
    mtps = round(montant_sans_taxes * tps, 2)
    mtvq = round(montant_sans_taxes * tvq, 2)
    Total = round(montant_sans_taxes + mtps + mtvq, 2)
    print("\t\t\t\t\t Le subtotal est:\t\t" , montant_sans_taxes, "$")
    print("\t\t\t\t\t La taxe fédérale est :\t\t", mtps, "$")
    print("\t\t\t\t\t La taxe provinciale est :\t", mtvq, "$")
    print("\t\t\t\t\t", 40*"-" )
    print("\t\t\t\t\t Le montant à payer est :\t", Total, "$")
    print("\t\t\t\t\t", 40*"-" )    
    print( "\t\t\t" "╔", 75*"═", "╗" )
    print("\t\t\t\t\t Nous sommes heureux de vous avoir comme client!!!")
    print( "\t\t\t" "╚", 75*"═", "╝" )
elif adition_article >=500  and adition_article <1000:
    print("\t\t\t\t\t Le montant sans taxes est :\t", adition_article, "$") 
    rebais5 = round(adition_article*0.05, 2)
    subtotal = round(adition_article - rebais5, 2)
    mtps = round(subtotal * tps, 2)
    mtvq = round(subtotal * tvq, 2)
    Total = round(subtotal + mtps + mtvq,2)
    print("\t\t\t\t\t Rebais de 5% :\t\t\t", rebais5, "$")
    print("\t\t\t\t\t Le subtotal est :\t\t", subtotal, "$")
    print("\t\t\t\t\t La taxe fédérale est :\t\t", mtps, "$")
    print("\t\t\t\t\t La taxe provinciale est :\t", mtvq, "$")
    print("\t\t\t\t\t", 40*"-" )
    print("\t\t\t\t\t Le montant à payer est :\t", Total, "$" )
    print("\t\t\t\t\t", 40*"-" )
    print("\t\t\t\t\t Vous avez beneficié d'un rabais de :", rebais5, "$")
    print( "\t\t\t" "╔", 75*"═", "╗" )
    print("\t\t\t\t Nous sommes heureux de vous avoir comme client!!!")
    print( "\t\t\t" "╚", 75*"═", "╝" )
elif adition_article >=1000:
    print("\t\t\t\t\t Le montant sans taxes est :\t", adition_article, "S")
    rebais10 = round(adition_article*0.10, 2)
    montant_sans_taxes = round(adition_article,2)
    subtotal = round(montant_sans_taxes - rebais10, 2)
    mtps = round(subtotal * tps, 2)
    mtvq = round(subtotal * tvq, 2)
    Total = round(subtotal + mtps + mtvq, 2)
    print("\t\t\t\t\t Rebais de 10%", rebais10, "S")
    print("\t\t\t\t\t Le subtotal est:\t\t", subtotal, "S")
    print("\t\t\t\t\t La taxe fédérale est :\t\t", mtps, "S")
    print("\t\t\t\t\t La taxe provinciale est :\t", mtvq, "S")
    print("\t\t\t\t\t Le montant à payer est :\t", Total, "S" )
    print("\t\t\t\t\t", 40*"-" )
    print("\t\t\t\t\t Vous avez beneficié d'un rabais de :", rebais10, "$")
    print( "\t\t\t" "╔", 75*"═", "╗" )
    print("\t\t\t\t\t Nous sommes heureux de vous avoir comme client!!!")
    print( "\t\t\t" "╚", 75*"═", "╝" )
else:
    print("\t\t\t\t\t Le montant sans taxes est :\t", adition_article, "S")
    montant_sans_taxes = adition_article
    mtps = round(montant_sans_taxes * tps, 2)
    mtvq = round(montant_sans_taxes * tvq, 2)
    Total = round(montant_sans_taxes + mtps + mtvq, 2)
    print("\t\t\t\t\t La taxe fédérale est :\t\t", mtps, "S")
    print("\t\t\t\t\t La taxe provinciale est :\t", mtvq, "S")
    print("\t\t\t\t\t Le montant à payer est :\t", Total, "S" )
    print( "\t\t\t" "╔", 75*"═", "╗" )
    print("\t\t\t\t\t Nous sommes heureux de vous avoir comme client!!!")
    print( "\t\t\t" "╚", 75*"═", "╝" )
