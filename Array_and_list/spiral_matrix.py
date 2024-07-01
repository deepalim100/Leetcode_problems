def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        print(f"Top: {top}, Bottom: {bottom}, Left: {left}, Right: {right}")
        
        # Traverse from left to right on the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  # Move down to the next row
        print(f"After traversing top row: {result}")

        # Traverse from top to bottom on the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  # Move left to the next column
        print(f"After traversing right column: {result}")

        if top <= bottom:
            # Traverse from right to left on the bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  # Move up to the next row
            print(f"After traversing bottom row: {result}")

        if left <= right:
            # Traverse from bottom to top on the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # Move right to the next column
            print(f"After traversing left column: {result}")

    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = spiralOrder(matrix)
print("Final Spiral order:", result)
