def square_number(number):
    return number **2
#print('The Square of a Given number {0} = {1}'.format(number,square))
def test_square_number():
      assert square_number(2) == 4
      assert square_number(8) == 64
      assert square_number(10) == 100
print("YOUR CODE IS CORRECT!")
test_square_number()
