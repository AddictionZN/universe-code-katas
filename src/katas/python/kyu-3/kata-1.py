def validate_battlefield(battleField):
    rows, cols = 10, 10
    ships = {4: 1, 3: 2, 2: 3, 1: 4}  # ship_length: number_of_ships

    def dfs(r, c, battleField):
        if r < 0 or r >= rows or c < 0 or c >= cols or battleField[r][c] != 1:
            return 0
        battleField[r][c] = -1  # Mark as visited
        size = 1

        # Check adjacent cells for contact, which is invalid
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and battleField[nr][nc] == 1:
                return -1  # Invalid due to contact

        # Continue DFS
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            size += dfs(r + dr, c + dc, battleField)

        return size

    for r in range(rows):
        for c in range(cols):
            if battleField[r][c] == 1:  # Ship found
                ship_size = dfs(r, c, battleField)

                if ship_size == -1 or ship_size not in ships or ships[ship_size] == 0:
                    return False

                ships[ship_size] -= 1  # Decrement ship count

    return all(v == 0 for v in ships.values())  # Check if all ships are used
