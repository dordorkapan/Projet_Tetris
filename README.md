# Tetris
Il s'agit d'un simple jeu Tetris codé en utilisant la bibliothèque PyGame en Python.
- Dans le jeu, il y a sept types de figurines qui descendent du haut du plateau. 
- Ils gèlent s'ils touchent une autre figurine ou le bout du plateau.
- Si les figurines congelées au fond du plateau forment une ligne complète, la ligne disparaît, entraînant ce qui se trouve au-dessus d'elle, vers le bas.
- Le joueur utilise les flèches directionnelles pour déplacer les figurines.
- Si une figurine gelée touche le haut du plateau, le jeu se termine.

## Commandes:
- ^ : Rotation des figures
- <- ou -> : déplacement a gauche et adroite des figures
- v : fait tomber les figures plus vite

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
        """
        vérifie si la figure actuellement en vol croise quelque chose 
        de fixe sur le terrain. Cela peut se produire lorsque la figure 
        se déplace vers la gauche, la droite, le bas ou en rotation.
        """
def break_lines(self):
        """
        regarde s'il y a des lignes horizontales pleines qui doivent être détruites. 
        Ensuite, nous créons une nouvelle figure, et si elle se croise déjà, alors 
        la partie est terminée.
        """
def go_down(self):
        """
        Si vous cliquez sur la flèche du bas, le figure descendra plus rapidement
        """
def freeze(self):
        """
        vérifie si nous sommes autorisés à déplacer ou faire pivoter la figure. 
        S'il descend et se coupe, cela signifie que nous avons atteint le bas,
        nous devons donc « geler » la figure sur notre champ
        """
def go_side(self):
        """
        Si vous cliquez sur les flèches latérales, la figure ira à gauche ou à droite
        """
def rotate(self):
        """
        Si vous cliquez sur les flèches vers le haut, l'état de rotation de la figure changera
        """
```

## Idées d'amélioration:
- Faire une fenêtre qui vous montrera quelle sera votre prochaine figure
- introduir plus des niveau
- enregistrer votre score le plus élevé précédent
