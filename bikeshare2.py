import time
import pandas as pd 
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('can you please choose a city from chicago, new york city, washington ')
    while city not in (CITY_DATA.keys()):
           print('please choose correct city name')
           City = input ('can you please choose a city from chicago, new york city, washington ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
           month = input('can you please choose a  month from january to june, or type "all" to desplay all months :').lower()
           months = ['january','february','march','april','may','june']
           if month != "all" and month not in months:
                  print("please choose correct Month")
           else:
                   break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
           day = input('can you please choose from days in the week, or type "all"  to desplay all days:' ).lower()
           days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
           
           if day != 'all' and day not in days:
                  print("please choose correct day")
           else:
                   break
    print('-'*40)
    return city,month,day         
city, month, day = get_filters()                     
     
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """ 
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #convert start time to datatime
    df['start time'] = pd.to_datetime(df['start time'])
    #extract month and day of week
    df['month'] = df['start time'].dt.month
    df['day_of_week'] = df['start time'].dt.day_name()
    #filter
    if month != "all":
           months = ['january','february','march','april','may','june']
           month = month.index(month) + 1
     #creat new datafram for months
    df = df[df['month'] == month]
     #creat new datafram for day of week
    if day != 'all':
            df = df[df['day_of_week'] == day.title()]
    return df
load_data(city, month, day)
def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january','february','march','april','may','june']
    month = df ["month"].mode()[0]
    print('most coommon month is: {months [month]}')
    # TO DO: display the most common day of week
    day = df["day_of_week"].mode([0])
    print('most coommon day of week is: {days [day]}')
    # TO DO: display the most common start hour
    df['hour'] = df['start time'].dt.hour
    hour =df['hour'].mode(0)
    print('most coommon day of week is: {days [day]}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(df)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_start_station = df['start station'].mode(0)
    print('most coommon start station is: [most_start_station]')
    # TO DO: display most frequent combination of start station and end station trip
    most_trip = df['start station'] + ' , ' + df['end station'].mode(0)
    print('most frequent combination of start station and end station trip is: [most_trip]')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total trave time:',total_time,'seconds, or',total_time/3600,'hour')
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean trave time:',mean_time,'seconds, or',mean_time/3600,'hour')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(df)
def user_stats(df):
       """Displays statistics on bikeshare users."""
       print('\nCalculating User Stats...\n')
       start_time = time.time()
       # TO DO: Display counts of user types
       df = ['user type'].value_counts()
       print('count of user typs:\n')
       # TO DO: Display counts of gender
       df = ['grnder'].value_counts()
       if 'Gender' in df:
              print('count of gender:\n')
       # TO DO: Display earliest, most recent, and most common year of birth
       year = df['birth year'].value_counts()
       if 'birth year' in df:
              print('earliset birth year is:{year.min()}\nmost recent is: {year.max()}\nand most common birth year is: (year.mode()[0]')
              print("\nThis took %s seconds." % (time.time() - start_time))
              print('-'*40)
user_stats(df)


def display_raw_data(df):
       """ask the user if he want to display the raw data and print 5 rows at time"""
       raw = input('\ndo you want to display raw data\n')
       if raw.lower() == "yes":
              count = 0
              while True:
                     print(df.iloc[count: count+5])
                     count += 5
                     ask = input('next 5 raws?')
                     if ask.lower() != 'yes': 
                            break
display_raw_data(df)       
def main():
       while True:
              display_raw_data(df)
              city, month, day = get_filters()
              df = load_data(city, month, day)
              time_stats(df)
              station_stats(df)
              trip_duration_stats(df)
              user_stats(df)
              
              restart = input('\nWould you like to restart? Enter yes or no.\n')
              if restart.lower() != 'yes':
                     break
       if __name__ == "__main__":
              main()
       