class TestClass:
    def test_one(self):
        x = 'Lando'
        assert 'a' in x

    def test_two(self):
        x = 'Hello'
        assert hasattr(x, 'check')