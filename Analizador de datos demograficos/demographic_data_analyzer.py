import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # 1. How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_counts = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    bachelors_percentage = (df['education'] == 'Bachelors').mean()*100

    # 4. What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # 5. What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100
    lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

    # 6. What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (min_hours_workers['salary'] == '>50K').mean() * 100

    # 8. What country has the highest percentage of people that earn >50K?
    rich_by_country = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_earning_country_percentage = rich_by_country.max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_counts) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {bachelors_percentage}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", rich_by_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': bachelors_percentage,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': rich_by_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }