import pandas as pd

def run_scheduler(orders_df, machines_df, materials_df):
    # Placeholder logic for scheduling - to be replaced with MIP logic
    orders_df['assigned_machine'] = ['M1', 'M2', 'M1'][:len(orders_df)]
    orders_df['scheduled_hours'] = [2, 3, 1][:len(orders_df)]

    summary = {
        "Total Orders": len(orders_df),
        "Machines Used": orders_df['assigned_machine'].nunique(),
        "Total Scheduled Hours": orders_df['scheduled_hours'].sum()
    }

    return orders_df, summary
