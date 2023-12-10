import matplotlib.pyplot as plt
from classes.command.receiver import Receiver


class CsvDisplayAppReceiver(Receiver):
    @staticmethod
    def run_display_barchart(data_frame):
        data_frame.plot(kind='bar', x='date', y='income', label='Income')
        plt.title('Income by date')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def run_display_piechart(data_frame):
        grouped_data = data_frame.groupby('ads_company')['products_sold'].sum()
        grouped_data.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Products Sold by Ads Company')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def run_display_linechart(data_frame):
        data_frame.plot(kind='line', x='date', y=['income', 'products_sold'])
        plt.title('Income and units sold')
        plt.legend(['Income', 'Products Sold'])
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def run_display_allcharts(data_frame):
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        axs[0, 0].bar(data_frame['date'], data_frame['income'], label='Income')
        axs[0, 0].set_title('Income by date')
        axs[0, 0].legend()

        grouped_data = data_frame.groupby('ads_company')['products_sold'].sum()
        axs[0, 1].pie(grouped_data, autopct='%1.1f%%', startangle=90)
        axs[0, 1].set_title('Products Sold by Ads Company')

        axs[1, 0].plot(data_frame['date'],
                       data_frame[['income', 'products_sold']])
        axs[1, 0].set_title('Income and units sold')
        axs[1, 0].legend(['Income', 'Products Sold'])

        axs[1, 1].axis('off')

        plt.setp(axs[1, 0].xaxis.get_majorticklabels(), rotation=90)
        plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=90)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def run_save_chart(data_frame, filename):
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        axs[0, 0].bar(data_frame['date'], data_frame['income'], label='Income')
        axs[0, 0].set_title('Income by date')
        axs[0, 0].legend()

        grouped_data = data_frame.groupby('ads_company')['products_sold'].sum()
        axs[0, 1].pie(grouped_data, autopct='%1.1f%%', startangle=90)
        axs[0, 1].set_title('Products Sold by Ads Company')

        axs[1, 0].plot(data_frame['date'],
                       data_frame[['income', 'products_sold']])
        axs[1, 0].set_title('Income and units sold')
        axs[1, 0].legend(['Income', 'Products Sold'])

        axs[1, 1].axis('off')

        plt.setp(axs[1, 0].xaxis.get_majorticklabels(), rotation=90)
        plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=90)

        plt.tight_layout()
        plt.savefig(filename)
