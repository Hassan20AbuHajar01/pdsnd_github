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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please choose from chicago, new york city, or washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter month (all, january, february, ..., june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month name. Please choose a valid month or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day of the week (all, monday, tuesday, ..., sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day name. Please choose a valid day or 'all'.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
        Loads data for the specified city's bikeshare system.

        Args:
            city (str): Name of the city to load data for.

        Returns:
            df (DataFrame): Pandas DataFrame containing the city's bikeshare data.
    """
    df = pd.read_csv(f'{city}.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week from 'Start Time'
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print(f"The most common month for travel: {common_month}")

    # Display the most common day of the week
    common_day = df['Day of Week'].mode()[0]
    print(f"The most common day of the week for travel: {common_day}")

    # Display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f"The most common start hour for travel: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {common_start_station}")

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {common_end_station}")

    # Display most frequent combination of start station and end station trip
    df['Start-End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip_combination = df['Start-End Combination'].mode()[0]
    print(f"The most frequent trip combination: {common_trip_combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display unique user types
    unique_user_types = df['User Type'].unique()
    print("Unique user types:", ', '.join(unique_user_types))

    # Display unique gender values (if available in the data)
    if 'Gender' in df:
        unique_genders = df['Gender'].unique()
        print("\nUnique genders:", ', '.join(unique_genders))
    else:
        print("\nGender data is not available for this city.")

    # Display unique birth years (if available in the data)
    if 'Birth Year' in df:
        unique_birth_years = df['Birth Year'].unique()
        print("\nUnique birth years:", ', '.join(map(str, unique_birth_years)))
    else:
        print("\nBirth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Display earliest, most recent, and most common year of birth (if available in the data)
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nEarliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", common_birth_year)
    else:
        print("\nBirth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Displays data in chunks of 5 rows based on user input.
    
    Args:
        df - Pandas DataFrame containing bikeshare data
    """
    print('\nDisplaying Data...\n')
    while True:
        display = input('\nDo you want to view 5 rows of raw data? Please enter yes or no.\n')
        if display.lower() != 'yes':
            break
        print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
        i+=5

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
