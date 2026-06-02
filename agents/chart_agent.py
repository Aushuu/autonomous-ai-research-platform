import os
import matplotlib.pyplot as plt


class ChartAgent:

    def generate_charts(self, topic, metrics):

        os.makedirs("charts", exist_ok=True)

        safe_topic = topic.replace(" ", "_").lower()

        labels = [
    "Advantages",
    "Challenges",
    "Future Trends",
    "Market Growth"
]
        values = list(metrics.values())

        chart_paths = []

        # ------------------
        # BAR CHART
        # ------------------

        bar_path = f"charts/{safe_topic}_bar.png"

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values)

        plt.title(f"{topic} Metrics")
        plt.ylabel("Score")

        plt.tight_layout()

        plt.savefig(bar_path)
        plt.close()

        chart_paths.append(bar_path)

        # ------------------
        # PIE CHART
        # ------------------

        pie_path = f"charts/{safe_topic}_pie.png"

        plt.figure(figsize=(6, 6))
        plt.pie(
            values,
            labels=labels,
            autopct="%1.1f%%"
        )

        plt.title(f"{topic} Distribution")

        plt.savefig(pie_path)
        plt.close()

        chart_paths.append(pie_path)

        # ------------------
        # LINE CHART
        # ------------------

        line_path = f"charts/{safe_topic}_line.png"

        plt.figure(figsize=(8, 5))
        plt.plot(
            labels,
            values,
            marker="o"
        )

        plt.title(f"{topic} Trend Analysis")
        plt.ylabel("Score")

        plt.tight_layout()

        plt.savefig(line_path)
        plt.close()

        chart_paths.append(line_path)

        return chart_paths