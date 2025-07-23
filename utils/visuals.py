import plotly.express as px
import pandas as pd

def plot_gantt(df):
    # Ensure correct columns exist
    if {'order_id', 'assigned_machine', 'scheduled_hours'}.issubset(df.columns):
        df['Start'] = pd.to_datetime('today')
        df['Finish'] = df['Start'] + pd.to_timedelta(df['scheduled_hours'], unit='h')
        df['Task'] = 'Order ' + df['order_id'].astype(str)

        fig = px.timeline(df, x_start="Start", x_end="Finish", y="assigned_machine", color="Task")
        fig.update_layout(title="Production Schedule Gantt Chart", xaxis_title="Time", yaxis_title="Machine")
        return fig
    return None
