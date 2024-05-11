from __future__ import annotations

from mangainfo import MangaParser


def test_full_scan() -> None:
    manga = MangaParser("tests/test_data/Some Manga v01 (2023) (Digital).cbz").full_scan()

    assert manga.name.as_posix() == "Some Manga v01 (2023) (Digital).cbz"
    assert manga.extension == "cbz"
    assert manga.format == "ZIP"
    assert manga.size == 8043
    assert manga.page_count == 10
    assert len(manga.pages) == 10
    assert manga.largest_page().name.as_posix() == "largest.png"
    assert manga.smallest_page().name.as_posix() == "smallest.png"
    assert manga.median_page().name.as_posix() in (
        "p08.png",
        "p07.png",
    )  # This oddly returns p08 on windows and macos but p07 on linux
    assert len(manga.unique_resolutions()) == 3
    assert manga.average_page_size() == 674
    assert len(manga.mediainfo().splitlines()) in (43, 46)  # Same issue here? I'm completely lost here
