import subprocess

comando = subprocess.run(
    ['ping','127.0.0.1'],
    capture_output=True,
    text=True
)

#O replace foi usado como demostração, a saída está na variavel e pode ser manipulada
saida = (comando.stdout).replace("<"," menor que : ")
print(saida)