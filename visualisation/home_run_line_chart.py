import pandas
from ggplot import *
def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/
    home_runs_df = pandas.read_csv(hr_year_csv)
    gg = ggplot(home_runs_df, aes(x='yearID', y='HR')) + geom_line() + geom_point(color="red")
    gg = gg + ggtitle('Total HRs by year') + xlab('Year') + ylab('Home Runs')
    return gg


if __name__ == "__main__":
    lineplot("./hr_year.csv").show()
