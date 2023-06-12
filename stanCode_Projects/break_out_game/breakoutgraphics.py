"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 5        # Number of rows of bricks
BRICK_COLS = 5        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
# click_works = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset-paddle_height/2)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (window_width-ball_radius)/2, (window_height-ball_radius)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.action)
        onmousemoved(self.paddle_move)

        self.brick_number = brick_rows * brick_cols
        self.click_works = False

        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if row <= 1:
                    self.brick.fill_color = "red"
                elif row <= 3:
                    self.brick.fill_color = "orange"
                elif row <= 5:
                    self.brick.fill_color = "yellow"
                elif row <= 7:
                    self.brick.fill_color = "green"
                else:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick, col * (brick_width + brick_spacing),
                                brick_offset + row * (brick_height + brick_spacing))

    def action(self, event):
        # to make sure that subsequent clicks will have no effects on the program
        self.click_works = True
        if self.click_works:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def paddle_move(self, event):
        if event.x - self.paddle.width / 2 <= 0:
            # to make sure that the paddle doesn't move out the left side of the window
            self.paddle.x = 0
        elif event.x + self.paddle.width / 2 >= self.window.width:
            # to make sure that the paddle doesn't move out the right side of the window
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_new_vx(self, new_vx):
        self.__dx = new_vx
        return self.__dx

    def set_new_vy(self, new_vy):
        self.__dy = new_vy
        return self.__dy

    def create_ball(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)


















