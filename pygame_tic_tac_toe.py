import pygame
import sys
import tic_tac_toe as ttt

# Initialize pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 3
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

class PygameTicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()
        
        # Get player names
        print("=== Pygame Tic Tac Toe ===")
        player1_name = input("Enter Player 1 name (X): ").strip() or "Player 1"
        player2_name = input("Enter Player 2 name (O): ").strip() or "Player 2"
        
        # Create game instance
        self.game = ttt.TicTacToe(player1_name, player2_name)
        self.game_over = False
        self.winner = None
        
        # Fonts
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
    def draw_grid(self):
        """Draw the tic-tac-toe grid lines"""
        self.screen.fill(WHITE)
        
        # Draw vertical lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (i * CELL_SIZE, 0), 
                           (i * CELL_SIZE, WINDOW_SIZE), 
                           LINE_WIDTH)
        
        # Draw horizontal lines
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, 
                           (0, i * CELL_SIZE), 
                           (WINDOW_SIZE, i * CELL_SIZE), 
                           LINE_WIDTH)
    
    def draw_symbols(self):
        """Draw X's and O's on the board"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                symbol = self.game.board[row][col]
                if symbol:
                    center_x = col * CELL_SIZE + CELL_SIZE // 2
                    center_y = row * CELL_SIZE + CELL_SIZE // 2
                    
                    if symbol == "X":
                        # Draw X
                        color = BLUE
                        margin = 40
                        start_x = col * CELL_SIZE + margin
                        start_y = row * CELL_SIZE + margin
                        end_x = (col + 1) * CELL_SIZE - margin
                        end_y = (row + 1) * CELL_SIZE - margin
                        
                        pygame.draw.line(self.screen, color, 
                                       (start_x, start_y), (end_x, end_y), 8)
                        pygame.draw.line(self.screen, color, 
                                       (start_x, end_y), (end_x, start_y), 8)
                    
                    elif symbol == "O":
                        # Draw O
                        color = RED
                        radius = CELL_SIZE // 2 - 40
                        pygame.draw.circle(self.screen, color, 
                                         (center_x, center_y), radius, 8)
    
    def draw_status(self):
        """Draw current player and game status"""
        if self.game_over:
            if self.winner:
                current_player_name = (self.game.player1[0] if self.winner == "X" 
                                     else self.game.player2[0])
                text = f"{current_player_name} Wins!"
                color = BLUE if self.winner == "X" else RED
            else:
                text = "It's a Draw!"
                color = GRAY
        else:
            current_player_name = (self.game.player1[0] if self.game.current_player == 1 
                                 else self.game.player2[0])
            symbol = "X" if self.game.current_player == 1 else "O"
            text = f"{current_player_name}'s turn ({symbol})"
            color = BLUE if self.game.current_player == 1 else RED
        
        # Create text surface
        text_surface = self.font_medium.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, 30))
        
        # Draw background rectangle
        bg_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(self.screen, WHITE, bg_rect)
        pygame.draw.rect(self.screen, BLACK, bg_rect, 2)
        
        self.screen.blit(text_surface, text_rect)
    
    def get_clicked_cell(self, mouse_pos):
        """Convert mouse position to grid coordinates"""
        x, y = mouse_pos
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        
        # Make sure click is within bounds
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            return row + 1, col + 1  # Convert to 1-based indexing for your game
        return None, None
    
    def handle_click(self, mouse_pos):
        """Handle mouse clicks on the game board"""
        if self.game_over:
            return
        
        row, col = self.get_clicked_cell(mouse_pos)
        if row is not None and col is not None:
            # Try to make the move
            result = self.game.move(row, col, self.game.current_player)
            
            if result != -1:  # Valid move
                # Check for win condition
                if self.game.win_condition():
                    self.game_over = True
                    self.winner = "X" if self.game.current_player == 1 else "O"
                # Check for draw
                elif self.is_board_full():
                    self.game_over = True
                    self.winner = None
                else:
                    # Switch players
                    self.game.switch_player()
    
    def is_board_full(self):
        """Check if the board is full (draw condition)"""
        for row in self.game.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def draw_restart_button(self):
        """Draw restart button when game is over"""
        if self.game_over:
            button_rect = pygame.Rect(WINDOW_SIZE // 2 - 75, WINDOW_SIZE - 60, 150, 40)
            pygame.draw.rect(self.screen, GRAY, button_rect)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2)
            
            text = self.font_small.render("Click to Restart", True, WHITE)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)
            
            return button_rect
        return None
    
    def restart_game(self):
        """Restart the game with same players"""
        player1_name = self.game.player1[0]
        player2_name = self.game.player2[0]
        self.game = ttt.TicTacToe(player1_name, player2_name)
        self.game_over = False
        self.winner = None
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        # Check if restart button was clicked
                        restart_button = self.draw_restart_button()
                        if (restart_button and 
                            restart_button.collidepoint(event.pos) and 
                            self.game_over):
                            self.restart_game()
                        else:
                            # Handle game move
                            self.handle_click(event.pos)
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        self.restart_game()
            
            # Draw everything
            self.draw_grid()
            self.draw_symbols()
            self.draw_status()
            self.draw_restart_button()
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PygameTicTacToe()
    game.run()