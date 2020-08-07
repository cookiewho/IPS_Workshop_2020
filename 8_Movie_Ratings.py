def favorite_genres(users, movies, movie_ratings):
  for user in users:
    dict = {}
    for movie_rating in movie_ratings:
      if user.get('id') == movie_rating.get('user_id'):
        for movie in movies:
          if movie_rating.get('movie_id') == movie.get('id'):
            if movie['genre'] in dict:
              dict[movie['genre']].append(movie_rating['rating'])
            else:
              dict[movie['genre']] = [movie_rating['rating']]
    for genre in dict:                                #average values properly, dont use shortcuts
      dict[genre] = sum(dict[genre])/len(dict[genre])
    vals = list(dict.values())
    max_ind = 0
    for x in range(len(vals)):
      if vals[x] > vals[max_ind]:
        max_ind = x
      if vals[x] == 5:
        break
    keys = list(dict.keys())
    user["favorite_genre"] = keys[max_ind]
  return (users)
users = [{"id": "923874rksd9293"}]
movie_ratings = [{"movie_id": "20jfcf02341kwd","user_id": "923874rksd9293", "rating": 5}]
movies = [
  {
     "id": "20jfcf02341kwd",
     "genre": "animated"
  }
]

print(favorite_genres(users, movies, movie_ratings))
# users = [
#   {
#     "id": "923874rksd9293",
#     "favorite_genre": "animated"
#   }
# ]
