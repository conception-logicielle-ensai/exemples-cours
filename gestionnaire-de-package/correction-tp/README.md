# TP : Quelques questions

- Si vous ne l'avez pas fait, installez le package `helloensai` avec pip et lancez le via une commande python. 

- Consultez les projets exemples : [1](https://github.com/conception-logicielle-ensai/archi-exemple) , [2](https://github.com/conception-logicielle-ensai/exemples-cours/tree/main/gestionnaire-de-package/uv-publish), [3](https://github.com/conception-logicielle-ensai/predicat). 
Répondez aux questions suivantes : est ce que le projet détaille comment arriver sur le projet? quel est le gestionnaire de paquet privilégié pour le projet ?

## Correction

1. 
```sh
pip install helloensai
python -m helloensai
pip install helloensai==0.1.2
python -m helloensai
set WORLD="ENSAI"
python -m helloensai
```

2. 

1: `pip` => condition d'install précisée, environnement reproductible
2: `uv` => condition d'install précisée, environnement reproductible
3: `pip` => condition d'install précisée, environnement reproductible
