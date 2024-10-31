import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_rectangle_1(self):
        p1 = data.Point(4, 4)
        p2 = data.Point(9,9 )
        expected_rectangle = data.Rectangle(data.Point(4, 9), data.Point(9, 4))
        self.assertEqual(hw2.create_rectangle(p1, p2), expected_rectangle)

    def test_rectangle_equal(self):
        p1 = data.Point(7, 7)
        p2 = data.Point(7, 7)
        expected_rectangle = data.Rectangle(data.Point(7, 7), data.Point(7, 7))
        self.assertEqual(hw2.create_rectangle(p1, p2), expected_rectangle)

    # Part 2

    def test_duration_shorter(self):
        duration1 = data.Duration(1, 45)
        duration2 = data.Duration(3, 10)
        self.assertTrue(hw2.shorter_duration_than(duration1, duration2))

    def test_duration_longer(self):
        d1 = data.Duration(2, 30)
        d2 = data.Duration(1, 30)
        self.assertFalse(hw2.shorter_duration_than(d1, d2))

    # Part 3
    def test_song_1(self):
        song_1 = data.Song("Adele", "Hello", data.Duration(3,0 ))
        song_2 = data.Song("Drake", "Hot Line Bling", data.Duration(2, 45))
        songs = [song_1, song_2]
        max_duration = data.Duration(3, 30)
        self.assertEqual(hw2.song_shorter_than(songs, max_duration), [song_1, song_2])

    def test_song_2_none(self):
        song1 = data.Song("Drake", "Massive", data.Duration(3, 30))
        songs = [song1]
        max_duration = data.Duration(3, 0)
        self.assertEqual(hw2.song_shorter_than(songs, max_duration), [])

    # Part 4
    def test_running_time_1(self):
        song1 = data.Song("artist1", "title1", data.Duration(2, 0))
        song2 = data.Song("artist2", "title2", data.Duration(1, 30))
        song3 = data.Song("artist3", "title3", data.Duration(3, 30))
        songs = [song1, song2, song3]
        playlist = [0, 2, 1]
        self.assertEqual(hw2.running_time(songs, playlist), data.Duration(7, 0))

    def test_running_time_empty(self):
        song1 = data.Song("artist1", "title1", data.Duration(2, 0))
        song2 = data.Song("artist2", "title2", data.Duration(2, 0))
        songs = [song1, song2]
        playlist = []
        self.assertEqual(hw2.running_time(songs, playlist), data.Duration(0, 0))


    # Part 5
    def test_route_1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertTrue(hw2.validate_route(city_links, route))

    def test_route_single_city(self):
        city_links = [
            ['san luis obispo', 'atascadero'],
        ]
        route = ['san luis obispo']
        self.assertTrue(hw2.validate_route(city_links, route))

    # Part 6
    def test_repetition_1(self):
        self.assertEqual(hw2.longest_repetition([1, 1, 2, 2, 3, 3, 3, 3, 4, 4]), 4)

    def test_repetition_2(self):
        self.assertEqual(hw2.longest_repetition([1, 2, 3]), 0)






if __name__ == '__main__':
    unittest.main()
