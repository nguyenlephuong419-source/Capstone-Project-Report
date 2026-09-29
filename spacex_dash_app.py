"""Interactive Falcon 9 landing dashboard using the IBM course dataset.

Install the requirements and run from the repository root:
    pip install -r requirements.txt
    python spacex_dash_app.py
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "dataset_part_2.csv")
df["Outcome"] = df["Class"].map({1: "Successful landing", 0: "Other outcome"})

app = Dash(__name__)
app.title = "SpaceX Falcon 9 Landing Dashboard"
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 first-stage landing outcomes"),
    html.P("Historical IBM course snapshot: 90 Falcon 9 flights."),
    dcc.Dropdown(
        id="site", options=[{"label": "All sites", "value": "ALL"}] +
        [{"label": site, "value": site} for site in sorted(df["LaunchSite"].unique())],
        value="ALL", clearable=False,
    ),
    dcc.Graph(id="site-pie"),
    html.Label("Payload mass range (kg)"),
    dcc.RangeSlider(
        id="payload", min=0, max=10000, step=500, value=[0, 10000],
        marks={i: f"{i:,}" for i in range(0, 10001, 2000)},
    ),
    dcc.Graph(id="payload-scatter"),
    html.P("Source: IBM DS0321EN dataset_part_2.csv. Outcome is first-stage landing success."),
], style={"maxWidth": "1100px", "margin": "auto", "fontFamily": "Arial, sans-serif"})

@app.callback(
    Output("site-pie", "figure"), Output("payload-scatter", "figure"),
    Input("site", "value"), Input("payload", "value"),
)
def update_charts(site, payload_range):
    selected = df if site == "ALL" else df[df["LaunchSite"] == site]
    counts = selected.groupby("Outcome", as_index=False).size()
    pie = px.pie(counts, names="Outcome", values="size", title=f"Landing outcomes: {site}",
                 color="Outcome", color_discrete_map={"Successful landing": "#16876e", "Other outcome": "#d86849"})
    filtered = selected[selected["PayloadMass"].between(*payload_range)]
    scatter = px.scatter(filtered, x="PayloadMass", y="LaunchSite", color="Outcome",
                         hover_data=["FlightNumber", "Orbit"], title="Payload versus launch outcome",
                         color_discrete_map={"Successful landing": "#16876e", "Other outcome": "#d86849"})
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=False)
