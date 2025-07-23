# Smart Production Scheduler

## 🧠 Problem Statement
**Supply Planning - Production Scheduling under Constraints**  
Manufacturers must plan production schedules while dealing with limited machine hours and material availability. Poor scheduling leads to under-utilized resources and missed demand.

## 💡 Real Optimization Solution
We use a **Mixed-Integer Programming (MIP)** model powered by [PuLP](https://coin-or.github.io/pulp/) to:
- Assign each order to one available machine
- Respect machine working time constraints
- Prevent exceeding available material stock

### Constraints Modeled
- Each order must be assigned to exactly one machine
- Machine total hours cannot be exceeded
- Material consumption per product is constrained by available stock

### Objective
Minimize total **unused machine hours**, maximizing machine utilization and production throughput.

## 📈 Business Impact
- ✅ Increases production throughput
- ✅ Reduces waste of machine and material resources
- ✅ Enables better capacity planning and order execution

## 🧪 Techniques Used
- **Optimization**: Mixed-Integer Linear Programming (MILP)
- **Tool**: `PuLP` for constraint modeling and solving
- **Visualization**: (Gantt chart planned via Plotly)

## 📊 Dashboard KPIs
- Total scheduled hours
- Number of machines used
- Utilization efficiency
- Per-order machine assignment

## 📁 Folder Structure
```
├── app.py                    # Main Streamlit app
├── data/                     # Sample input data (CSV)
├── models/                   # Placeholder for saved models
├── notebooks/                # Jupyter prototyping (optional)
├── utils/                    # Logic for scheduler and visuals
│   ├── scheduler.py
│   ├── modeling.py
│   └── visuals.py
├── requirements.txt          # Packages for Streamlit Cloud
├── README.md
```

## ✅ Sample Input Files
- `orders.csv`: order_id, product_type, quantity, priority
- `machines.csv`: machine_id, available_hours
- `materials.csv`: material_type, stock_units

## 🚀 How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Run app: `streamlit run app.py`

## 🔗 References
- [GoodData Dashboard Examples](https://www.gooddata.com/blog/supply-chain-dashboard-examples/)
- [ACM Paper on Constraint-Aware Scheduling](https://dl.acm.org/doi/fullHtml/10.1145/3584816.3584830)
- [PuLP Documentation](https://coin-or.github.io/pulp/)
