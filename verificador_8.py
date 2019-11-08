#verificador 8: volumen de un prisma
volumen_prisma, base_prisma, altura_prisma=0.0, 0.0, 0.0
#asignacion de valores
base_prisma=int(input("mostrar la base del prisma:"))
altura_prisma=int(input("mostrar la altura del prisma:"))
#calculo
volumen_prisma=base_prisma*altura_prisma
verificador=(volumen_prisma<=58)
#mostrar valores
print("base del prisma:",base_prisma)
print("altura del prisma:",altura_prisma)
print("volumen del prisma:",volumen_prisma)
print("volumen del prisma<=58",verificador)
