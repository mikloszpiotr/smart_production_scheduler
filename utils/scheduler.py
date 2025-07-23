import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpStatus

def run_scheduler(orders_df, machines_df, materials_df):
    material_requirements = {"A": "MatA", "B": "MatB"}
    time_per_unit = 1 / 100  # 1 hour per 100 units

    model = LpProblem("Production_Scheduling", LpMinimize)

    x = {
        (i, m): LpVariable(f"x_{i}_{m}", cat=LpBinary)
        for i in orders_df.index
        for m in machines_df["machine_id"]
    }

    total_machine_hours = {
        m: machines_df.loc[machines_df["machine_id"] == m, "available_hours"].values[0]
        for m in machines_df["machine_id"]
    }
    used_hours = {
        m: lpSum(x[(i, m)] * orders_df.loc[i, "quantity"] * time_per_unit for i in orders_df.index)
        for m in machines_df["machine_id"]
    }

    model += lpSum(total_machine_hours[m] - used_hours[m] for m in machines_df["machine_id"])

    for i in orders_df.index:
        model += lpSum(x[(i, m)] for m in machines_df["machine_id"]) == 1

    for m in machines_df["machine_id"]:
        model += used_hours[m] <= total_machine_hours[m]

    for mat in materials_df["material_type"]:
        mat_orders = [
            i for i in orders_df.index
            if material_requirements[orders_df.loc[i, "product_type"]] == mat
        ]
        total_material_used = lpSum(
            x[(i, m)] * orders_df.loc[i, "quantity"]
            for i in mat_orders
            for m in machines_df["machine_id"]
        )
        available = materials_df.loc[materials_df["material_type"] == mat, "stock_units"].values[0]
        model += total_material_used <= available

    model.solve()

    schedule_rows = []
    for i in orders_df.index:
        for m in machines_df["machine_id"]:
            if x[(i, m)].value() == 1:
                schedule_rows.append({
                    "order_id": orders_df.loc[i, "order_id"],
                    "product_type": orders_df.loc[i, "product_type"],
                    "quantity": orders_df.loc[i, "quantity"],
                    "assigned_machine": m,
                    "scheduled_hours": orders_df.loc[i, "quantity"] * time_per_unit
                })

    schedule_df = pd.DataFrame(schedule_rows)
    summary = {
        "Total Orders": len(orders_df),
        "Machines Used": schedule_df["assigned_machine"].nunique(),
        "Total Scheduled Hours": schedule_df["scheduled_hours"].sum(),
        "Solver Status": LpStatus[model.status]
    }

    return schedule_df, summary
