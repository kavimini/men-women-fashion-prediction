import pandas as pd
import keywords_enum as keywords
import re

class CategoriesClassifier:

    def __init__(self, categories_file):
        self.classify_categories(categories_file)

    def read_csv(self, categories_file):
        self.categories_df = pd.read_csv(categories_file)    

    def check_keywords_in_column(self, column, keywords):
        return column.str.contains(fr'\b(?:{"|".join(map(re.escape, keywords))})\b', case=False)    

    def category_classification(self):
        men_keywords = keywords.MenKeywords.get_all_values()
        women_keywords = keywords.WomenKeywords.get_all_values()
        fashion_item_keywords =keywords.FashionItemKeywords.get_all_values()
        
        men_condition = self.check_keywords_in_column(self.categories_df['category_name'], men_keywords)
        women_condition = self.check_keywords_in_column(self.categories_df['category_name'], women_keywords)
        fashion_item_condition = self.check_keywords_in_column(self.categories_df['category_name'], fashion_item_keywords)

        combined_condition = men_condition | women_condition & fashion_item_condition
        self.filtered_df = self.categories_df[combined_condition]

    def export_results(self):
        self.filtered_df[['id', 'category_name']].to_csv('men-women-fashion-prediction/data/processed/filtered_men_women_category_results.csv', index=False)

    def filter_by_category_id(self):
        return self.filtered_df['id']
    
    def classify_categories(self,categories_file):
        self.read_csv(categories_file)
        self.category_classification()
        self.export_results()
        self.filter_by_category_id()