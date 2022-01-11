import pygame
import random

couleurs= [(0,0,0),
           (0, 255, 0), 
           (255, 0, 0), 
           (0, 255, 255), 
           (255, 255, 0), 
           (255, 165, 0), 
           (0, 0, 255), 
           (128, 0, 128)]

class Figure:
    """
    description et fonctions des figures
    """
    x = 0
    y = 0
   
    figures=[
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]#On le met sur un grid de 15
     
    def __init__(self, x:str, y:str):
        self.x = x
        self.y = y
        self.couleur = random.randint(1, len(couleurs)-1)
        self.type  = random.randint(0, len(self.figures)-1)
        self.rotation = 0
    
    def image(self):
        """
        retourner une figure choisie, sa forme et son point de rotation
        """
        return self.figures[self.type][self.rotation]
    
    def pivoter(self):
        """
        calculer l'état de rotation dans lequel se trouve la figure
        """
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        
class Game:
    """
    les principales fonctions du jeu
    """
    niveau = 2
    score = 0
    etait = "start"
    field = []
    hauteur = 0
    largeur = 0
    x = 100
    y = 60
    zoom = 20
    figure = None
    
    def __init__(self, hauteur, largeur):
        """
        spécifie des attributs et crée un champ avec 
        la taille hauteur x largeur
        """
        self.hauteur = hauteur
        self.largeur = largeur
        self.field = []
        self.score = 0
        self.etait = "start"
        for i in range(hauteur):
            nouv_ligne = []
            for j in range(largeur):
                nouv_ligne.append(0)
            self.field.append(nouv_ligne)
    
    def nouv_figure(self):
        """
        Créer une nouvelle figure et la positionner aux coordonnées (3,0)
        """
        self.figure = Figure(3, 0)
        
    def croiser(self):
        """
        vérifie si la figure actuellement en vol croise quelque chose 
        de fixe sur le terrain. Cela peut se produire lorsque la figure 
        se déplace vers la gauche, la droite, le bas ou en rotation.
        Retourne si la figure intersecte.
        """
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.hauteur - 1 or \
                            j + self.figure.x > self.largeur - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection
    
    def freeze(self):
        """
        vérifie si nous sommes autorisés à déplacer ou faire pivoter la figure. 
        S'il descend et se coupe, cela signifie que nous avons atteint le bas,
        nous devons donc « geler » la figure sur notre champ
        """
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.couleur
        self.casser_lignes()
        self.nouv_figure()
        if self.croiser():
            self.etait = "gameover"
    
    def casser_lignes(self):
        """
        regarde s'il y a des lignes horizontales pleines qui doivent être détruites. 
        Ensuite, nous créons une nouvelle figure, et si elle se croise déjà, alors 
        la partie est terminée.
        """
        lignes = 0
        for i in range(1, self.hauteur):
            zeros = 0
            for j in range(self.largeur):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lignes += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.largeur):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lignes ** 2

    def descendre(self):
        """
        Si vous cliquez sur la flèche du bas, le figure descendra plus rapidement
        """
        self.figure.y += 1
        if self.croiser():
            self.figure.y -= 1
            self.freeze()

    def aller_cote(self, dx):
        """
        Si vous cliquez sur les flèches latérales, la figure ira à gauche ou à droite
        """
        old_x = self.figure.x
        self.figure.x += dx
        if self.croiser():
            self.figure.x = old_x

    def rotate(self):
        """
        Si vous cliquez sur les flèches vers le haut, l'état de rotation de la figure changera
        """
        old_rotation = self.figure.rotation
        self.figure.pivoter()
        if self.croiser():
            self.figure.rotation = old_rotation

# Initialiser le moteur de jeu    
pygame.init()

# Définir des couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (128, 128, 128)

taille = (400, 500)
ecran = pygame.display.set_mode(taille)

pygame.display.set_caption("Tetris")

# Boucle jusqu'à ce que l'utilisateur clique sur le bouton de fermeture.
fini = False
clock = pygame.time.Clock()
fps = 25 #frames per second
game = Game(20, 10)
counter = 0

presser_bas = False

while not fini:
    if game.figure is None:
        game.nouv_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.niveau // 2) == 0 or presser_bas:
        if game.etait == "start":
            game.descendre()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                presser_bas = True
            if event.key == pygame.K_LEFT:
                game.aller_cote(-1)
            if event.key == pygame.K_RIGHT:
                game.aller_cote(1)
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                presser_bas = False

    ecran.fill(BLANC)

    for i in range(game.hauteur):
        for j in range(game.largeur):
            pygame.draw.rect(ecran, GRIS, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(ecran, couleurs[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(ecran, couleurs[game.figure.couleur],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, NOIR)
    text_game_over = font1.render("GAME OVER", True, (103, 49, 71))
    text_game_over1 = font1.render("Appuyer ESC", True, (248, 152, 128))

    ecran.blit(text, [0, 0])
    if game.etait == "gameover":
        ecran.fill(GRIS)
        ecran.blit(text_game_over, [20, 200])
        ecran.blit(text_game_over1, [25, 265])
        

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()