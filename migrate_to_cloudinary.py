# migrate_to_cloudinary.py
import os
import django
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import cloudinary.uploader
from product.models import Product  # change to your actual model

for product in Product.objects.all():
    if product.image and not str(product.image).startswith('http'):
        result = cloudinary.uploader.upload(f"media/Images/{str(product.image).split('/')[-1]}")
        product.image = result['public_id']  
        product.save()
        print(f"✅ {product.slug}: {result['public_id']}")
