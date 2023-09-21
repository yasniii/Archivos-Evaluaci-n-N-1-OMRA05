aclNum = int(input("¿Cúal es el número IPV4 ACL?: "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es una ACL IPV4 Estándar.")
elif aclNum >= 100 and aclNum <= 199:
    print("Este es una ACL IPV4 Extendida.")
else:
    print("NO corresponde a una lista de acceso conocida.")