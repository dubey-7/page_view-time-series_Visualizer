import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# Clean data (remove top and bottom 2.5%)
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    df_copy = df.copy()

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_copy.index, df_copy["value"], color="red")

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_copy = df.copy()

    df_copy["year"] = df_copy.index.year
    df_copy["month"] = df_copy.index.month_name()

    df_bar = df_copy.groupby(["year", "month"])["value"].mean().unstack()

    # Order months correctly
    months_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    df_bar = df_bar[months_order]

    fig = df_bar.plot(kind="bar", figsize=(10, 8)).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    df_copy = df.copy()
    df_copy.reset_index(inplace=True)

    df_copy["year"] = df_copy["date"].dt.year
    df_copy["month"] = df_copy["date"].dt.strftime("%b")
    df_copy["month_num"] = df_copy["date"].dt.month

    # Sort months properly
    df_copy = df_copy.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    sns.boxplot(
        data=df_copy,
        x="year",
        y="value",
        ax=axes[0]
    )
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        data=df_copy,
        x="month",
        y="value",
        ax=axes[1]
    )
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
