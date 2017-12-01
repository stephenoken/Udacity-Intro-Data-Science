import pandas as pd
from ggplot import ggplot, aes, geom_point, geom_line, scale_color_identity

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather

    To see all the columns and data points included in the turnstile_weather 
    dataframe.
    
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    turnstile_df = pd.read_csv(turnstile_weather)
    turnstile_df['DayOfWeek'] = pd.to_datetime(turnstile_df['DATEn']).apply(lambda x: x.weekday())
    # turnstile_df = turnstile_df.groupby(['DayOfWeek'])
  #  df = pd.DataFrame(turnstile_df.groupby(['UNIT', 'DayOfWeek'])['ENTRIESn_hourly', "EXITSn_hourly"].sum())
 #   df.reset_index(inplace=True)
    # data = pd.concat([df.head((7 * 5)), df.tail((7 * 5))])
#     plot = ggplot(df, aes(x="DayOfWeek", y="ENTRIESn_hourly", color="DayOfWeek")) + geom_point() 
    # Display the sum hourly entries and arrivals by each day 
    foot_traffic_df = pd.DataFrame(turnstile_df.groupby(['DayOfWeek'])['ENTRIESn_hourly', "EXITSn_hourly"].sum())
    foot_traffic_df.reset_index(inplace=True)
    foot_traffic_df = pd.melt(foot_traffic_df, id_vars=["DayOfWeek"])  
    plot = ggplot(foot_traffic_df, aes(x="DayOfWeek", y="value", color="variable")) + geom_line()
    # ggplot(turnstile_df, aes(x='DayOfWeek', y='ENTRIESn_hourly', color="UNIT")) + geom_line()
    return plot


if __name__ == "__main__":
    plot_weather_data("./turnstile_data_master_with_weather.csv").show()
