import main


class TestClass:
    def test_1(self):
        main.input = lambda: '1'
        output = main.main()
        assert output == 'Weird'

    def test_2(self):
        main.input = lambda: '4'
        output = main.main()
        assert output == 'Not Weird'

    def test_3(self):
        main.input = lambda: '11'
        output = main.main()
        assert output == 'Weird'

    def teardown_method(self, method):
        main.input = input
