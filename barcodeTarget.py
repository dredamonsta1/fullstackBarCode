from barcode import Code128

data1 = "01S100H33"

my_code = Code128(data1)

my_code.save("myAlphaBarCode")