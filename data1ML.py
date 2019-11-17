from surprise import SVD, Dataset, accuracy
from surprise .model_selection import train_test_split, cross_validate, GridSearchCV
from surprise import Reader
import pickle
import random

reader = Reader(sep=",", rating_scale=(0.5,2.5))
data = Dataset.load_from_file("data/data1_user.csv", reader=reader,)
#print(data)
random.shuffle(data.raw_ratings)
train_set, test_set = train_test_split(data, random_state=1)
#print(train_set)

# print('Grid Search...')
# param_grid = {'n_epochs': [10, 100], 'lr_all': [0.002, 0.005]}
# grid_search = GridSearchCV(SVD, param_grid, measures=['rmse'], cv=3)
# grid_search.fit(data)
#
# algo = grid_search.best_estimator['rmse']
# print(grid_search.cv_results)
#
# # retrain on the whole set A
# algo.fit(train_set)
#
# # Compute biased accuracy on A
# predictions = algo.test(train_set.build_testset())
# print('Biased accuracy on A,', end='   ')
# accuracy.rmse(predictions)
#
# # Compute unbiased accuracy on B # testset is now the set B
# predictions = algo.test(test_set)
# print('Unbiased accuracy on B,', end=' ')
# accuracy.rmse(predictions)
# print(grid_search.cv_results)


algo = SVD(n_epochs=1000,n_factors=10, random_state=0)
algo.fit(train_set)
filename = 'data1ML.model'
pickle.dump(algo, open(filename, 'wb'))
print(train_set)
predict = algo.test(test_set)
print(predict)
accuracy.rmse(predict)
algo.predict(str(2),str(6), verbose=True)
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)