from jinja2 import Template

import os

# Récupérer le chemin absolu du dossier où se trouve le script
chemin_script = os.path.dirname(os.path.abspath(__file__))
USER_NAME = "antoine"
USER_EMAIL = "monmail@xxxx.com"
# Privilégiez toujours les ouverture de fichier sur un temps limité
with open(os.path.join(chemin_script,"template.html"),"r",encoding="utf-8") as fichier_template:
    contenu_fichier_template = fichier_template.read()
    print("🔥🔥🔥 Contenu du fichier template 🔥🔥🔥")
    print(contenu_fichier_template)
    print("🔥🔥🔥 Contenu du fichier template après application (cas non admin) 🔥🔥🔥")
    template=Template(contenu_fichier_template)
    template_rempli_non_admin=template.render(
        user_name=USER_NAME,user_email=USER_EMAIL,is_admin=False
    )
    print(template_rempli_non_admin)
    print("🔥🔥🔥 Contenu du fichier template après application (cas admin) 🔥🔥🔥")
    template_rempli_admin=template.render(
        user_name=USER_NAME,user_email=USER_EMAIL,is_admin=True
    )
    print(template_rempli_admin)