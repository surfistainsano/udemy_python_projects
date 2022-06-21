from udemy_section_four.aula_113.classes.poupanca import ContaPoupanca
from udemy_section_four.aula_113.classes.conta_corrente import ContaCorrente

cp = ContaPoupanca(3070, 461687, 1212.50)
cp.depositar(100)
cp.sacar(200)

print('#' * 20)

cc = ContaCorrente(14109, 331066, 220, 200)
cc.depositar(100)
cc.sacar(400)
