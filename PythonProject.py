import time
import datetime as dt
import pandas as pd
import numpy


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
week_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

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
    cities = ['chicago', 'new york city', 'washington']
    city = ''
    while city not in cities:
        try:
            city = input('Select a city from the following list (Chicago, New York City, Washington)): \n').lower().strip()
            if city not in cities:
                print('City supplied is not the list, please make sure to use correct spelling')
        except Exception as e:
            print("Exception sytax: {}".format(e))



    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    all_month = months + ['all']

    while month not in all_month:
        try:
            month = input('\nType " ALL " to analyze all time data or select a month from the following list' + str(months) + '\n').lower().strip()
            if month not in months:
                print('Month syntax input is incorrect, please try again')
        except Exception as e:
            print("Exception sytax: {}".format(e))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    all_days = week_days + ['all']
    day = ''
    while day not in all_days:
        try:
            day = input('Type "all" to analyze all time data or select a day from the following list \n' + str(week_days) + '\n').lower().strip()
            if day not in all_days:
                print('Day syntax frame given is incorrect')
        except Exception as e:
            print("Exception sytax: {}".format(e))

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != 'all':
        month_index = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        df = df[df['Start Time'].dt.month == month_index[month]]
    else:
        df['month'] = df['Start Time'].dt.month

    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]
    else:
        df['day'] = df['Start Time'].dt.weekday_name

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month

    if 'month' in df.columns:
        common_month = df['month'].mode()[0]
        print('The most common month using applied filters is: ' + str(months[common_month-1]).title())
    # TO DO: display the most common day of week
    if 'day' in df.columns:
        common_day = df['day'].mode()[0]
        print('The most common day using applied filters is: ', common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour using applied filters is: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station using applied filters is: ', common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station using applied filters is: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station'] + ' - ' + df['End Station']
    common_combo = df['Combo'].mode()[0]
    print('The most common combination from start and end stations is: ', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_timing = df['Trip Duration'].sum()
    read_total = str(dt.timedelta(seconds=int(total_timing)))
    print('The total traveled time is: ', read_total)

    # TO DO: display mean travel time
    average_timing = df['Trip Duration'].mean()
    read_average = str(dt.timedelta(seconds=int(average_timing)))
    print('The average travel time is: ', read_average)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print('The total number of users is:', df['User Type'].count())
    else:
        print('No user data type is found in supplied data')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts(dropna=True)
        male = gender['Male']
        female = gender['Female']
        print("Total number of males: ", male, "\nTotal number of females: ", female)
    else:
        print('No gender data is found in supplied data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("The earliest year of birth : ", int(df['Birth Year'].min()))
        print("The most recent year of birth : ", int(df['Birth Year'].max()))
        print("The most common year of birth : ", int(df['Birth Year'].mode()[0]))
    else:
        print("No birth year is found in supplied data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
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
