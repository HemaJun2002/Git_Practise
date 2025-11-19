def test_sum(read_file):  # <-- use fixture as a parameter
    #data = read_file      # pytest automatically calls the fixture
    assert sum(read_file) == 15
