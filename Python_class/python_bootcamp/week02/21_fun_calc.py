def fun_calc(num1: int, num2: int, operator: str):
    tmp = str(num1)+operator+str(num2)
    product = eval(tmp)
    process = tmp+'='+str(product)
    return product, process
product, process = fun_calc(50, 2, '$')
print(f'Product: {product}')
print(f'Process: {process}')



