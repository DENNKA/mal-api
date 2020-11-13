import unittest

from mal import MangaSearch


class TestMangaSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manga_search = MangaSearch("monster")

    def test_manga_search(self):
        self.assertEqual(self.manga_search.results[0].mal_id, 1)
        self.assertEqual(
            self.manga_search.results[0].url,
            "https://myanimelist.net/manga/1/Monster",
        )
        self.assertEqual(
            self.manga_search.results[0].image_url,
            "https://cdn.myanimelist.net/r/50x70/images/manga/3/54525.jpg?s=c660994ac8b"
            "a790d9e6bb2400f7c73cd",
        )
        self.assertEqual(self.manga_search.results[0].title, "Monster")
        self.assertEqual(
            self.manga_search.results[0].synopsis,
            "Kenzou Tenma, a renowned Japanese neurosurgeon working in post-war "
            "Germany, faces a difficult choice: to operate on Johan Liebert, an orphan "
            "boy on the verge of death, or on the mayor of Düsseldorf. I...",
        )
        self.assertEqual(self.manga_search.results[0].type, "Manga")
        self.assertEqual(self.manga_search.results[0].volumes, 18)
        self.assertIsInstance(self.manga_search.results[0].score, float)


if __name__ == "__main__":
    unittest.main()
