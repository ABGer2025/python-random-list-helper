# list_utils.py
def find_max(numbers):
    """Findet die größte Zahl in einer Liste."""
   return max(numbers) if numbers else None

def remove_duplicates(items):
    """Entfernt Duplikate aus einer Liste und gibt eine neue Liste zurück."""
    return list(set(items))