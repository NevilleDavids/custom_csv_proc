from tabulate import tabulate as tb
import pandas as pd
import sys as sys
import os as os

class CSVProcessor:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.dataframe = None
        self.selected_columns = None

    def fetch_file_path(self):
        self.file_path = input("Enter file path: ")
        print(f"File path set to: {self.file_path}")

    def load_file(self):
        if self.file_path:
            try:
                if not self.file_path:
                    raise ValueError("File path not set. Please fetch the file path first.") 
                #Set variables            
                df = pd.read_csv(self.file_path)
                self.dataframe = df
            except Exception as error_raised:
                print(f"Error loading file: {error_raised}")
        else:
            print("File path is not set. Please fetch the file path first.")

    def DisplayData(self):
        print("Columns available: \n")
                #Display Data
        for i, col in enumerate(self.dataframe.columns, 1):
                print(f"{i}. {col}")

    def DisplayDataTabulate(self):
        df = self.dataframe
        df_lim = df.head(100)
        print("Columns available: \n")
                #Display Data
        for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
        print(tb(df_lim,headers="keys", tablefmt="psql"))
        

    def select_columns(self):
        if self.file_path:
            try:
                if not self.file_path:
                    raise ValueError("File path not set. Please fetch the file path first.")
                #Display Data
                self.DisplayData()
                columns_choice = input("Enter column numbers separated by commas (e.g., 1,2,3): ")
                columns_choice = [int(col.strip()) for col in columns_choice.split(",")]
                selected_columns = [self.dataframe.columns[col - 1] for col in columns_choice]
                print("Columns selected successfully.")
                #Exporter
                export_file_name = input("Enter the export file name (without extension): ")
                self.dataframe[selected_columns].to_csv(f"{export_file_name}.csv", index=False)
                print(f"Exported selected columns to {export_file_name}.csv")
            except Exception as error_raised:
                print(f"Error loading file: {error_raised}")
        else:
            print("File path is not set. Please fetch the file path first.")

    def export_grouped_by(self):
        df = self.dataframe
        if self.file_path:
            try:
                if not self.file_path:
                    raise ValueError("File path not set. Please fetch the file path first.") 
                #Display to CLI Available Data
                self.DisplayData()
                column_choice = int(input("Enter column number to group by (e.g. 1): "))
                selected_columns = df.columns[column_choice-1]
                print("Columns selected successfully.")
                df_grouped = df.groupby(selected_columns).apply(lambda x: x)
                export_file_name = input("Enter the export file name (without extension): ")
                df_grouped.to_csv(f"{export_file_name}.csv", index=False)
                print(f"Exported selected column to {export_file_name}.csv")
            except Exception as error_raised:
                print(f"Error exporting file: {error_raised}")
                
        else:
            print("File path is not set. Please fetch the file path first.")

    def export_pivot_table(self):
        df = self.dataframe
        if self.file_path:
            try:
                if not self.file_path:
                    raise ValueError("File path not set. Please fetch the file path first.")
                #Display Data
                self.DisplayData()
                column_choice = int(input("Enter column numbers separated by commas (e.g., 1): "))
                selected_column = df.columns[column_choice-1]
                other_col = df.columns[column_choice]
                print("Columns selected successfully.")
                df_pivoted = df.groupby(selected_column)[other_col].apply(list).reset_index()
                #Exporter
                df_pivoted[other_col] = df_pivoted[other_col].apply(lambda x:x)
                export_file_name = input("Enter the export file name (without extension): ")
                df_pivoted.to_csv(f"{export_file_name}.csv", index=False)
                print(f"Exported selected columns to {export_file_name}.csv")
            except Exception as error_raised:
                print(f"Error loading file: {error_raised}")
        else:
            print("File path is not set. Please fetch the file path first.")