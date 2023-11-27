import data_cleaning_categories as dcc
import filter_products  as fp

if __name__ == "__main__":

    categories_file_path = 'men-women-fashion-prediction/data/raw/amazon_categories.csv'

    classify_categories = dcc.CategoriesClassifier(categories_file_path)
    filterByCategoryId = classify_categories.filter_by_category_id()

    products_info_file_path = 'men-women-fashion-prediction/data/raw/amazon_products.csv'
    
    classify_products = fp.FilterProducts(products_info_file_path,filterByCategoryId)









