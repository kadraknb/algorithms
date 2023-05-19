from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("12345", 2) == "543_21"
    assert encrypt_message("teste", 3) == "321_54"
    assert encrypt_message("teste", 6) == "54321"

    with pytest.raises(TypeError):
        encrypt_message("12345", "string")
