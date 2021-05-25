'''Product Series multiply with factorial 
Product_series(5,5)
Ex 5  * 1 = 5
   5  * 2 = 10
   10 * 3 = 30
   30 * 4 = 120
   120* 5 = 600''' 
def Product_series(n,start): 
    for i in range(1, n+1):
        product = start * i
        print(f'{start} of {i} is {product}')
        start = product
    return

if __name__ == "__main__":
    Product_series(5,5)
