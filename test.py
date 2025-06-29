import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Get screen info for fullscreen
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Atherosclerosis: Vessel Blockage Process")

# Colors
BACKGROUND = (15, 25, 45)
ARTERY_COLOR = (180, 60, 60)
ARTERY_LINING = (220, 200, 200)
LUMEN_COLOR = (200, 30, 30, 100)
LDL_COLOR = (255, 215, 0)  # Yellow for LDL cholesterol
VLDL_COLOR = (255, 180, 0)  # Slightly darker yellow for VLDL
IDL_COLOR = (255, 150, 0)   # Intermediate color for IDL
CHYLOMICRON_COLOR = (255, 200, 100)  # Light yellow for chylomicrons
MONOCYTE_COLOR = (70, 130, 180)  # Steel blue for monocytes
MACROPHAGE_COLOR = (100, 150, 200)  # Blue for macrophages
FOAM_CELL_COLOR = (180, 200, 230)  # Light blue for foam cells
MUSCLE_CELL_COLOR = (200, 60, 60)  # Red for smooth muscle cells
FIBROUS_COLOR = (220, 220, 220)  # Light gray for fibrous cap
PLAQUE_COLOR = (180, 140, 80)  # Tan for plaque
TEXT_COLOR = (220, 240, 255)
HIGHLIGHT_COLOR = (0, 200, 255)
SUBTITLE_COLOR = (180, 220, 255)
MEDIA_COLOR = (150, 70, 70)  # Outer layer of artery
INTIMA_COLOR = (200, 100, 100)  # Middle layer

# Fonts
title_font = pygame.font.SysFont('Arial', min(48, HEIGHT//20), bold=True)
stage_font = pygame.font.SysFont('Arial', min(32, HEIGHT//25), bold=True)
term_font = pygame.font.SysFont('Arial', min(26, HEIGHT//30))
desc_font = pygame.font.SysFont('Arial', min(22, HEIGHT//35))
small_font = pygame.font.SysFont('Arial', min(18, HEIGHT//40))

# Animation parameters
clock = pygame.time.Clock()
current_stage = 0
animation_progress = 0
stage_transition = 0
stage_descriptions = [
    "Healthy Artery: Normal blood flow with intact endothelial lining.",
    "Endothelial Injury: Damage to the inner artery wall.",
    "Lipoprotein Accumulation: LDL, VLDL, and chylomicrons penetrate the damaged endothelium.",
    "Monocyte Adhesion: Immune cells attach to the injury site.",
    "Foam Cell Formation: Macrophages engulf lipoproteins to become foam cells.",
    "Plaque Development: Foam cells accumulate and form atherosclerotic plaque.",
    "Fibrous Cap Formation: Smooth muscle cells create a protective cap over plaque.",
    "Advanced Plaque: Significant narrowing of the arterial lumen."
]

# Key components for each stage
stage_components = [
    ["Lumen", "Endothelium", "Intima", "Media"],
    ["Lumen", "Endothelium", "Intima", "Media"],
    ["Lumen", "Endothelium", "Intima", "Media", "LDL", "VLDL", "Chylomicron"],
    ["Lumen", "Endothelium", "Intima", "Media", "Monocytes"],
    ["Lumen", "Endothelium", "Intima", "Media", "Macrophage", "Foam cells"],
    ["Lumen", "Endothelium", "Intima", "Media", "Foam cells", "atherosclerotic plaque"],
    ["Lumen", "Endothelium", "Intima", "Media", "Foam cells", "atherosclerotic plaque", "Fibrous Cap"],
    ["Lumen", "Endothelium", "Intima", "Media", "Foam cells", "atherosclerotic plaque", "Fibrous Cap"]
]

# Component colors
component_colors = {
    "Lumen": LUMEN_COLOR,
    "Endothelium": ARTERY_LINING,
    "Intima": INTIMA_COLOR,
    "Media": MEDIA_COLOR,
    "LDL": LDL_COLOR,
    "VLDL": VLDL_COLOR,
    "IDL": IDL_COLOR,
    "Chylomicron": CHYLOMICRON_COLOR,
    "Chylomicron Remnants": (255, 170, 50),
    "Monocytes": MONOCYTE_COLOR,
    "Macrophage": MACROPHAGE_COLOR,
    "Foam cells": FOAM_CELL_COLOR,
    "Smooth Muscle": MUSCLE_CELL_COLOR,
    "Fibrous Cap": FIBROUS_COLOR,
    "atherosclerotic plaque": PLAQUE_COLOR,
    "VLD": VLDL_COLOR,
    "LPL": (180, 220, 100),
    "HL": (150, 200, 150)
}

class Particle:
    def __init__(self, x, y, color, radius, dx=0, dy=0, particle_type=""):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.original_color = color
        self.particle_type = particle_type
        self.target_x = x
        self.target_y = y
        self.speed = 0.01
        
    def move_toward_target(self):
        dx = (self.target_x - self.x) * self.speed
        dy = (self.target_y - self.y) * self.speed
        self.x += dx
        self.y += dy
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        # Draw particle type label for larger particles
        if self.radius > 10 and self.particle_type:
            label = small_font.render(self.particle_type, True, (10, 20, 30))
            surface.blit(label, (int(self.x) - label.get_width()//2, int(self.y) - label.get_height()//2))

def draw_artery(surface, narrowing=0, plaque_size=0):
    center_y = HEIGHT // 2
    artery_width = HEIGHT // 4 - narrowing * (HEIGHT // 10)
    
    # Draw media (outer layer)
    pygame.draw.rect(surface, MEDIA_COLOR, 
                    (WIDTH//8, center_y - artery_width//2 - 20, 
                     WIDTH * 3//4, artery_width + 40))
    
    # Draw intima (middle layer)
    pygame.draw.rect(surface, INTIMA_COLOR, 
                    (WIDTH//8 + 15, center_y - artery_width//2 - 10, 
                     WIDTH * 3//4 - 30, artery_width + 20))
    
    # Draw lumen (blood channel)
    pygame.draw.rect(surface, LUMEN_COLOR, 
                    (WIDTH//8 + 30, center_y - artery_width//2, 
                     WIDTH * 3//4 - 60, artery_width))
    
    # Draw endothelium (inner lining)
    pygame.draw.rect(surface, ARTERY_LINING, 
                    (WIDTH//8 + 30, center_y - artery_width//2, 
                     WIDTH * 3//4 - 60, 3))
    pygame.draw.rect(surface, ARTERY_LINING, 
                    (WIDTH//8 + 30, center_y + artery_width//2 - 3, 
                     WIDTH * 3//4 - 60, 3))
    
    # Draw labels for artery layers
    media_label = term_font.render("Media", True, TEXT_COLOR)
    intima_label = term_font.render("Intima", True, TEXT_COLOR)
    endothelium_label = term_font.render("Endothelium", True, TEXT_COLOR)
    lumen_label = term_font.render("Lumen", True, TEXT_COLOR)
    
    surface.blit(media_label, (WIDTH//8 - 10, center_y - artery_width//2 - 60))
    surface.blit(intima_label, (WIDTH//8 + 20, center_y - artery_width//2 - 40))
    surface.blit(endothelium_label, (WIDTH//8 + 40, center_y - artery_width//2 - 20))
    surface.blit(lumen_label, (WIDTH//8 + 50, center_y - 10))
    
    # Draw plaque if present
    if plaque_size > 0:
        plaque_height = artery_width * 0.7 * plaque_size
        plaque_width = WIDTH//10 * plaque_size
        
        pygame.draw.ellipse(surface, PLAQUE_COLOR, 
                          (WIDTH//2 - plaque_width//2, 
                           center_y - plaque_height//2, 
                           plaque_width, plaque_height))
        
        # Draw foam cells inside plaque
        for _ in range(int(15 * plaque_size)):
            x = WIDTH//2 + random.randint(-int(plaque_width//2.5), int(plaque_width//2.5))
            y = center_y + random.randint(-int(plaque_height//2.5), int(plaque_height//2.5))
            pygame.draw.circle(surface, FOAM_CELL_COLOR, (x, y), min(12, int(10 * plaque_size)))
    
    return center_y, artery_width

def draw_stage_indicator(surface):
    # Draw stage indicator at the top
    pygame.draw.rect(surface, (30, 60, 90), (0, 0, WIDTH, HEIGHT//10))
    stage_text = title_font.render("Atherosclerosis: Vessel Blockage Process", True, TEXT_COLOR)
    surface.blit(stage_text, (WIDTH // 2 - stage_text.get_width() // 2, HEIGHT//60))
    
    # Draw current stage description
    desc_text = desc_font.render(stage_descriptions[current_stage], True, SUBTITLE_COLOR)
    surface.blit(desc_text, (WIDTH // 2 - desc_text.get_width() // 2, HEIGHT//15))
    
    # Draw stage progress bar
    bar_width = WIDTH * 0.8
    bar_height = HEIGHT//100
    bar_x = (WIDTH - bar_width) // 2
    bar_y = HEIGHT//10 - HEIGHT//60
    pygame.draw.rect(surface, (50, 70, 100), (bar_x, bar_y, bar_width, bar_height), border_radius=4)
    pygame.draw.rect(surface, HIGHLIGHT_COLOR, (bar_x, bar_y, bar_width * animation_progress, bar_height), border_radius=4)
    
    # Draw stage markers
    for i in range(8):
        x = bar_x + i * (bar_width // 7)
        color = HIGHLIGHT_COLOR if i <= current_stage else (100, 130, 180)
        pygame.draw.circle(surface, color, (x, bar_y + bar_height // 2), HEIGHT//60)
        stage_num = stage_font.render(str(i+1), True, (10, 30, 50))
        surface.blit(stage_num, (x - stage_num.get_width() // 2, bar_y - HEIGHT//40))

def draw_legend(surface):
    # Draw legend box
    box_width = min(350, WIDTH//4)
    box_height = min(200, HEIGHT//5)
    pygame.draw.rect(surface, (30, 60, 90, 180), 
                    (WIDTH - box_width - 20, HEIGHT - box_height - 20, box_width, box_height), 
                    border_radius=8)
    pygame.draw.rect(surface, (80, 140, 200), 
                    (WIDTH - box_width - 20, HEIGHT - box_height - 20, box_width, box_height), 
                    2, border_radius=8)
    
    # Legend title
    legend_title = term_font.render("Key Components:", True, HIGHLIGHT_COLOR)
    surface.blit(legend_title, (WIDTH - box_width, HEIGHT - box_height - 10))
    
    # Get current components
    current_comps = stage_components[current_stage]
    
    # Draw components in two columns if needed
    half = (len(current_comps) // 2 + (1 if len(current_comps) % 2 else 0))
    
    for i, comp in enumerate(current_comps):
        if i < half:
            y_pos = HEIGHT - box_height + 20 + i * (box_height//8)
            x_pos = WIDTH - box_width + 20
        else:
            y_pos = HEIGHT - box_height + 20 + (i - half) * (box_height//8)
            x_pos = WIDTH - box_width//2
        
        pygame.draw.circle(surface, component_colors[comp], (x_pos, y_pos), HEIGHT//80)
        comp_text = small_font.render(comp, True, TEXT_COLOR)
        surface.blit(comp_text, (x_pos + 15, y_pos - comp_text.get_height()//2))

def draw_injury_site(surface, center_y, artery_width, progress):
    x = WIDTH//2
    y = center_y - artery_width//2
    
    # Draw injury as jagged line
    injury_points = []
    injury_width = artery_width * 0.5 * progress
    for i in range(15):
        offset_x = i * (injury_width // 14) - injury_width//2
        offset_y = math.sin(i * 0.8) * 5 * progress
        injury_points.append((x + offset_x, y + offset_y))
    
    if len(injury_points) > 1:
        pygame.draw.lines(surface, (255, 100, 100), False, injury_points, max(2, int(HEIGHT//150)))

def draw_enzymes(surface, center_y, artery_width, progress):
    # Draw LPL enzymes
    if progress > 0.3:
        for i in range(5):
            x = WIDTH//3 + i * (WIDTH//10)
            y = center_y - artery_width//3
            pygame.draw.circle(surface, component_colors["LPL"], (x, y), HEIGHT//80)
            if progress > 0.6:
                enzyme_label = small_font.render("LPL", True, (10, 30, 20))
                surface.blit(enzyme_label, (x - enzyme_label.get_width()//2, y - HEIGHT//40))
    
    # Draw HL enzymes
    if progress > 0.5:
        for i in range(3):
            x = WIDTH*2//3 + i * (WIDTH//15)
            y = center_y + artery_width//4
            pygame.draw.circle(surface, component_colors["HL"], (x, y), HEIGHT//80)
            if progress > 0.7:
                enzyme_label = small_font.render("HL", True, (10, 30, 20))
                surface.blit(enzyme_label, (x - enzyme_label.get_width()//2, y + HEIGHT//60))

def main():
    global current_stage, animation_progress, stage_transition
    
    # Create particles
    ldl_particles = [Particle(random.randint(WIDTH//8, WIDTH*7//8), 
                             random.randint(HEIGHT//3, HEIGHT*2//3), 
                             LDL_COLOR, max(6, HEIGHT//100), particle_type="LDL") for _ in range(8)]
    
    vldl_particles = [Particle(random.randint(WIDTH//8, WIDTH*7//8), 
                              random.randint(HEIGHT//3, HEIGHT*2//3), 
                              VLDL_COLOR, max(8, HEIGHT//90), particle_type="VLDL") for _ in range(5)]
    
    chylomicrons = [Particle(random.randint(WIDTH//8, WIDTH*7//8), 
                            random.randint(HEIGHT//3, HEIGHT*2//3), 
                            CHYLOMICRON_COLOR, max(10, HEIGHT//80), particle_type="Chylomicron") for _ in range(4)]
    
    remnants = [Particle(random.randint(WIDTH//8, WIDTH*7//8), 
               random.randint(HEIGHT//3, HEIGHT*2//3), 
               component_colors["Chylomicron Remnants"], max(7, HEIGHT//100), particle_type="Remnants") for _ in range(6)]
    
    monocytes = [Particle(random.randint(WIDTH//8, WIDTH*7//8), 
                random.randint(HEIGHT//3, HEIGHT*2//3), 
                MONOCYTE_COLOR, max(10, HEIGHT//80), particle_type="Monocyte") for _ in range(6)]
    
    macrophages = []
    foam_cells = []
    muscle_cells = [Particle(WIDTH//4 if i % 2 == 0 else WIDTH*3//4, 
                            HEIGHT//2 + random.randint(-HEIGHT//10, HEIGHT//10), 
                            MUSCLE_CELL_COLOR, max(12, HEIGHT//70), particle_type="Smooth Muscle") for i in range(6)]
    
    # Set targets for particles
    injury_x, injury_y = WIDTH//2, HEIGHT//2 - HEIGHT//8
    
    for particle in ldl_particles + vldl_particles + chylomicrons + remnants + monocytes:
        particle.target_x = injury_x
        particle.target_y = injury_y
        particle.speed = 0.02
    
    for cell in muscle_cells:
        cell.target_x = WIDTH//2
        cell.target_y = HEIGHT//2
        cell.speed = 0.015
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_stage < 7:
                    current_stage += 1
                    animation_progress = 0
                elif event.key == pygame.K_LEFT and current_stage > 0:
                    current_stage -= 1
                    animation_progress = 0
                elif event.key == pygame.K_SPACE:
                    current_stage = (current_stage + 1) % 8
                    animation_progress = 0
                elif event.key == pygame.K_0:
                    current_stage = 0
                    animation_progress = 0
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update animation progress
        animation_progress = min(1.0, animation_progress + 0.005)
        if animation_progress >= 1.0 and current_stage < 7:
            stage_transition += 1
            if stage_transition > 60:  # Wait 60 frames before next stage
                current_stage += 1
                animation_progress = 0
                stage_transition = 0
        
        # Fill background
        screen.fill(BACKGROUND)
        
        # Draw artery with narrowing based on stage
        narrowing = min(1.0, max(0, (current_stage - 4) / 4)) if current_stage > 3 else 0
        plaque_size = min(1.0, max(0, (current_stage - 4) / 4)) if current_stage > 4 else 0
        center_y, artery_width = draw_artery(screen, narrowing, plaque_size)
        
        # Draw injury site for stages 1+
        if current_stage >= 1:
            injury_progress = min(1.0, animation_progress * 2 if current_stage == 1 else 1.0)
            draw_injury_site(screen, center_y, artery_width, injury_progress)
        
        # Draw enzymes
        if current_stage >= 2:
            enzyme_progress = min(1.0, animation_progress * 2 if current_stage == 2 else 1.0)
            draw_enzymes(screen, center_y, artery_width, enzyme_progress)
        
        # Stage 2: Lipoprotein Accumulation
        if current_stage >= 2:
            lipo_progress = min(1.0, animation_progress * 2 if current_stage == 2 else 1.0)
            
            # Move and draw LDL particles
            for particle in ldl_particles:
                particle.move_toward_target()
                if lipo_progress > 0.3:
                    particle.draw(screen)
            
            # Move and draw VLDL particles
            for particle in vldl_particles:
                particle.move_toward_target()
                if lipo_progress > 0.4:
                    particle.draw(screen)
            
            # Move and draw chylomicrons
            for particle in chylomicrons:
                particle.move_toward_target()
                if lipo_progress > 0.5:
                    particle.draw(screen)
            
            # Move and draw remnants
            for particle in remnants:
                particle.move_toward_target()
                if lipo_progress > 0.6:
                    particle.draw(screen)
        
        # Stage 3: Monocyte Adhesion
        if current_stage >= 3:
            mono_progress = min(1.0, animation_progress * 2 if current_stage == 3 else 1.0)
            
            for particle in monocytes:
                particle.move_toward_target()
                if mono_progress > 0.3:
                    particle.draw(screen)
                    
                    # Draw adhesion lines
                    if mono_progress > 0.6:
                        for _ in range(2):
                            offset_x = random.randint(-5, 5)
                            offset_y = random.randint(-5, 5)
                            pygame.draw.line(screen, MONOCYTE_COLOR, 
                                            (int(particle.x), int(particle.y)), 
                                            (injury_x + offset_x, injury_y + offset_y), 
                                            max(1, HEIGHT//300))
        
        # Stage 4: Foam Cell Formation
        if current_stage >= 4:
            foam_progress = min(1.0, animation_progress * 2 if current_stage == 4 else 1.0)
            
            # Convert monocytes to macrophages
            if foam_progress > 0.3 and len(macrophages) < len(monocytes):
                for mono in monocytes:
                    dist = math.sqrt((mono.x - injury_x)**2 + (mono.y - injury_y)**2)
                    if dist < 30 and random.random() < 0.02:
                        macrophages.append(Particle(mono.x, mono.y, MACROPHAGE_COLOR, 
                                                  max(14, HEIGHT//70), particle_type="Macrophage"))
                        if mono in monocytes:  # Safety check
                            monocytes.remove(mono)
            
            # Convert macrophages to foam cells
            if foam_progress > 0.6 and len(foam_cells) < len(macrophages):
                for macro in macrophages:
                    if random.random() < 0.03:
                        foam_cells.append(Particle(macro.x, macro.y, FOAM_CELL_COLOR, 
                                                 max(16, HEIGHT//60), particle_type="Foam Cell"))
                        if macro in macrophages:  # Safety check
                            macrophages.remove(macro)
            
            # Draw macrophages and foam cells
            for cell in macrophages:
                if foam_progress > 0.3:
                    cell.draw(screen)
            
            for cell in foam_cells:
                if foam_progress > 0.6:
                    cell.draw(screen)
        
        # Stage 6: Smooth Muscle Migration
        if current_stage >= 6:
            muscle_progress = min(1.0, animation_progress * 2 if current_stage == 6 else 1.0)
            
            # Move muscle cells toward plaque
            for muscle in muscle_cells:
                muscle.move_toward_target()
                if muscle_progress > 0.3:
                    muscle.draw(screen)
            
            # Draw fibrous cap
            if muscle_progress > 0.7:
                cap_width = artery_width * 0.6 * muscle_progress
                cap_height = artery_width * 0.2
                pygame.draw.ellipse(screen, FIBROUS_COLOR, 
                                   (WIDTH//2 - cap_width//2, 
                                    center_y - cap_height//2, 
                                    cap_width, cap_height))
                
                # Draw fibrous cap label
                cap_label = term_font.render("Fibrous Cap", True, (20, 30, 40))
                screen.blit(cap_label, (WIDTH//2 - cap_label.get_width()//2, center_y - artery_width//3))
        
        # Draw stage indicator and legend
        draw_stage_indicator(screen)
        draw_legend(screen)
        
        # Draw instructions
        instructions = small_font.render("Use LEFT/RIGHT keys to navigate stages, SPACE to advance, 0 to reset, ESC to exit", True, (180, 220, 255))
        screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT - 30))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

