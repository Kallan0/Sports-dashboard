import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

DATA_FILE = Path(__file__).with_name("records.csv")

st.set_page_config(page_title="Sports Participation Dashboard", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce")
    return df


def main():
    st.markdown(
        """
        <style>
        .main { background: linear-gradient(135deg, #f8fbff 0%, #eef6ff 100%); }
        .stApp { font-family: 'Segoe UI', sans-serif; }
        h1 { color: #0f4c81; }
        .block-container { padding-top: 1.5rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Sports Participation Analytics Dashboard")
    st.write(
        "Explore student participation across departments, genders, and sports with interactive filters and visual insights."
    )

    df = load_data()

    if df.empty:
        st.warning("No data available to display.")
        return

    st.sidebar.header("Filters")
    departments = sorted(df["Department"].dropna().unique().tolist())
    genders = sorted(df["Gender"].dropna().unique().tolist())
    sports = sorted(df["Sports"].dropna().unique().tolist())

    selected_departments = st.sidebar.multiselect("Department", departments, default=departments)
    selected_genders = st.sidebar.multiselect("Gender", genders, default=genders)
    selected_sports = st.sidebar.multiselect("Sports", sports, default=sports)

    filtered_df = df.copy()
    if selected_departments:
        filtered_df = filtered_df[filtered_df["Department"].isin(selected_departments)]
    if selected_genders:
        filtered_df = filtered_df[filtered_df["Gender"].isin(selected_genders)]
    if selected_sports:
        filtered_df = filtered_df[filtered_df["Sports"].isin(selected_sports)]

    st.sidebar.download_button(
        label="Download filtered data",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_sports_participation.csv",
        mime="text/csv",
    )

    st.subheader("Summary Statistics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Participants", len(filtered_df))
    col2.metric("Departments", filtered_df["Department"].nunique())
    col3.metric("Sports", filtered_df["Sports"].nunique())
    col4.metric("Gender Groups", filtered_df["Gender"].nunique())

    st.subheader("Filtered Data")
    st.dataframe(filtered_df, use_container_width=True)

    st.subheader("Visual Insights")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        dept_counts = filtered_df["Department"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Participants"]
        fig_dept = px.bar(
            dept_counts,
            x="Department",
            y="Participants",
            color="Department",
            title="Participants by Department",
        )
        st.plotly_chart(fig_dept, use_container_width=True)

        sport_counts = filtered_df["Sports"].value_counts().reset_index()
        sport_counts.columns = ["Sports", "Count"]
        fig_sports = px.histogram(
            filtered_df,
            x="Sports",
            color="Sports",
            title="Sports Distribution",
        )
        st.plotly_chart(fig_sports, use_container_width=True)

    with chart_col2:
        gender_counts = filtered_df["Gender"].value_counts().reset_index()
        gender_counts.columns = ["Gender", "Count"]
        fig_gender = px.pie(
            gender_counts,
            names="Gender",
            values="Count",
            title="Gender Distribution",
        )
        st.plotly_chart(fig_gender, use_container_width=True)

        fig_scatter = px.scatter(
            filtered_df,
            x="Sports",
            y="Gender",
            color="Gender",
            hover_data=["Name", "Department"],
            title="Gender vs Sports",
        )
        st.plotly_chart(fig_scatter, use_container_width=True)


if __name__ == "__main__":
    main()
