class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        # ถ้าเป็นลบทั้งคู่จะเป็น Flase
        negative_result = (a < 0) ^ (b < 0)
        # ทำให้เป็นค่าสัมบูรณ์เพื่อง่ายต่อการคำนวณ
        a, b = abs(a), abs(b)
        # ทำการบวกค่าเรื่อยๆจำนวนครั้งเท่ากับ b 
        for i in range(b):
            x = a 
            result = self.add(result, x )
        # ทำการเปลี่ยนเครื่องหมาย result เมื่อ negative_result เมื่อมีค่าเป้น True 
        if negative_result:
            result = -result
        return result

    def divide(self, a, b):
        result = 0
        negative_result_divide = (a < 0) ^ (b < 0) 
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a , b)
            result += 1
        if negative_result_divide:
            result = -result
        return result
    
    def modulo(self, a, b):
        negative_result_modulo  = (a < 0) ^ (b < 0) 
        a, b = abs(a), abs(b)
        while b < a:
            a = a - b
        if negative_result_modulo :
            a = -a
        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(-4 , -20))
    print("Example: division: ", calc.divide(-14, 2))
    print("Example: modulo: ", calc.modulo(-35, 3))
