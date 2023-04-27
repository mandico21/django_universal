import csv
import io
from dataclasses import dataclass
from typing import Union

import requests
import tqdm
from django.core.management import BaseCommand

from apps.shop.models import Category, CategoryNode


@dataclass
class Categories:
    id: int
    name: str
    description: str
    parent_id: int
    slug: str


BASE_EXPORT_URL = "https://docs.google.com/spreadsheets/d/10eISEcboROasxeTOLy8PfNXevKOPj6uYigOfKRkVK3E/export?format=csv&gid=0"


def compare(income: Union[str, int, bool, None], come: Union[str, int, bool, ], update: bool):
    """Compares data"""
    if income != come:
        update = True
        return income, update
    update = update if update else False
    return come, update


def load_category():
    counter_created = 0
    counter_updated = 0
    r = requests.get(BASE_EXPORT_URL)
    iterable = io.StringIO(r.content.decode("utf-8"))
    generator = csv.DictReader(iterable)
    next(generator)

    for row in tqdm.tqdm(generator):
        income = Categories(**row)
        category = Category.objects.filter(id=income.id).first()
        if category is not None:
            category_node = CategoryNode.objects.filter(category_id=category.id).first()
            update = False
            category.name, update = compare(income.name, category.name, update)
            category.description, update = compare(income.description, category.description, update)
            category.slug, update = compare(income.slug, category.slug, update)
            category_node.parent_id, update = compare(income.parent_id, str(category_node.parent_id), update)
            if update == True:
                category.save()
                category_node.save()
                counter_updated += 1
        else:
            create_category = Category.objects.create(id=income.id,
                                                      name=income.name,
                                                      description=income.description,
                                                      slug=income.slug)
            CategoryNode.objects.create(id=income.id, category=create_category, parent_id=income.parent_id)
            counter_created += 1
    print(counter_created)
    print(counter_updated)
    return counter_created, counter_updated


class Command(BaseCommand):

    def handle(self, *args, **options):
        load_category()
