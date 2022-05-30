import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# Reading in the data
df = pd.read_csv('products.csv', lineterminator='\n')

# Processing the data
del df[df.columns[0]]
df.drop(['create_time\r', 'page_id'], axis=1, inplace=True)
df = df.dropna()
df['price'] = df['price'].str.strip('£')

# First data splitting
X = df['product_name']
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print("Number of samples in:")
print(f"    Training: {len(y_train)}")
print(f"    Testing: {len(y_test)}")
# min_df=2 will remove all terms that only appear once in the entire data sheet. I assume them to be outliers or words that are never seen again.
# cvec will transform all words into lowercase by default.
# We only fit on our X_train.
# We want to train the model on just the training data and then all we want to do with the testing data is to transform it based on our training data. 
# We still need both of these to be dataframes so we convert our matrices made in the fit to dense matrices so they can be made into dataframes easily.
cvec = CountVectorizer(min_df=2).fit(X_train)
df_product_name_train = pd.DataFrame(cvec.transform(X_train).todense(),columns=cvec.get_feature_names_out())
df_product_name_test = pd.DataFrame(cvec.transform(X_test).todense(),columns=cvec.get_feature_names_out())
print(df_product_name_train.shape)
print(y_train.shape)
print(df_product_name_test.shape)
print(y_test.shape)
