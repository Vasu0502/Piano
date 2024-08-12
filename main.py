import pygame
import keyboard 
import tune
# Initialize pygame
pygame.init()
pygame.mixer.init()

# Path to your MP3 file
 # Replace with the name of your MP3 file

# Set up the display (necessary for pygame to process events)
screen = pygame.display.set_mode((100, 100))

# Function to play sound
def play_sound(key):
    if (pygame.mixer.music.get_busy()):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(key)
        pygame.mixer.music.play()
    else:
     pygame.mixer.music.load(key)
     pygame.mixer.music.play()


def on_key_event(event):
    # Store the key pressed in a variable
    global key
    key = event.name
    return key

# Set up a listener for key events
key=keyboard.on_press(on_key_event)

# Main loop
running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                running=False # Check if the pressed key is 'esc'
                running = False
            elif key in tune.tunes:
             play_sound(tune.tunes[key])
            else:
             print("press the correct key")


pygame.time.Clock().tick(10)

pygame.quit()