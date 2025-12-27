import os
import sys

# Путь к проекту
project_path = r'C:\Users\Admin\PycharmProjects\new life\django_sprint1\blogicum'
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')

import django
django.setup()

from django.conf import settings

print("BASE_DIR:", settings.BASE_DIR)
print("\nПроверяем путь к шаблону:")
template_path = os.path.join(settings.BASE_DIR, 'templates', 'blog', 'index.html')
print("Путь:", template_path)
print("Существует:", os.path.exists(template_path))

print("\nСодержимое templates:")
templates_dir = os.path.join(settings.BASE_DIR, 'templates')
if os.path.exists(templates_dir):
    for root, dirs, files in os.walk(templates_dir):
        level = root.replace(templates_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{subindent}{file}')