from udemy_section_four.aula_113.classes.poupanca import ContaPoupanca
from udemy_section_four.aula_113.classes.conta_corrente import ContaCorrente

cp = ContaPoupanca(3070, 461687, 1212.50)

try:
    cp.depositar('R$100')
except ValueError as e:
    print(e)

cp.depositar(100)
cp.sacar(200)

print('#' * 20)

cc = ContaCorrente(14109, 331066, 22)
cc.depositar(100)
cc.sacar(122 + cc.limite)
