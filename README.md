# Tetris
Il s'agit d'un simple jeu Tetris codé en utilisant la bibliothèque PyGame en Python.
- Dans le jeu, il y a sept types de figurines qui descendent du haut du plateau. 
- Ils gèlent s'ils touchent une autre figurine ou le bout du plateau.
- Si les figurines congelées au fond du plateau forment une ligne complète, la ligne disparaît, entraînant ce qui se trouve au-dessus d'elle, vers le bas.
- Le joueur utilise les flèches directionnelles pour déplacer les figurines.
- Si une figurine gelée touche le haut du plateau, le jeu se termine.

## Découpage en classes:

*Classe Figures()*
```
"""
description et fonctions des figures
"""
def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type
        self.color
        self.rotation

def image(self):
        """
        retourner une figure choisie, sa forme et son point de rotation
        """

def rotate(self):
"""
        calculer l'état de rotation dans lequel se trouve la figure
        """
```

*Classe Game:*
```
"""
    les principales fonctions du jeu
    """
    
def __init__(self, height, width):
"""
        spécifie des attributs et crée un champ avec 
        la taille hauteur x largeur
        """
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        
def new_figure(self):
 """
        Créer une nouvelle figure et la positionner aux coordonnées (3,0)
        """

def intersects(self):

def break_lines(self):

def go_space(self):

def go_down(self):

def freeze(self):

def go_side(self):

def rotate(self):

def score(self):
```
