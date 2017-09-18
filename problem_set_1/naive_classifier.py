class NaiveBayes:

    def fit(self, X, Y):
       pass 


def sex_feature(sex):
    return 1 if sex == "female" else 0


def simple_heuristic(df):
    titanic_data = zip(df['PassengerId'].tolist(), df['Sex'].tolist())
    return {id: sex_feature(sex) for (id, sex) in titanic_data}
