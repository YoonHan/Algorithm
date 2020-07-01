from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_songs = defaultdict(list)  # {genre: [(id, plays), ...]}
    genre_plays = defaultdict(int)  # {genre: total played times}
    for id in range(len(genres)):
        genre = genres[id]
        play = plays[id]
        genre_songs[genre].append((id, play))
        genre_plays[genre] += play

    # sort decending order
    genre_plays = sorted(genre_plays.items(),
                         key=lambda pair: pair[1], reverse=True)
    for genre, pairs in genre_songs.items():
        genre_songs[genre] = sorted(
            pairs, key=lambda pair: (pair[1], -pair[0]), reverse=True)
    # pick songs
    for genre, total_play in genre_plays:
        songs = genre_songs[genre][:2]
        for song in songs:
            answer.append(song[0])

    return answer
