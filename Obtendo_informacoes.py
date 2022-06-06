import wmi

c = wmi.WMI()
system = c.Win32_ComputerSystem()[0]

print(f'Marca: {system.Manufacturer}')
print(f'Modelo: {system.Model}')
print(f'Usuario: {system.Name}')
print(f'Qtd de cpu: {system.NumberOfProcessors}')
print(f'Arquitetura: {system.SystemType}')
print(f'Familia: {system.SystemFamily}')