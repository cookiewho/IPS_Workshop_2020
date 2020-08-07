def sentiment_scores(sentiments, texts):
  scores = []
  for text in texts:
    text = text.lower().replace(",", "").replace(".","").replace("!", "").replace("?", "")
    text = text.split()
    score = 0
    for word in text:
      if word in sentiments:
        # print(word + " " + str(sentiments[word]))
        score += sentiments[word]
    scores.append(score)
  return scores
  
sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}
texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]

print(sentiment_scores(sentiments, texts))