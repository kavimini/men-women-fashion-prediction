import pandas as pd
class FilterProducts :
    def __init__(self, products_file,filtered_categories_ids):
        self.filter_products(products_file,filtered_categories_ids)

    def read_csv(self, products_file):
        self.products_df = pd.read_csv(products_file)   

    def filter_products_by_category(self,filtered_categories_ids):
        self.filtered_df = self.products_df[self.products_df['category_id'].isin(filtered_categories_ids)]
    
    def export_results(self):
        self.filtered_df.to_csv('men-women-fashion-prediction/data/processed/filtered_men_women_product_results.csv', index=False)

    def filter_products(self,products_file,filtered_categories_ids):
        self.read_csv(products_file) 
        self.filter_products_by_category(filtered_categories_ids)  
        self.export_results() 