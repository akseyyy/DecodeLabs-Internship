import pandas as pd
movies = pd.read_csv("movies.csv")

print("=" * 40)
print("      🎬 MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)
print("\nAvailable Genres:\n")

genres = movies["genre"].dropna().unique()

for i, genre in enumerate(sorted(genres), start=1):
    print(f"{i}. {genre}")

genre = input("\nEnter your favorite genre: ")

rating = float(input("Enter minimum rating (0-10): "))


recommended = movies[
    (movies["genre"].str.contains(genre, case=False, na=False)) &
    (movies["score"] >= rating)
]


print("\nSearching for recommendations...")
print("-" * 40)

if recommended.empty:
    print("❌ No movies found.")

else:
    print("\n🎥 Recommended Movies\n")

    for index, row in recommended.head(10).iterrows():
        print(f"🎬 Movie    : {row['name']}")
        print(f"⭐ Rating   : {row['score']}")
        print(f"📅 Year     : {row['year']}")
        print(f"🎥 Director : {row['director']}")
        print(f"✍️ Writer   : {row['writer']}")
        print(f"🌍 Country  : {row['country']}")
        print()

print("-" * 40)
print("\nThankyou for using Movie Recommendation System\n")

