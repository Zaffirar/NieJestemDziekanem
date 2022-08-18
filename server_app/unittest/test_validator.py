from ..validator import Validator

def test_Validator_has_only_one_instance():
    V1 = Validator()
    V2 = Validator()
    assert id(V1) == id(V2)
