"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""
from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    global NUM_LIVES
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    while True:
        if NUM_LIVES > 0:
            # to make sure that the click works in order for the program to begin
            if graphics.click_works:
                while True:
                    vx = graphics.get_vx()
                    vy = graphics.get_vy()
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        # change the direction of the speed when the ball hits the wall
                        graphics.set_new_vx(-vx)
                    if graphics.ball.y <= 0:
                        graphics.set_new_vy(-vy)
                    if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        graphics.window.remove(graphics.ball)
                        NUM_LIVES -= 1
                        graphics.click_works = False
                        break
                    # to check if the ball is hitting any object
                    for i in range(0, 2):
                        maybe_hit = graphics.window.get_object_at(graphics.ball.x+i*graphics.ball.height,
                                                                  graphics.ball.y+i*graphics.ball.height)
                        if maybe_hit is not None:
                            # if the ball hits the paddle, it bounces off
                            if maybe_hit is graphics.paddle:
                                graphics.set_new_vy(-vy)
                                graphics.ball.y = graphics.paddle.y - graphics.ball.height*2
                            else:
                                # if the ball hits the brick, the brick disappears
                                graphics.window.remove(maybe_hit)
                                # change the direction of the speed when the ball hits something
                                graphics.set_new_vy(-vy)
                    graphics.ball.move(graphics.get_vx(), graphics.get_vy())
                    pause(FRAME_RATE)
                if NUM_LIVES > 0:
                    graphics.window.remove(graphics.ball)
                    graphics.create_ball()
                if NUM_LIVES == 0:
                    game_over = GLabel('Game Over.')
                    game_over.font = '-40'
                    graphics.window.add(game_over, graphics.window.width / 2 - game_over.width / 2,
                                        graphics.window.height / 2 + game_over.height)
                # if graphics.brick_number == 0:
                #     win = GLabel('You Win!')
                #     win.font = '-40'
                #     graphics.window.add(win, (graphics.window.width - win.width) / 2,
                #                         (graphics.window.height + win.height) / 2)
                #     graphics.window.remove(graphics.paddle)
                #     graphics.window.remove(graphics.ball)

        else:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
