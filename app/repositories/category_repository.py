from app.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.categories = []
        self.next_id = 1
        # Agregar 3 categorías predefinidas
        self.add_category(Category(name='Tecnología', description='Todo sobre lo último en tecnología.'))
        self.add_category(Category(name='Salud', description='Consejos y noticias sobre salud y bienestar.'))
        self.add_category(Category(name='Estilo de vida', description='Artículos sobre estilo de vida y vivir.'))


    def add_category(self, category):
        category.id = self.next_id
        self.categories.append(category)
        self.next_id += 1
        

    def get_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category
        return None
    
    def get_all_categories(self):
        return self.categories
    
    def update_category(self, category_id, category_data):
        category = self.get_category_by_id(category_id)
        if category:
            category.name = category_data.get('name', category.name)
            category.description = category_data.get('description', category.description)
            return category
        return None
    
    def delete_category(self, category_id):
        category = self.get_category_by_id(category_id)
        if category:
            self.categories.remove(category)
            return True
        return False
    
    def get_categories_by_post_id(self, post_id):
        return [category for category in self.categories if post_id in [post.id for post in category.posts]]
