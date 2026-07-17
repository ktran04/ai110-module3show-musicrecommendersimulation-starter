from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.recommender import Song, UserProfile, Recommender, load_songs


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_score_song_returns_score_and_reasons():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
    }

    score, reasons = load_songs.__globals__["score_song"](user_prefs, song)

    assert score == 4.0
    assert any("genre match" in reason for reason in reasons)
    assert any("mood match" in reason for reason in reasons)


def test_load_songs_converts_numeric_values_to_numbers():
    csv_path = Path("data/songs.csv")
    songs = load_songs(str(csv_path))

    assert len(songs) == 10
    assert isinstance(songs[0]["energy"], float)
    assert isinstance(songs[0]["tempo_bpm"], int)
    assert isinstance(songs[0]["acousticness"], float)
