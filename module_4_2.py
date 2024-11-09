def test_function():
    def inner_function():
        print('Я в области видимости функци test_function')
    inner_function()

inner_function()