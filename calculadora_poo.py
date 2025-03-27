class Calculadora:
    def __init__(self, a, b):
        self._resultado = 0
        self.a = a
        self.b = b
        self.operacion = ""

    def sumar(self):
        self.operacion = "suma"
        self._resultado = self.a + self.b
        return self._mostrar_operacion()

    def restar(self):
        self.operacion = "resta"
        self._resultado = self.a - self.b
        return self._mostrar_operacion()

    def multiplicar(self):
        self.operacion = "multiplicación"
        self._resultado = self.a * self.b
        return self._mostrar_operacion()

    def dividir(self):
        if self.b == 0:
            return "Error: no se puede dividir por cero"
        self.operacion = "división"
        self._resultado = self.a / self.b
        return self._mostrar_operacion()

    def _mostrar_operacion(self):
        return f"{self.operacion}: {self.a} y {self.b} = {self._resultado}"

calculadora_1 = Calculadora(15, 5)

print(calculadora_1.sumar())
print(calculadora_1.restar())
print(calculadora_1.multiplicar())
print(calculadora_1.dividir())

calculadora_2 = Calculadora(10, 0)
print(calculadora_2.dividir())