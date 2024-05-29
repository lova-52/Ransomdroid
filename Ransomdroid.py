import os
from bs4 import BeautifulSoup

def extract_permissions(manifest_path):
    try:
        with open(manifest_path, 'rb') as file:
            content = file.read().decode('utf-8', errors='ignore')
        print(content)
        soup = BeautifulSoup(content, 'xml')
    
        permissions = [perm.get('android:name') or perm.get('name') for perm in soup.find_all('uses-permission')]
        return permissions
    except FileNotFoundError:
        print(f"File not found: {manifest_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
manifest_path = r'C:\Users\Administrator\Downloads\Dataset_\Datasets2\Adware2\1\AndroidManifest.xml'
permissions = extract_permissions(manifest_path)
print("Permissions:", permissions)

def extract_intents(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'xml')
    intents = []
    for receiver in soup.find_all('receiver'):
        for intent_filter in receiver.find_all('intent-filter'):
            actions = [action['android:name'] for action in intent_filter.find_all('action')]
            intents.extend(actions)
    return intents

# Example usage
intents = extract_intents(manifest_path)
print("Intents:", intents)

def extract_strings(strings_path):
    with open(strings_path, 'r', encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'xml')
    strings = {string['name']: string.text for string in soup.find_all('string')}
    return strings

# Example usage
strings_path = 'path/to/strings.xml'
strings = extract_strings(strings_path)
print("Strings:", strings)

def list_images(res_folder):
    images = []
    for root, _, files in os.walk(res_folder):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, file))
    return images

# Example usage
res_folder = 'path/to/res'
images = list_images(res_folder)
print("Images:", images)

