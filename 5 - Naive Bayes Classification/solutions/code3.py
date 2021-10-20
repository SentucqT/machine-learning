### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

from sklearn.naive_bayes import MultinomialNB
spam_nbc = MultinomialNB()
spam_nbc.fit(Xtrain,ytrain)
print("Score:", spam_nbc.score(Xtest,ytest))

# Compute cross-validation score
nb_trials = 20
score = []
for i in range(nb_trials):
    Xtrain, ytrain, Xtest, ytest = spam_data.shuffle_and_split(2000)
    spam_nbc = MultinomialNB()
    spam_nbc.fit(Xtrain,ytrain);
    score += [spam_nbc.score(Xtest,ytest)]
    print('*', end='')
print(" done!")
print("Average generalization score:", np.mean(score))
print("Standard deviation:", np.std(score))
