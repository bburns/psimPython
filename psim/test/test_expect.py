from addict import Dict
import expect

def test_foo():
    params = Dict()
    expect.initialize(params)
    assert params.expected.pressure == 0
