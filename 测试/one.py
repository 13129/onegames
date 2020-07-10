# -*- coding:utf-8 -*-
import pygame


class Actor(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, events, dt):
        pass


#只是方便的的动作效果。
class Shadow(Actor):
    def __init__(self, image, pos):
        # 新表面以允许表面水平alpha值 #每个像素的Alpha曲面
        tmp = pygame.Surface(image.get_rect().size)
        tmp.set_colorkey((1, 2, 3))
        tmp.fill((1, 2, 3))
        tmp.blit(image, (0, 0))
        super().__init__(tmp, pos)
        self.time = 0
        self.alpha = 255
        self.image.set_alpha(self.alpha)

    def update(self, events, dt):
        self.time += dt
        if self.time > 50:
            self.time = 0
            self.alpha -= 50
            if self.alpha < 50:
                self.kill()
            else:
                self.image.set_alpha(self.alpha)


class Player(Actor):
    def __init__(self, image, pos):
        super().__init__(image, pos)

        # 因为我们想知道是否有两次按键,,我们需要跟踪按下的最后一个按钮
        self.last_move_button = None

        #一个标志，表明我们正在运行
        self.running = False

        self.run_counter = 0

    def update(self, events, dt):

        # 这是检查是否双击的部分
        for e in events:
            if e.type == pygame.KEYDOWN:
                ticks = pygame.time.get_ticks()

                # 我们检查是否在最近500毫秒内按过相同的键
                self.running = self.last_move_button and self.last_move_button[0] == e.key and ticks - self.last_move_button[1] < 500

                # 跟踪最后按下的按钮和按键的时间
                self.last_move_button = (e.key, ticks)

        # 这是“常规”运行代码
        pressed = pygame.key.get_pressed()
        move = pygame.Vector2((0, 0))
        if pressed[pygame.K_UP]: move += (0, -1)
        if pressed[pygame.K_LEFT]: move += (-1, 0)
        if pressed[pygame.K_DOWN]: move += (0, 1)
        if pressed[pygame.K_RIGHT]: move += (1, 0)
        if move.length() > 0:
            move.normalize_ip()
        else:
            # 如果我们不动，我们就不会在奔跑
            self.running = False

        # 如果设置了运行标志，我们将以两倍的速度移动
        speed = 2 if self.running else 1

        self.pos += move * (dt / 5) * speed
        self.rect.center = self.pos

        # 只是为了方便的的动作效果。
        self.run_counter = (self.run_counter + dt) if self.running else 0
        if self.running and self.run_counter > 25:
            self.run_counter = 0
            self.groups()[0].add(Shadow(self.image, self.rect.center))


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    dt = 0

    sprites = pygame.sprite.Group(Player(pygame.image.load('地板.png').convert_alpha(), (100, 200)))

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return

        sprites.update(events, dt)
        screen.fill((30, 30, 30))
        sprites.draw(screen)

        pygame.display.update()
        dt = clock.tick(60)


if __name__ == '__main__':
    main()