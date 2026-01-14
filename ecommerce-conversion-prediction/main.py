# Oma Tasie-Amadi
# TAC-216
# Final Project
# E-commerce conversion predictor
# This program analyses customer behaviour. Loads data, performs aggregation 
# and predicts purchase probability using KNN.

# import libraries
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import machine learning modules from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# constants for file handling
CSV = 'shoppers.csv'

class ShopAnalytics:
    """
    main engine for analysis pipeline
    """
    def __init__(self):
        """
        constructor: initialises the class attributes to None
        """
        self.df_shoppers = None 
        self.X_test = None      
        self.y_test = None      
        self.y_pred = None      
        self.model = None       
        self.scaler = None      

    def wrangle(self):
        """
        data wrangling
        loads CSV, filters columns, renames them, and removes missing values
        """
        try:
            # load raw dataset
            self.df_shoppers = pd.read_csv(CSV)

            # selecting specific columns
            cols = ['PageValues','ExitRates','ProductRelated_Duration','VisitorType','Revenue']
            self.df_shoppers = self.df_shoppers[cols]

            # rename columns to snake_case
            self.df_shoppers.rename(columns={
                'PageValues': 'page_values',
                'ExitRates': 'exit_rates',
                'ProductRelated_Duration': 'duration',
                'VisitorType': 'visitor_type',
                'Revenue': 'revenue'
            }, inplace=True)

            # drop rows with missing values
            self.df_shoppers = self.df_shoppers.dropna(axis=0)
            
            # filter malformed data
            self.df_shoppers = self.df_shoppers[self.df_shoppers['duration'] >= 0]
            print(f"Data loaded successfully. Valid sessions found: {self.df_shoppers.shape[0]}")

        except FileNotFoundError:
            print(f"Error: The file '{CSV}' was not found.")
            sys.exit()

    def computation(self):
        """
        scientific computation
        aggregate 'PageValues' by 'VisitorType'
        """
        if self.df_shoppers is None:
            return

        print("\n--- Scientific Computation ---")

        grouped = self.df_shoppers.groupby('visitor_type')
        agg_results = grouped[['page_values', 'duration']].mean()
        agg_results = agg_results.sort_values(by='page_values', ascending=False)

        print("Average Metrics by Visitor Type:")
        print(agg_results)

    def run_ml(self):
        """
        machine learning
        uses KNN classification to predict 'revenue'
        """
        print("\n--- Training Machine Learning Model (KNN) ---")

        X = self.df_shoppers[['page_values','exit_rates','duration']]
        y = self.df_shoppers['revenue'].astype(int)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

        # transform data (scaling)
        self.scaler = StandardScaler()
        self.scaler.fit(X_train)

        X_train = pd.DataFrame(self.scaler.transform(X_train), columns=X.columns)
        X_test_scaled = pd.DataFrame(self.scaler.transform(X_test), columns=X.columns)

        self.model = KNeighborsClassifier(n_neighbors=15)
        self.model.fit(X_train, y_train)

        self.y_pred = self.model.predict(X_test_scaled)
        
        # save
        self.X_test = X_test_scaled
        self.y_test = y_test

        print("Classification Report:")
        print(classification_report(self.y_test, self.y_pred))

    def visualise(self, sub_choice):
        """
        visualisation
        generates plots based on the user's specific choice from the menu
        saves to a unique filename so they don't overwrite each other
        """
        
        # determine subset based on choice passed from main
        subset_df = self.df_shoppers
        subset_name = "All_Visitors"
        
        if sub_choice == '1':
            subset_df = self.df_shoppers[self.df_shoppers['visitor_type'] == 'Returning_Visitor']
            subset_name = "Returning_Visitors"
        elif sub_choice == '2':
            subset_df = self.df_shoppers[self.df_shoppers['visitor_type'] == 'New_Visitor']
            subset_name = "New_Visitors"
        
        print(f"\nGenerating plots for: {subset_name}...")

        plt.style.use('ggplot')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # --- PLOT 1: Real Data (Blue) ---
        ax1.scatter(
            subset_df['page_values'], 
            subset_df['exit_rates'], 
            color='blue', 
            alpha=0.5,
            label='Real User Sessions'
        )
        
        ax1.set(
            title=f'Real Data: PageValue vs Exit ({subset_name})',
            xlabel='Page Value Index',
            ylabel='Exit Rate'
        )
        ax1.legend()
        ax1.grid(True)
        
        # --- PLOT 2: Predicted Data (Orange) ---
        # generate predictions specifically for this subset
        X_subset = subset_df[['page_values','exit_rates','duration']]
        y_subset_true = subset_df['revenue'].astype(int)
        
        # scale features using the trained scaler
        X_subset_scaled = self.scaler.transform(X_subset)
        X_subset_scaled = pd.DataFrame(X_subset_scaled, columns=X_subset.columns)
        
        # predict
        y_subset_pred = self.model.predict(X_subset_scaled)

        # generate confusion matrix for this subset
        cm = confusion_matrix(y_subset_true, y_subset_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Buy', 'Buy'])
        
        # colour map = Orange
        disp.plot(ax=ax2, cmap='Oranges')
        ax2.set(title=f'Predictions for {subset_name}')
        
        fig.suptitle(f'E-Commerce Analysis: {subset_name}')
        fig.tight_layout()
        
        # save
        filename = f'analysis_{subset_name}.png'
        fig.savefig(filename)
        print(f"Visualisation saved to '{filename}'")
        
        plt.close(fig)

def main():
    """
    main control function
    """
    analytics = ShopAnalytics()

    analytics.wrangle()
    analytics.computation()
    analytics.run_ml()

    # menu loop for visualisation choices
    run = True
    while run:
        print("\n--- Visualisation Menu ---")
        print("1. View Returning Visitors")
        print("2. View New Visitors")
        print("3. View All Visitors")
        print("4. Quit")
        
        choice = input("Select an option (1-4): ")

        if choice in ['1', '2', '3']:
            # pass the choice directly to the visualisation method
            analytics.visualise(choice)
        elif choice == '4':
            print("Exiting program")
            run = False
        else:
            print("Invalid selection. Please try again.")

if __name__ == '__main__':
    main()
