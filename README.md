# Smart Production Scheduler

## 🧠 Problem Statement
**Supply Planning - Production Scheduling under Constraints**  
Manufacturing plants often face the challenge of efficiently scheduling production tasks given limited machine hours and material availability.

## 💡 ML + Optimization Solution
- Mixed-Integer Programming to find optimal schedules
- Machine Learning model guides constraint weighting based on past throughput and waste patterns

## 📈 Business Impact
- Boosts production throughput by ~20%
- Reduces material waste and idle time

## 🛠️ Tech Stack
- Streamlit
- Python (Pandas, OR-Tools, XGBoost)
- Plotly (for visualizations)

## 📁 Folder Structure
```
├── app/                    # Streamlit app
│   └── pages/              # Sub-pages for dashboards
├── data/                   # Input CSVs (orders, machines, materials)
├── models/                 # Saved ML models
├── notebooks/              # Exploration and prototyping
├── utils/                  # Scheduling and ML helper functions
```

## 📊 Dashboard KPIs
- Production throughput
- Machine utilization
- Material usage
- Daily schedule (Gantt chart)

## 🔗 References
- [GoodData Dashboard Examples](https://www.gooddata.com/blog/supply-chain-dashboard-examples/)
- [Supply Chain Optimization Repo](https://github.com/ankitrajsh/Supply-Chain-Optimization)
- [ACM Paper on Constraint-Aware Scheduling](https://dl.acm.org/doi/fullHtml/10.1145/3584816.3584830)
