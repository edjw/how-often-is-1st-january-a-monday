from datetime import datetime
from statistics import mean
import plotly
import plotly.graph_objs as go

# year = int(datetime.today().strftime("%Y"))  # 2018 at the moment
year = 9999  # the latest year you can use


def get_first_jan_weekdays(year):

    mondays = []  # "2018, 2007, 2001"
    tuesdays = []
    wednesdays = []
    thursdays = []
    fridays = []
    saturdays = []
    sundays = []

    while year >= 1:

        day_of_week_first_jan = datetime(year, 1, 1).strftime("%A")

        if day_of_week_first_jan == 'Monday':
            mondays.append(year)
        elif day_of_week_first_jan == 'Tuesday':
            tuesdays.append(year)
        elif day_of_week_first_jan == 'Wednesday':
            wednesdays.append(year)
        elif day_of_week_first_jan == 'Thursday':
            thursdays.append(year)
        elif day_of_week_first_jan == 'Friday':
            fridays.append(year)
        elif day_of_week_first_jan == 'Saturday':
            saturdays.append(year)
        elif day_of_week_first_jan == 'Sunday':
            sundays.append(year)

        year -= 1

    return mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays


def first_jans_over_time(mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays):
    mondays_over_time = sorted(mondays)
    tuesdays_over_time = sorted(tuesdays)
    wednesdays_over_time = sorted(wednesdays)
    thursdays_over_time = sorted(thursdays)
    fridays_over_time = sorted(fridays)
    saturdays_over_time = sorted(saturdays)
    sundays_over_time = sorted(sundays)

    return mondays_over_time, tuesdays_over_time, wednesdays_over_time, thursdays_over_time, fridays_over_time, saturdays_over_time, sundays_over_time


def get_number_of_first_jan_weekdays(mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays):
    total_mondays = len(mondays)
    total_tuesdays = len(tuesdays)
    total_wednesdays = len(wednesdays)
    total_thursdays = len(thursdays)
    total_fridays = len(fridays)
    total_saturdays = len(saturdays)
    total_sundays = len(sundays)

    return total_mondays, total_tuesdays, total_wednesdays, total_thursdays, total_fridays, total_saturdays, total_sundays


def get_avg_wait_between_years(mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays):
    # 1st num minus 2nd num
    mon_waits = [s - t for s, t in zip(mondays, mondays[1:])]
    # mean difference rounded to 2 decimal places
    mon_avg_wait = round(mean(mon_waits), 2)

    tues_waits = [s - t for s, t in zip(tuesdays, tuesdays[1:])]
    tues_avg_wait = round(mean(tues_waits), 2)

    wed_waits = [s - t for s, t in zip(wednesdays, wednesdays[1:])]
    wed_avg_wait = round(mean(wed_waits), 2)

    thurs_waits = [s - t for s, t in zip(thursdays, thursdays[1:])]
    thurs_avg_wait = round(mean(thurs_waits), 2)

    fri_waits = [s - t for s, t in zip(fridays, fridays[1:])]
    fri_avg_wait = round(mean(fri_waits), 2)

    sat_waits = [s - t for s, t in zip(saturdays, saturdays[1:])]
    sat_avg_wait = round(mean(sat_waits), 2)

    sun_waits = [s - t for s, t in zip(sundays, sundays[1:])]
    sun_avg_wait = round(mean(sun_waits), 2)

    return mon_avg_wait, tues_avg_wait, wed_avg_wait, thurs_avg_wait, fri_avg_wait, sat_avg_wait, sun_avg_wait


def generate_first_jan_over_time_line_chart(*args):

    trace0 = go.Scatter(
        x=mondays_over_time,
        name='Mondays',
        line=dict(
            color=('red'),
            width=3)
        )

    trace1 = go.Scatter(
        x=tuesdays_over_time,
        name='Tuesdays',
        line=dict(
        color=('blue'),
        width=3)
    )

    trace2 = go.Scatter(
        x=wednesdays_over_time,
        name='Wednesdays',
        line=dict(
        color=('yellow'),
        width=3)
    )

    trace3 = go.Scatter(
        x=thursdays_over_time,
        name='Thursdays',
        line=dict(
        color=('green'),
        width=3)
    )

    trace4 = go.Scatter(
        x=fridays_over_time,
        name='Fridays',
        line=dict(
        color=('black'),
        width=3)
    )

    trace5 = go.Scatter(
        x=saturdays_over_time,
        name='Saturdays',
        line=dict(
        color=('pink'),
        width=3)
    )

    trace6 = go.Scatter(
        x=sundays_over_time,
        name='Sundays',
        line=dict(
        color=('orange'),
        width=3)
    )


    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6]

    layout = go.Layout(
        title="Number of times 1st Jan is X day over time",

        xaxis=dict(
            title="Instance of X day as 1st January",
            range=[0, 10001]

        ),
        yaxis=dict(
            title="Year from 1 AD to 9999",
            range=[0, 1400]

        ),

    )

    plotly.offline.plot({"data": data, "layout": layout})


def generate_totals_bar_chart(*args):
    y_axis_data = []
    for arg in args:
        y_axis_data.append(arg)

    data = [go.Bar(
            x=["Mondays", "Tuesdays", "Wednesdays",
                "Thursday", "Fridays", "Saturdays", "Sundays"],
            y=y_axis_data
            )]

    layout = go.Layout(
        title="How often is 1st January a Monday? From the year 1 to 9999",

        xaxis=dict(
            title="Days of the week"
        ),
        yaxis=dict(
            title="Number of times 1st January has been X day",
            range=[1350, 1460]
        ),

    )

    plotly.offline.plot({"data": data, "layout": layout})


def generate_avgs_barchart(*args):
    y_axis_data = []
    for arg in args:
        y_axis_data.append(arg)

    data = [go.Bar(
            x=["Mondays", "Tuesdays", "Wednesdays",
                "Thursday", "Fridays", "Saturdays", "Sundays"],
            y=y_axis_data
            )]

    layout = go.Layout(
        title="How many years until it's a Monday again? From the year 1 to 9999",

        xaxis=dict(
            title="Days of the week"
        ),
        yaxis=dict(
            title="Average (mean) years to wait",
            range=[6.5, 7.5]
        ),

    )

    plotly.offline.plot({"data": data, "layout": layout})


mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays = get_first_jan_weekdays(
    year)

total_mondays, total_tuesdays, total_wednesdays, total_thursdays, total_fridays, total_saturdays, total_sundays = get_number_of_first_jan_weekdays(
    mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays)

mon_avg_wait, tues_avg_wait, wed_avg_wait, thurs_avg_wait, fri_avg_wait, sat_avg_wait, sun_avg_wait = get_avg_wait_between_years(
    mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays)

mondays_over_time, tuesdays_over_time, wednesdays_over_time, thursdays_over_time, fridays_over_time, saturdays_over_time, sundays_over_time = first_jans_over_time(
    mondays, tuesdays, wednesdays, thursdays, fridays, saturdays, sundays)

# generate_totals_bar_chart(total_mondays, total_tuesdays, total_wednesdays, total_thursdays, total_fridays, total_saturdays, total_sundays)

# generate_avgs_barchart(mon_avg_wait, tues_avg_wait, wed_avg_wait, thurs_avg_wait, fri_avg_wait, sat_avg_wait, sun_avg_wait)

# generate_first_jan_over_time_line_chart(mondays_over_time, tuesdays_over_time, wednesdays_over_time, thursdays_over_time, fridays_over_time, saturdays_over_time, sundays_over_time)
