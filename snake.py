import curses
import random
import time

def main(stdscr):
    # Setup screen
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()  # Screen height and width
    w = curses.newwin(sh, sw, 0, 0)  # Create a new window
    w.timeout(100)  # Refresh every 100ms
    w.keypad(1)  # Enable arrow key input

    # Initial snake and food
    snake = [[sh//2, sw//2]]  # Start in the middle
    food = [random.randint(1, sh-2), random.randint(1, sw-2)]
    w.addch(food[0], food[1], curses.ACS_PI)  # Add food symbol

    # Initial direction
    key = curses.KEY_RIGHT
    next_key = key
    score = 0

    while True:
        # Get next key input
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Calculate new head position
        head = snake[-1]
        if key == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif key == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif key == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        else:
            continue

        # Game over if snake hits the wall or itself
        if new_head in snake or new_head[0] in [0, sh-1] or new_head[1] in [0, sw-1]:
            w.addstr(sh//2, sw//2 - 5, f"Game Over! Score: {score}")
            w.refresh()
            time.sleep(3)
            break

        # Move the snake
        snake.append(new_head)
        if new_head == food:
            # Snake eats the food
            score += 1
            food = [random.randint(1, sh-2), random.randint(1, sw-2)]
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Remove tail
            tail = snake.pop(0)
            w.addch(tail[0], tail[1], ' ')

        # Draw the snake
        w.addch(new_head[0], new_head[1], curses.ACS_CKBOARD)

if name == "__main__":
    curses.wrapper(main)