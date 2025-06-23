import pandas as pd
from datetime import datetime

class HistoryManager:
    def __init__(self, path):
        self.path = path
        self.df = pd.DataFrame(columns=["timestamp", "expr", "result"])
        self.load()

    def load(self):
        try:
            self.df = pd.read_csv(self.path)
        except FileNotFoundError:
            pass

    def add(self, expr, result):
        row = {
            "timestamp": datetime.now().isoformat(),
            "expr": expr,
            "result": result
        }
        # Append via .loc instead of DataFrame.append()
        self.df.loc[len(self.df)] = row

    def save(self):
        self.df.to_csv(self.path, index=False)
