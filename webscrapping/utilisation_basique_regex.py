import re

texte = """
<ul class="liste-cours">
    <li>Cours 1 - Architecture logicielle avancée</li>
    <li>Cours 2 - Conception orientée objet et principes SOLID</li>
    <li>Cours 3 - Tests automatisés et intégration continue</li>
</ul>
"""

# Deux groupes : le tag ouvrant et le contenu
pattern = r"(<li>)(.*?)</li>"

match = re.search(pattern, texte)
if match:
    print("Groupe 0 :", match.group(0))  # Groupe 0 : <li>Cours 1 - Architecture logicielle avancée</li>
    print("Groupe 1 :", match.group(1))  # Groupe 1 : <li>
    print("Groupe 2 :", match.group(2))  # Groupe 2 : Cours 1 - Architecture logicielle avancée