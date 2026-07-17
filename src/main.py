"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def _print_profile_recommendations(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nTop recommendations ({profile_name})")
    print("-" * 72)
    print(
        f"profile: genre={user_prefs.get('genre')}, mood={user_prefs.get('mood')}, "
        f"energy={user_prefs.get('energy')}"
    )
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']}")
        print(f"   Score  : {score:.2f}")
        print(f"   Reasons: {explanation}")
        print("-" * 72)


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.9}),
        ("Chill Lofi", {"genre": "lofi", "mood": "calm", "energy": 0.2}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.95}),
        ("Adversarial: Sad High Energy", {"genre": "pop", "mood": "sad", "energy": 0.9}),
        ("Adversarial: Mismatch Hunter", {"genre": "classical", "mood": "party", "energy": 0.1}),
        ("Adversarial: Everything Conflicts", {"genre": "jazz", "mood": "intense", "energy": 0.99}),
    ]

    for profile_name, user_prefs in profiles:
        _print_profile_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
