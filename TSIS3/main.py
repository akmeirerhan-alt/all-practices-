import pygame, sys
from persistence import load_settings, save_score

pygame.init()
pygame.mixer.init()

from ui import main_menu, enter_name, leaderboard_screen, settings_screen, game_over_screen
from racer import run_game

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

# 1. These are for ONE-TIME effects (triggered in racer.py)
sounds = {
    "crash":   pygame.mixer.Sound("sound/crash.mp3"),
    "coin":    pygame.mixer.Sound("sound/coin.mp3"),
    "powerup": pygame.mixer.Sound("sound/powerup.mp3"),
}

# 2. This is for BACKGROUND music (looped music)
# If you don't have a background music file yet, keep the line below commented out
# pygame.mixer.music.load("sound/your_actual_music_file.mp3") 

settings = load_settings()

def apply_music(s):
    # Only play if a music file is loaded and sound is enabled in settings
    if s["sound"] and pygame.mixer.music.get_busy() == False:
        try:
            # pygame.mixer.music.play(-1) # Uncomment this when you have a background.mp3
            pass 
        except pygame.error:
            pass
    else:          
        pygame.mixer.music.stop()

apply_music(settings)

while True:
    action = main_menu(screen)

    if action == "quit":
        pygame.quit()
        sys.exit()

    elif action == "leaderboard":
        leaderboard_screen(screen)

    elif action == "settings":
        settings = settings_screen(screen)
        apply_music(settings)

    elif action == "play":
        name = enter_name(screen)

        while True:
            # The 'sounds' dictionary is passed here. 
            # Inside racer.py, you should have: sounds["coin"].play() when a coin is collected.
            score, distance, coins, result = run_game(screen, settings, sounds, name)

            if result == "quit":
                pygame.quit()
                sys.exit()

            save_score(name, score, distance)

            outcome = game_over_screen(screen, score, distance, coins)

            if outcome == "retry": 
                continue
            if outcome == "menu":  
                break
            if outcome == "quit":
                pygame.quit()
                sys.exit()