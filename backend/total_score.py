import json
import numpy as np
from text_similarity import calculate_review_similarity_score
from demographic_info_score import get_demographic_info_score
from popularity_score import get_rating_popularity_score

with open("data/author_demographics.json", "r") as file:
    demographics_data = json.load(file)

with open("data/reviews_en.json", "r") as file:
    review_data = json.load(file)

def get_total_score(city, user_age, user_gender, user_text, poi_list): 
    popularity_score, rating_score = get_rating_popularity_score(poi_list)
    review_similarity_score = \
        calculate_review_similarity_score(city, user_text) #returns a list of all POI_text_scores
    demographic_score = get_demographic_info_score(demographics_data, review_data, user_age, 
                                      user_gender, poi_list) #returns a list of all POIs_demogr_score
    
    print(f"popularity min, max: {min(popularity_score), max(popularity_score)}")
    print(f"rating min, max: {min(rating_score), max(rating_score)}")
    print(f"review_similarity_score min, max: {min(review_similarity_score), max(review_similarity_score)}")
    print(f"demographic_score min, max: {min(demographic_score), max(demographic_score)}")
    return 0.6 * review_similarity_score + 0.1 * popularity_score + \
        0.1 * rating_score + 0.2 * np.array(demographic_score) 