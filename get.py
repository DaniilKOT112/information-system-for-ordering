from database import connection


def get_category_id(categories_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT id_categories 
                FROM categories 
                WHERE name_categories = %s;
                ''', (categories_name,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
    except Exception as e:
        print(f'Ошибка: {e}')
        return None


def get_parent_category_id(parent_category_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT id_parent_category 
                FROM parent_category 
                WHERE name = %s;
                ''', (parent_category_name,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
    except Exception as e:
        print(f'Ошибка: {e}')
        return None


def get_product_id(product_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT id_product 
                FROM product 
                WHERE name = %s;
                ''', (product_name,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
    except Exception as e:
        print(f'Error: {e}')
        return None


def get_image_for_product(name_product):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT i.url
                FROM product p
                JOIN image i ON p.id_image = i.id_image
                WHERE p.name LIKE %s::text;
            ''', (name_product,))

            image_url = cursor.fetchone()

            if image_url:
                return image_url[0]

    except Exception as e:
        print(f'Error in get_image_for_product: {e}')
        return None


def get_category_for_product(product_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT C.name_categories
                FROM product P
                JOIN categories_parent_category CPC ON P.id_category = CPC.id_categories
                JOIN categories C ON CPC.id_categories = C.id_categories
                WHERE P.name = %s;
                ''', (product_name,))
            result = cursor.fetchone()
            if result:
                return result[0]
    except Exception as e:
        print(f'Ошибка: {e}')
        return None