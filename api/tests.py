from django.test import TestCase

# Create your tests here.
items = [1,2,3,4,5,6,7,6,5,4,3,5,6,4,3,5,6,4]
if (length := len(items)) > 10:
    print(f"List is too long! It has {length} items.")