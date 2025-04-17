# Import required libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


# We read the airline data into the pandas dataframe
spacex_df = pd.read_csv("data\processed\spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)
                               
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
        style={'textAlign': 'center',
                'color': '#000004',
                'font-size': 50}),
    html.Br(),
    # TASK 1: Add a drop-down list to enable launch site selection
    # The default selection value is for ALL launch sites
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All sities', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}  
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    # TASK 3: Add a slider to select the payload range
    dcc.RangeSlider(id='payload-slider',
                min=0, max=10000, step=1000,
                marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                value=[min_payload, max_payload]),

    # TASK 4: Add a scatter chart to show the evaluation between payload and launch success.
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    ])
# TASK 2: Add a callback function to plot a pie chart of success based on the selected site dropdown menu
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # We group by 'Launch Site' and add the hits (class=1)
        all_sites_df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(all_sites_df, values='class', names='Launch Site',
                     title='Total Successful Launches by Site')
        return fig
    else:
        # We filter by the selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # We count successes and failures (class: 1 = success, 0 = failure)
        outcome_counts = filtered_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        outcome_counts['Outcome'] = outcome_counts['Outcome'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(outcome_counts, values='Count', names='Outcome',
                     title=f'Success vs Failure Launches for site {entered_site}')
        return fig

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter(selected_site, payload_range):
    # We filter by payload range
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if selected_site == 'ALL':
        fig = px.scatter(filtered_df, 
                         x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category',
                         title='correlation between payload and launch success')
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(site_df, 
                         x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category',
                         title=f'Payload vs. Success for {selected_site}')
    return fig


# Run the app
if __name__ == '__main__':
    app.run()