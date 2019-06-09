import main


class TestClass:
    def test_1(self):
        # main.input = lambda: 'some_input'
        output = main.main()
        assert output == 'Hello world'

    def test_2(self):
        # main.input = lambda: 'some_other_input'
        output = main.main()
        assert output == 'Hello world'

    def test_3(self):
        # main.input = lambda: 'some_other_input'
        output = main.main()
        assert output == 'Hello world'

    def teardown_method(self, method):
        main.input = input
