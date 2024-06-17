from app.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()


    def add_category(self, category):
        self.category_repository.add_category(category)

    def get_category_by_id(self, category_id):
        return self.category_repository.get_category_by_id(category_id)

    def get_all_categories(self):
        return self.category_repository.get_all_categories()

    def update_category(self, category_id, category_data):
        return self.category_repository.update_category(category_id, category_data)

    def delete_category(self, category_id):
        return self.category_repository.delete_category(category_id)
    
    def get_categories_by_post_id(self, post_id):
        return self.category_repository.get_categories_by_post_id(post_id)
    
    def add_post_to_category(self, category_id, post):
        category = self.category_repository.get_category_by_id(category_id)
        if category:
            category.posts.append(post)
            return True
        return False
    

    