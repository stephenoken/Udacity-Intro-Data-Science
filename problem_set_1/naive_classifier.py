class NaiveBayes:
    def partition_outcomes(self, xy):
        if len(xy) == 0:
            return []
        x = xy[0]
        result = (x[0],) if x[1] == 0 else (None, x[0])
        return [result] + self.partition_outcomes(xy[1:])

    def fit(self, X, Y):
        (living, dead) = self.partition_outcomes(zip(X, Y))
        print(living)
        print("######")
        print(dead)


def sex_feature(sex):
    return 1 if sex == "female" else 0


def simple_heuristic(df):
    titanic_data = zip(df['PassengerId'].tolist(), df['Sex'].tolist())
    return {id: sex_feature(sex) for (id, sex) in titanic_data}
