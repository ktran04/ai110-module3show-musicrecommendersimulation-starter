from __future__ import annotations

import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


def _build_user_pref_dict(user_prefs: Dict | UserProfile) -> Dict:
    """Normalize user preferences from either a dict or a UserProfile dataclass."""
    if isinstance(user_prefs, UserProfile):
        return {
            "genre": user_prefs.favorite_genre,
            "mood": user_prefs.favorite_mood,
            "energy": user_prefs.target_energy,
        }
    return user_prefs


def _build_song_dict(song: Dict | Song) -> Dict:
    """Normalize a song from either a dict or a Song dataclass."""
    if isinstance(song, Song):
        return {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
    return song

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by score for a user profile."""
        ranked_songs = sorted(
            ((score_song(user, song)[0], song) for song in self.songs),
            key=lambda item: (-item[0], item[1].id),
        )
        return [song for _, song in ranked_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Summarize why a song scored as a recommendation for the user."""
        _, reasons = score_song(user, song)
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file into typed dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(float(row["tempo_bpm"])),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted score and explanation reasons for one song."""
    prefs = _build_user_pref_dict(user_prefs)
    song_data = _build_song_dict(song)

    score = 0.0
    reasons: List[str] = []

    if prefs.get("genre") and song_data.get("genre") == prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")
    else:
        reasons.append(f"genre mismatch ({song_data.get('genre')})")

    if prefs.get("mood") and song_data.get("mood") == prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")
    else:
        reasons.append(f"mood mismatch ({song_data.get('mood')})")

    target_energy = prefs.get("energy")
    song_energy = song_data.get("energy")
    if target_energy is not None and song_energy is not None:
        energy_difference = abs(float(song_energy) - float(target_energy))
        energy_similarity = max(0.0, 1.0 - energy_difference)
        score += energy_similarity
        if energy_difference == 0:
            reasons.append("energy match (+1.0)")
        else:
            reasons.append(f"energy similarity (+{energy_similarity:.2f})")

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank all songs by score and return the top-k with explanations."""
    ranked_songs = sorted(
        (
            (song, score, "; ".join(reasons))
            for song in songs
            for score, reasons in [score_song(user_prefs, song)]
        ),
        key=lambda item: (-item[1], item[0].get("id", 0)),
    )
    return ranked_songs[:k]
