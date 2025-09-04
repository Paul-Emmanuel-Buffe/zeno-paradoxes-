"""
dichotomy_pygame.py
Visualisation Pygame du paradoxe de la dichotomie.
Réutilise la fonction simulate_dichotomy de dichotomy.py.
"""

import argparse
import pygame
import sys
from paradoxe_dichotomy import dichotomy
from config import WHITE, BLACK, BLUE, GREEN, init_window

def dichotomy_pygame(total_distance=800, stop=1e-2, max_steps=1000):
    # On récupère les étapes depuis la fonction console
    steps = dichotomy(total_distance, stop, max_steps, verbose=False)

    screen, clock, font = init_window(title="Paradoxe de la Dichotomie - Zénon")
    # Grande police pour le titre
    title_font = pygame.font.SysFont("Arial", 28, bold=True)

    index = 0
    running = True

    while running:
        screen.fill((240, 240, 240))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        if index < len(steps):
            step, position, remaining = steps[index]
            index += 1
        else:
            # On reste sur la dernière étape atteinte
            step, position, remaining = steps[-1]
        # === Dessins ===
        # Ligne de parcours (plus épaisse)
        pygame.draw.line(screen, BLACK, (50, 180), ( total_distance, 180), 4)

        # Arbre (objectif) → stylisé
        pygame.draw.rect(screen, (139, 69, 19), ( total_distance , 160, 10, 50))  # tronc marron
        pygame.draw.circle(screen, GREEN, ( total_distance, 150), 25)  # feuillage

        # Pierre (plus grosse et avec bord noir)
        pygame.draw.circle(screen, BLUE, ( int(position), 180), 5)
        pygame.draw.circle(screen, BLACK, ( int(position), 180), 5, 2)

        
        ## Titre
        title_text = title_font.render("Paradoxe de la Dichotomie", True, (20, 20, 20))
        screen.blit(title_text, (50, 30))

        # Sous-texte (infos étapes)
        info_text = font.render(
            f"Étape: {step} | Position: {position:.2f}px | Reste: {remaining:.4f}px",
            True, BLACK
        )
        screen.blit(info_text, (50, 80))

        pygame.display.flip()
        clock.tick(1)  # 1 étape par seconde

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulation Pygame du paradoxe de la dichotomie")
    parser.add_argument("--distance", type=float, default=800.0, help="Distance initiale (pixels)")
    parser.add_argument("--stop", type=float, default=1e-2, help="Seuil d'arrêt (pixels)")
    parser.add_argument("--max_steps", type=int, default=1000, help="Nombre maximum d'étapes")

    args = parser.parse_args()

    dichotomy_pygame(
        total_distance=args.distance,
        stop=args.stop,
        max_steps=args.max_steps
    )
