# facebook-market
My first project using ML

### Milestone 1

I decided to use NLP (Natural Language Processing) for the product_name, product_description and location so to not waste any information. Before this, I have trimmed a lot of data and only encoded location and categories. This is not ideal as a lot of information is lost from the product_name and product_description columns.

I will use CVec (CountVectorizer) and TFIDF Vectorizer (Term Frequency Inverse Document Frequency) to examine the importance of each feature (word or character) in my 'string based' columns.