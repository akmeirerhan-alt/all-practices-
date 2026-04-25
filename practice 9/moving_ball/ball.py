import pygame

class Ball:
    def __init__(self, w, h):
        self.x, self.y = w // 2, h // 2
        self.radius = 25
        self.speed = 20
        self.w, self.h = w, h

    def move(self, keys):
        # 边界检查：确保球心 + 半径不超出屏幕
        if keys[pygame.K_UP] and self.y - self.speed >= self.radius:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed <= self.h - self.radius:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x - self.speed >= self.radius:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed <= self.w - self.radius:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius) 