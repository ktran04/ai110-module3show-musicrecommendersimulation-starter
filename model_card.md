# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

This recommender suggests songs that seem to match a user's genre, mood, and energy preferences. It is for classroom exploration, not real users. It assumes the user can describe their taste with a few simple labels.

---

## 3. How the Model Works  

The model looks at genre, mood, and energy. It gives the biggest score boost for a genre match, a smaller boost for a mood match, and extra points when the song energy is close to the user's target energy. Then it sorts the songs from highest score to lowest score. This is a simple content-based system, not a learning model.

---

## 4. Data  

The dataset has 10 songs. It includes pop, lofi, rock, ambient, jazz, synthwave, and indie pop. It also includes moods like happy, chill, intense, relaxed, moody, and focused. The catalog is small, so some taste combinations are missing and some genres have more examples than others.

---

## 5. Strengths  

The system works best for clear profiles like happy pop, chill lofi, or intense rock. It often matches intuition when the genre and mood are both obvious. It also gives reasonable results when energy is the main thing the user cares about.

---

## 6. Limitations and Bias 

One weakness is that the recommender can create a small filter bubble around exact genre matches. Genre gets the biggest bonus, so users with mixed tastes may be pushed toward the same few songs. The energy gap can also flatten differences between songs, because a close energy match can keep a mismatched song near the top. In my experiments, unusual profiles sometimes returned calm or off-genre songs just because they were the closest energy match in a tiny catalog.

---

## 7. Evaluation  

I tested several profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Sad High Energy, Mismatch Hunter, and Everything Conflicts. I compared how the top songs changed when I changed genre, mood, or energy. The biggest surprise was that Gym Hero kept showing up near the top because it has pop genre and high energy. That makes sense in this system because genre and energy are the strongest signals. It also showed me that strange profiles can still pull up songs that are only a partial fit.

High-Energy Pop and Deep Intense Rock behaved as expected because they matched the strongest signals in the songs. Chill Lofi shifted toward softer lofi tracks because the user wanted low energy. The weird profiles were less accurate, but they showed how the model falls back on energy when the rest of the profile does not match well.

---

## 8. Future Work  

I would add more song features like tempo, valence, and acousticness to make the score more detailed. I would also lower the genre weight a little so one genre does not dominate as much. I would add a diversity rule so the top five songs do not all feel too similar.

---

## 9. Personal Reflection  

**Biggest learning moment:**
I think my biggest learning moment was seeing how much a tiny scoring rule can shape the whole recommender. Changing one weight or removing one feature can move songs up and down a lot. That gives the system more transparency into why it does what it does rather than just 1 factor alone. It is up to the designer to decide what moves the needle the most.

**How AI tools helped:**
AI tools helped me move faster when I needed help with wording, code structure, and debugging ideas. I still had to double-check the output because the tool could sound very confident even when the reasoning needed a second look. I learned to trust it for quick help and syntax, but not to skip my own review.

**What surprised me:**
I was surprised that such a simple algorithm could still feel like a real recommendation system. Even without machine learning, the outputs started to look meaningful because the songs matched the user's genre, mood, and energy. That made the results feel familiar in a way that was easy to understand.

**What I would try next:**
If I extended this project, I would add more song features and try a more balanced scoring system. I would also make the top results more diverse so the same song does not keep showing up for different profiles. After that, I would test more unusual users to see where the recommender breaks down.
