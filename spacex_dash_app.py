# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
options=[{'label': 'All Sites', 'value': 'ALL'},{'label': 'site1', 'value': 'site1'},
        {'label': 'site2', 'value': 'site2'}, {'label': 'site3', 'value': 'site3'}, 
        {'label': 'site4', 'value': 'site4'}]
print(max_payload)        
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(
                                    id='site-drowdown',
                                    options = options,
                                    value='ALL',
                                    placeholder= 'Select a Launch Site here',
                                    searchable=True,),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider', min=int(min_payload), max=int(max_payload),
                                                step=5, marks={i: str(i) for i in range(int(min_payload), int(max_payload), 1000)},
                                                value=[int(min_payload), int(max_payload)]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
        Input(component_id='site-drowdown', component_property='value'))
def get_pie_chart(entered_site):
    data = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(data, values='class', names='Launch Site', title='Succes Rate for all sites')
        return fig
    elif entered_site == 'site1':
        filtered_data = data[data['Launch Site'] == 'CCAFS LC-40']
        class_counts = filtered_data['class'].value_counts()
        fig = px.pie(names=class_counts.index,  # 0 y 1 como nombres
        values=class_counts.values, title='Succes Rate SLC-40 site')
        return fig
    elif entered_site == 'site2':
        filtered_data = data[data['Launch Site'] == 'VAFB SLC-4E']
        class_counts = filtered_data['class'].value_counts()
        fig = px.pie(names=class_counts.index,  # 0 y 1 como nombres
        values=class_counts.values, title='Succes Rate SLC-40 site')
        return fig
    elif entered_site == 'site3':
        filtered_data = data[data['Launch Site'] == 'KSC LC-39A']
        class_counts = filtered_data['class'].value_counts()
        fig = px.pie(names=class_counts.index,  # 0 y 1 como nombres
        values=class_counts.values, title='Succes Rate SLC-40 site')
        return fig
    elif entered_site == 'site4':
        filtered_data = data[data['Launch Site'] == 'CCAFS SLC-40']
        class_counts = filtered_data['class'].value_counts()
        fig = px.pie(names=class_counts.index,  # 0 y 1 como nombres
        values=class_counts.values, title='Succes Rate SLC-40 site')
        return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
            [Input(component_id='site-drowdown', component_property='value'), Input(component_id='payload-slider', component_property='value')]
            )
def show_scatter_payload(entered_site, selected_range):
    data = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= selected_range[0]) & 
        (spacex_df['Payload Mass (kg)'] <= selected_range[1])]
    if entered_site == 'ALL':
        fig = px.scatter(data, x='Payload Mass (kg)', y='class', color='Booster Version', title='Success rate per mass')
        return fig
    elif entered_site == 'site1':
        fig = px.scatter(data[data['Launch Site'] == 'CCAFS LC-40'], x='Payload Mass (kg)', y='class', color='Booster Version', title='Success rate per mass')
        return fig
    elif entered_site == 'site2':
        fig = px.scatter(data[data['Launch Site'] == 'VAFB SLC-4E'], x='Payload Mass (kg)', y='class', color='Booster Version', title='Success rate per mass')
        return fig
    elif entered_site == 'site3':
        fig = px.scatter(data[data['Launch Site'] == 'KSC LC-39A'], x='Payload Mass (kg)', y='class', color='Booster Version', title='Success rate per mass')
        return fig
    elif entered_site == 'site4':
        fig = px.scatter(data[data['Launch Site'] == 'CCAFS SLC-40'], x='Payload Mass (kg)', y='class', color='Booster Version', title='Success rate per mass')
        return fig
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
