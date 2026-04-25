import pygame
import datetime

def rotate_center(image, angle, x, y):
    # 老师代码里没有的核心逻辑：绕中心旋转
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

def get_time_angles():
    now = datetime.datetime.now()
    # 秒针每秒 6度，分针每分 6度
    # 减去 90 是因为图片初始指向通常是 3 点钟方向
    sec_angle = -(now.second * 6) 
    min_angle = -(now.minute * 6)
    return sec_angle, min_angle