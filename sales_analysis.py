import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataLoader:
    """Класс для загрузки данных из CSV-файла"""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Загружает данные из CSV-файла и возвращает DataFrame"""
        self.data = pd.read_csv(self.file_path)
        print("Данные успешно загружены")
        return self.data


class DataAnalyzer:
    """Класс для анализа данных и вычисления метрик"""

    def __init__(self, data):
        self.data = data

    def calculate_metrics(self):
        """Вычисляет основные метрики: общая выручка, средняя выручка за день"""
        total_sales = self.data['quantity'].sum()  # Общее количество проданных единиц
        total_revenue = self.data['revenue'].sum()  # Общая выручка
        average_daily_revenue = self.data.groupby('date')['revenue'].sum().mean()  # Средняя выручка за день
        print("Общее количество продаж:", total_sales)
        print("Общая выручка:", total_revenue)
        print("Средняя выручка за день:", round(average_daily_revenue, 2))
        return total_sales, total_revenue, average_daily_revenue

    def get_top_products(self):
        """Возвращает список самых популярных продуктов по количеству продаж"""
        top_products = self.data.groupby('product_id')['quantity'].sum().sort_values(ascending=False)
        print("\nПопулярные продукты по количеству продаж:")
        print(top_products)
        return top_products

    def get_daily_revenue(self):
        """Возвращает таблицу выручки по дням"""
        daily_revenue = self.data.groupby('date')['revenue'].sum()
        print("\nВыручка по дням:")
        print(daily_revenue)
        return daily_revenue


class DataVisualizer:
    """Класс для визуализации данных"""

    def __init__(self, daily_revenue, top_products):
        self.daily_revenue = daily_revenue
        self.top_products = top_products

    def plot_all(self):
        """Создает графики ежедневной выручки и популярных продуктов на одной панели"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # Создаем две области для графиков на одной панели

        # Линейный график для ежедневной выручки
        axes[0].plot(self.daily_revenue.index, self.daily_revenue.values, marker='o', color='b')
        axes[0].set_title("Выручка по дням")
        axes[0].set_xlabel("Дата")
        axes[0].set_ylabel("Выручка")
        axes[0].tick_params(axis='x', rotation=45)
        axes[0].grid()

        # Гистограмма для популярных продуктов
        sns.barplot(x=self.top_products.index, y=self.top_products.values, ax=axes[1], palette="viridis",
                    hue=self.top_products.index, dodge=False)
        axes[1].set_title("Популярные продукты по количеству продаж")
        axes[1].set_xlabel("ID продукта")
        axes[1].set_ylabel("Количество проданных единиц")
        axes[1].legend().remove()  # Убираем легенду

        plt.tight_layout()  # Настраиваем отступы
        plt.show()


if __name__ == "__main__":
    # 1. Загрузка данных
    file_path = 'sales_data.csv'
    data_loader = DataLoader(file_path)
    data = data_loader.load_data()

    # 2. Анализ данных
    analyzer = DataAnalyzer(data)
    total_sales, total_revenue, average_daily_revenue = analyzer.calculate_metrics()
    top_products = analyzer.get_top_products()
    daily_revenue = analyzer.get_daily_revenue()

    # 3. Визуализация данных
    visualizer = DataVisualizer(daily_revenue, top_products)
    visualizer.plot_all()

