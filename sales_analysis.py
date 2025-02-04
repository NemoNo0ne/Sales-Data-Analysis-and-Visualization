import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class CSVLoader:
    """Загружает данные из CSV-файла"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read(self):
        """Читает файл и возвращает DataFrame"""
        self.data = pd.read_csv(self.file_path)
        print("Файл загружен")
        return self.data


class SalesAnalyzer:
    """Считает метрики и анализирует данные"""

    def __init__(self, data):
        self.data = data

    def get_metrics(self):
        """Общий объём продаж, сумма выручки и средняя дневная выручка"""
        total_sales = self.data['quantity'].sum()
        total_revenue = self.data['revenue'].sum()
        avg_daily_revenue = self.data.groupby('date')['revenue'].sum().mean()
        print("Продано всего:", total_sales)
        print("Выручка всего:", total_revenue)
        print("Средняя дневная выручка:", round(avg_daily_revenue, 2))
        return total_sales, total_revenue, avg_daily_revenue

    def top_selling(self):
        """Самые популярные товары по количеству продаж"""
        top_products = self.data.groupby('product_id')['quantity'].sum().sort_values(ascending=False)
        print("\nТОП-товары по продажам:")
        print(top_products)
        return top_products

    def daily_revenue(self):
        """Выручка по дням"""
        revenue_per_day = self.data.groupby('date')['revenue'].sum()
        print("\nВыручка по дням:")
        print(revenue_per_day)
        return revenue_per_day


class SalesPlotter:
    """Рисует графики на основе данных"""

    def __init__(self, daily_revenue, top_products):
        self.daily_revenue = daily_revenue
        self.top_products = top_products

    def show(self):
        """Выручка по дням + топ товаров в одной панели"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # График дневной выручки
        axes[0].plot(self.daily_revenue.index, self.daily_revenue.values, marker='o', color='b')
        axes[0].set_title("Выручка по дням")
        axes[0].set_xlabel("Дата")
        axes[0].set_ylabel("Выручка")
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].grid()

        # Гистограмма топ-товаров
        sns.barplot(x=self.top_products.index, y=self.top_products.values, ax=axes[1], palette="viridis",
                    hue=self.top_products.index, dodge=False)
        axes[1].set_title("Топ товаров по продажам")
        axes[1].set_xlabel("ID товара")
        axes[1].set_ylabel("Продано единиц")
        axes[1].legend().remove()

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # 1. Загружаем файл
    file_path = 'sales_data.csv'
    loader = CSVLoader(file_path)
    data = loader.read()

    # 2. Анализируем данные
    analyzer = SalesAnalyzer(data)
    total_sales, total_revenue, avg_daily_revenue = analyzer.get_metrics()
    top_products = analyzer.top_selling()
    daily_revenue = analyzer.daily_revenue()

    # 3. Рисуем графики
    plotter = SalesPlotter(daily_revenue, top_products)
    plotter.show()
