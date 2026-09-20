# 📊 Matplotlib Custom Pie Chart Visualization

This repository contains Python scripts demonstrating advanced data visualization techniques using Matplotlib. This specific script focuses on building and styling customized Pie Charts.

---

## 🎯 Key Concepts Covered

- **Slice Detachment:** Using `explode` to highlight specific data categories.
- **Data Formatting:** Displaying percentage values on wedges using `autopct`.
- **Wedge Styling:** Applying border lines, custom width, and edge colors via `wedgeprops`.
- **Label Orientation:** Adjusting label rotation (`rotatelabels`) and distance (`labeldistance`).

---

## 🛠️ Parameters Breakdown

| Parameter | Function |
| :--- | :--- |
| **`explode`** | Offsets a slice out of the center for emphasis. |
| **`autopct`** | Formats numerical values into percentage text (`%0.2f%%`). |
| **`wedgeprops`** | Controls slice aesthetics like `linewidth`, `edgecolor`, and `width`. |
| **`startangle`** | Rotates the start of the pie chart degrees counter-clockwise from the x-axis. |
| **`rotatelabels`** | Rotates the slice text labels to align with the wedges. |

---

## 💻 Code Example

```python
import matplotlib.pyplot as plt

# Data
x = ["c++", "java", "c sharp", "ruby"]
y = [20, 30, 50, 60]
ex = [0.0, 0.0, 0.5, 0.0]

# Plotting
plt.pie(
    y,
    labels=x,
    explode=ex,
    autopct="%0.2f%%",
    shadow=True,
    radius=0.6,
    labeldistance=2,
    startangle=90,
    textprops={"fontsize": 15},
    counterclock=False,
    wedgeprops={'linewidth': 2, 'width': 1, "edgecolor": "r"},
    center=(8, 6),
    rotatelabels=True
)

plt.legend(loc=2)
plt.show()
