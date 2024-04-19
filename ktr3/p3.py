import os

# Khởi tạo bản đồ game
def init_map():
    return [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-']
    ]

# Hiển thị bản đồ game
def display_map(game_map, player_pos):
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if (i, j) == player_pos:
                print('P', end=' ')
            else:
                print(game_map[i][j], end=' ')
        print()

# Xác định hướng di chuyển dựa vào phím người dùng nhập
def get_move():
    move = input("Enter your move (W/A/S/D): ").upper()
    return move

# Thay đổi vị trí Player sau mỗi lần di chuyển và kiểm tra điều kiện thắng/thua
def move_player(game_map, player_pos, move):
    x, y = player_pos
    if move == 'W':
        x -= 1
    elif move == 'S':
        x += 1
    elif move == 'A':
        y -= 1
    elif move == 'D':
        y += 1
    
    # Kiểm tra giới hạn của bản đồ
    if x < 0 or x >= len(game_map) or y < 0 or y >= len(game_map[0]):
        return player_pos
    
    # Kiểm tra ô K hoặc ô D
    if game_map[x][y] == 'K':
        print("You found the key!")
        game_map[x][y] = '-'  # Xóa chìa khóa khỏi bản đồ
    elif game_map[x][y] == 'D':
        print("Congratulations! You escaped!")
        return (-1, -1)  # Trả về vị trí (-1, -1) để kết thúc trò chơi
    
    return (x, y)

# Hàm main
def main():
    game_map = init_map()
    player_pos = (0, 0)
    key_pos = (2, 3)
    door_pos = (4, 4)
    game_map[key_pos[0]][key_pos[1]] = 'K'
    game_map[door_pos[0]][door_pos[1]] = 'D'

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        display_map(game_map, player_pos)
        move = get_move()
        os.system('cls' if os.name == 'nt' else 'clear')
        player_pos = move_player(game_map, player_pos, move)
        if player_pos == (-1, -1):
            break

# Gọi hàm main để chạy trò chơi
main()
 
 