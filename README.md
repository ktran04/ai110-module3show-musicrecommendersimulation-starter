# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

In real-world recommender systems, platforms predict what you will like next by combining signals from your past choices with patterns from similar users and item attributes. My version will focus on a simple content-based approach: it will compare each song’s features against a user profile, reward close matches, and rank songs by the total score so the closest matches appear first.

This simulation will use these specific features:

- `Song`: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
- `UserProfile`: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

Algorithm Recipe:

- `+2.0` points for a genre match
- `+1.0` point for a mood match
- Energy similarity points based on how close the song’s `energy` is to the user’s `target_energy`
- Optional tie-breakers can use other features like `acousticness`, but only after the core score is calculated

Data flow:

```mermaid
flowchart LR
  A[Input: User Prefs] --> B[Process: Score each song in songs.csv]
  B --> C[Output: Rank songs by total score]
  C --> D[Top K Recommendations]
```

This design gives genre the strongest exact-match boost, mood a smaller but still meaningful boost, and energy a flexible similarity score so songs can rank well even when they are not exact matches. Mood matters less than genre in the raw points, but it still helps capture the user’s vibe when the genre is broad or only loosely related.

Possible biases:

- The system may over-prioritize genre and miss songs that better match the user’s mood.
- Exact-match scoring can create ties when many songs share the same labels.
- With a small catalog, one unusual or mislabeled song can shift the ranking more than it would in a larger dataset.
- If energy similarity is weighted too heavily, the recommender may favor songs that feel similar but do not match the user’s style.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Below are real terminal outputs from running the recommender on several regular and edge-case profiles.

### High-Energy Pop

```text
Loaded songs: 10

Top recommendations (High-Energy Pop)
------------------------------------------------------------------------
profile: genre=pop, mood=happy, energy=0.9
1. Sunrise City
  Score  : 3.92
  Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+0.92)
------------------------------------------------------------------------
2. Gym Hero
  Score  : 2.97
  Reasons: genre match (+2.0); mood mismatch (intense); energy similarity (+0.97)
------------------------------------------------------------------------
3. Rooftop Lights
  Score  : 1.86
  Reasons: genre mismatch (indie pop); mood match (+1.0); energy similarity (+0.86)
------------------------------------------------------------------------
4. Storm Runner
  Score  : 0.99
  Reasons: genre mismatch (rock); mood mismatch (intense); energy similarity (+0.99)
------------------------------------------------------------------------
5. Night Drive Loop
  Score  : 0.85
  Reasons: genre mismatch (synthwave); mood mismatch (moody); energy similarity (+0.85)
------------------------------------------------------------------------
```

### Chill Lofi

```text
Top recommendations (Chill Lofi)
------------------------------------------------------------------------
profile: genre=lofi, mood=calm, energy=0.2
1. Library Rain
  Score  : 2.85
  Reasons: genre match (+2.0); mood mismatch (chill); energy similarity (+0.85)
------------------------------------------------------------------------
2. Focus Flow
  Score  : 2.80
  Reasons: genre match (+2.0); mood mismatch (focused); energy similarity (+0.80)
------------------------------------------------------------------------
3. Midnight Coding
  Score  : 2.78
  Reasons: genre match (+2.0); mood mismatch (chill); energy similarity (+0.78)
------------------------------------------------------------------------
4. Spacewalk Thoughts
  Score  : 0.92
  Reasons: genre mismatch (ambient); mood mismatch (chill); energy similarity (+0.92)
------------------------------------------------------------------------
5. Coffee Shop Stories
  Score  : 0.83
  Reasons: genre mismatch (jazz); mood mismatch (relaxed); energy similarity (+0.83)
------------------------------------------------------------------------
```

### Deep Intense Rock

```text
Top recommendations (Deep Intense Rock)
------------------------------------------------------------------------
profile: genre=rock, mood=intense, energy=0.95
1. Storm Runner
  Score  : 3.96
  Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+0.96)
------------------------------------------------------------------------
2. Gym Hero
  Score  : 1.98
  Reasons: genre mismatch (pop); mood match (+1.0); energy similarity (+0.98)
------------------------------------------------------------------------
3. Sunrise City
  Score  : 0.87
  Reasons: genre mismatch (pop); mood mismatch (happy); energy similarity (+0.87)
------------------------------------------------------------------------
4. Rooftop Lights
  Score  : 0.81
  Reasons: genre mismatch (indie pop); mood mismatch (happy); energy similarity (+0.81)
------------------------------------------------------------------------
5. Night Drive Loop
  Score  : 0.80
  Reasons: genre mismatch (synthwave); mood mismatch (moody); energy similarity (+0.80)
------------------------------------------------------------------------
```

### Adversarial: Sad High Energy

```text
Top recommendations (Adversarial: Sad High Energy)
------------------------------------------------------------------------
profile: genre=pop, mood=sad, energy=0.9
1. Gym Hero
  Score  : 2.97
  Reasons: genre match (+2.0); mood mismatch (intense); energy similarity (+0.97)
------------------------------------------------------------------------
2. Sunrise City
  Score  : 2.92
  Reasons: genre match (+2.0); mood mismatch (happy); energy similarity (+0.92)
------------------------------------------------------------------------
3. Storm Runner
  Score  : 0.99
  Reasons: genre mismatch (rock); mood mismatch (intense); energy similarity (+0.99)
------------------------------------------------------------------------
4. Rooftop Lights
  Score  : 0.86
  Reasons: genre mismatch (indie pop); mood mismatch (happy); energy similarity (+0.86)
------------------------------------------------------------------------
5. Night Drive Loop
  Score  : 0.85
  Reasons: genre mismatch (synthwave); mood mismatch (moody); energy similarity (+0.85)
------------------------------------------------------------------------
```

### Adversarial: Mismatch Hunter

```text
Top recommendations (Adversarial: Mismatch Hunter)
------------------------------------------------------------------------
profile: genre=classical, mood=party, energy=0.1
1. Spacewalk Thoughts
  Score  : 0.82
  Reasons: genre mismatch (ambient); mood mismatch (chill); energy similarity (+0.82)
------------------------------------------------------------------------
2. Library Rain
  Score  : 0.75
  Reasons: genre mismatch (lofi); mood mismatch (chill); energy similarity (+0.75)
------------------------------------------------------------------------
3. Coffee Shop Stories
  Score  : 0.73
  Reasons: genre mismatch (jazz); mood mismatch (relaxed); energy similarity (+0.73)
------------------------------------------------------------------------
4. Focus Flow
  Score  : 0.70
  Reasons: genre mismatch (lofi); mood mismatch (focused); energy similarity (+0.70)
------------------------------------------------------------------------
5. Midnight Coding
  Score  : 0.68
  Reasons: genre mismatch (lofi); mood mismatch (chill); energy similarity (+0.68)
------------------------------------------------------------------------
```

### Adversarial: Everything Conflicts

```text
Top recommendations (Adversarial: Everything Conflicts)
------------------------------------------------------------------------
profile: genre=jazz, mood=intense, energy=0.99
1. Coffee Shop Stories
  Score  : 2.38
  Reasons: genre match (+2.0); mood mismatch (relaxed); energy similarity (+0.38)
------------------------------------------------------------------------
2. Gym Hero
  Score  : 1.94
  Reasons: genre mismatch (pop); mood match (+1.0); energy similarity (+0.94)
------------------------------------------------------------------------
3. Storm Runner
  Score  : 1.92
  Reasons: genre mismatch (rock); mood match (+1.0); energy similarity (+0.92)
------------------------------------------------------------------------
4. Sunrise City
  Score  : 0.83
  Reasons: genre mismatch (pop); mood mismatch (happy); energy similarity (+0.83)
------------------------------------------------------------------------
5. Rooftop Lights
  Score  : 0.77
  Reasons: genre mismatch (indie pop); mood mismatch (happy); energy similarity (+0.77)
------------------------------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



