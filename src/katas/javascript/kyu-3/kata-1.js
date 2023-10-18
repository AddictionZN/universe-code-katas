function validateBattlefield(board) {
  let submarines = 0,
    destroyers = 0,
    cruisers = 0,
    battleship = 0;

  // Helper function to check if a cell is occupied
  function isOccupied(x, y) {
    return x >= 0 && x < 10 && y >= 0 && y < 10 && board[x][y] === 1;
  }

  // DFS traversal to find and validate ships
  function dfs(x, y, visited, isHorizontal, isVertical) {
    if (!isOccupied(x, y) || visited.has(`${x},${y}`)) return 0;

    // Mark as visited
    visited.add(`${x},${y}`);

    // Check for adjacent ships diagonally, which is invalid
    if (
      isOccupied(x - 1, y - 1) ||
      isOccupied(x - 1, y + 1) ||
      isOccupied(x + 1, y - 1) ||
      isOccupied(x + 1, y + 1)
    ) {
      return -1; // Invalid placement
    }

    // Initialize variables for horizontal and vertical checks
    let horizontal = 0,
      vertical = 0;

    // Check horizontally and vertically
    if (isOccupied(x + 1, y)) {
      isHorizontal = true;
      horizontal = dfs(x + 1, y, visited, isHorizontal, isVertical);
      if (horizontal === -1) return -1;
    }
    if (isOccupied(x, y + 1)) {
      isVertical = true;
      vertical = dfs(x, y + 1, visited, isHorizontal, isVertical);
      if (vertical === -1) return -1;
    }

    // Validate if the ship is straight
    if (isHorizontal && isVertical) {
      return -1; // Invalid ship shape (non-straight)
    }

    return 1 + horizontal + vertical;
  }

  const visited = new Set();

  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      if (isOccupied(i, j) && !visited.has(`${i},${j}`)) {
        const length = dfs(i, j, visited, false, false);

        if (length === -1) return false; // Invalid placement or shape

        if (length === 1) submarines++;
        else if (length === 2) destroyers++;
        else if (length === 3) cruisers++;
        else if (length === 4) battleship++;
        else return false; // Invalid ship size
      }
    }
  }

  return (
    battleship === 1 && cruisers === 2 && destroyers === 3 && submarines === 4
  );
}
