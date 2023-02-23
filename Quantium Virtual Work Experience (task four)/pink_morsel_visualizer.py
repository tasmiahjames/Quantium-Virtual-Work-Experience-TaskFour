import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

DATA_PATH = "./data.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

#init dash
dash_app = Dash(__name__)

def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart

#visualization
visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

#header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


#define the callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    #filter
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    #generate a new line chart
    figure = generate_figure(trimmed_data)
    return figure


#app layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

#this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()
