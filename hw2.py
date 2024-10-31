import data
from typing import List, Optional
# Write your functions for each part in the space below.

# Part 1
# Obtain a rectangle with top left and bottom right points.
# input: point1 and point2 as a Point object
# output: Rectangle with top left and bottom right points defined
def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    top_left_x = min(point1.x, point2.x)
    top_left_y = max(point1.y, point2.y)
    bottom_right_x = max(point1.x, point2.x)
    bottom_right_y = min(point1.y, point2.y)

    top_left = data.Point(top_left_x, top_left_y)
    bottom_right = data.Point(bottom_right_x, bottom_right_y)

    return data.Rectangle(top_left, bottom_right)

# Part 2
# Compare a duration to another duration
# input: d1, which is the first duration to compare, then d2, which is the second one
# output: True if d1 is shorter than d2, False vice versa
def shorter_duration_than(d1: data.Duration, d2: data.Duration) -> bool:
    d1_total_seconds = d1.minutes * 60 + d1.seconds
    d2_total_seconds = d2.minutes * 60 + d2.seconds
    return d1_total_seconds < d2_total_seconds

# Part 3
# Returns a list of all songs in the input list with duration less than the provided duration parameter.
# input: a list of songs and a specific maximum duration of the song.
# output: a list songs with a duration shorter than max_duration
def song_shorter_than(songs: List[data.Song], max_duration: data.Duration) -> List[data.Song]:
    def time(duration: data.Duration) -> int:
        return duration.minutes * 60 + duration.seconds

    return [song for song in songs if time(song.duration) < time(max_duration)]

# Part 4
# Gets the duration of a group of songs based on the selected songs
# Input: A list of songs with a duration, and a list of songs to include in the playlist
# Output: the total duration of the playlist
def running_time(songs: List[data.Song], playlist: List[int]) -> data.Duration:
    total_seconds = 0
    for song_index in playlist:
        if 0 <= song_index < len(songs):
            song_duration = songs[song_index].duration
            total_seconds += song_duration.minutes * 60 + song_duration.seconds
    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    return data.Duration(total_minutes, remaining_seconds)

# Part 5
# Validates if there is a route between cities
# Input: city_links (A list of pairs representing direct links between cities). A list representing the route.
# Output: returns a bool, true if there is a connection between the cities, false vice versa.
def validate_route(city_links: List[List[str]], route: List[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]
        link_exists = False
        for link in city_links:
            if city1 in link and city2 in link:
                link_exists = True
                break
        if not link_exists:
            return False

    return True

# Part 6
# Find the starting index of the longest consecutive repetition
# Input: A list of integers
# Output: the starting index of the longest consecutive repetition
def longest_repetition(numbers: List[int]) -> Optional[int]:
    if not numbers:
        return None
    longest_count = 0
    longest_index = 0
    current_count = 1
    current_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > longest_count:
                longest_count = current_count
                longest_index = current_index
            current_count = 1
            current_index = i
    if current_count > longest_count:
        longest_index = current_index

    return longest_index
