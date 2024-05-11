from __future__ import annotations

from mangainfo import Resolution


def test_resolution() -> None:
    res = Resolution(width=2000, height=3000)
    assert res.as_str() == "2000x3000"
    assert res.as_tuple() == (2000, 3000)
    assert res.is_landscape() is False
    assert res.is_portrait() is True
