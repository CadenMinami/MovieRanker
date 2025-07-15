#MovieRanker.py
#Author: Caden Minami
#Date: 2025/7/14

import os
import json
#Creates a Json file to store the movie rankings
MOVIE_RANKING_FILE = 'moving_ranking.json'


def load_movie_rankings():
    if not os.path.exists(MOVIE_RANKING_FILE):
        return []
    with open(MOVIE_RANKING_FILE, 'r') as f:
        return json.load(f) 
    
def add_movie_ranking(movie_name, rank):

    rankings = load_movie_rankings()
    for movie in rankings:
        if movie['rank'] >= rank:
            movie['rank'] += 1
    rankings.append({'movie_name': movie_name, 'rank': rank})

    with open(MOVIE_RANKING_FILE, 'w') as f:
        json.dump(rankings, f , indent = 2)
def view_movie_rankings():
    rankings = load_movie_rankings()
    if not rankings:
        print("Nothing is ranked yet.")
    else:
        print("Current movie standings:")
        for movie in sorted(rankings, key=lambda x: x['rank']):
            print(f"{movie['rank']}. {movie['movie_name']}")

def main():
    while True:
        print("-----------Welcome to the Movie Ranker!--------- \n what would you like to do?\n1. Add Movie\n2. View Rankings\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            userMovie = input("Enter the movie name: ")
            userRank = int(input("Enter the movie rank: "))

            if userRank < 1 or userRank > len(load_movie_rankings()) + 1: 
                print("Invalid rank. Please enter a valid rank.")
            else:
                add_movie_ranking(userMovie, userRank)
                print(f"Movie '{userMovie}' with rank {userRank} added successfully!")


        elif choice == '2':
            view_movie_rankings()
        elif choice == '3':
            print("Exiting the Movie Ranker. Goodbye!")
            break
            
main()
    
