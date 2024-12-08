import pytest
from src.gravity_flip import GravityFlip

def test_gravityToggle():
    gf = GravityFlip()
    assert gf.toggle_gravity() == "down"
    assert gf.toggle_gravity() == "up"

def test_gravityApplied():
    gf = GravityFlip()
    position = {"x": 0, "y": 0}
    assert gf.apply_gravity(position) == {"x": 0, "y": 1}

    gf.toggle_gravity()
    assert gf.apply_gravity(position) == {"x": 0, "y": 0}
