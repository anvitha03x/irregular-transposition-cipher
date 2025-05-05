import streamlit as st
import math

def create_grid(plaintext, key, n):
    r = len(key)

    # Create empty grid with spaces
    grid = [[' ' for _ in range(n)] for _ in range(r)]

    index = 0

    # Fill the grid based on key positions
    for i in range(r):
        start_pos = int(key[i]) - 1
        for j in range(start_pos, n):
            if index < len(plaintext):
                grid[i][j] = plaintext[index]
                index += 1

    return grid

def generate_ciphertext(grid):
    n = len(grid[0])
    ciphertext = ""
    for col in range(n):
        for row in grid:
            if row[col] != ' ':
                ciphertext += row[col]
    return ciphertext

def display_grid(grid):
    st.write("### Table Representation:")

    # Create table headers
    n = len(grid[0])
    headers = "| " + " | ".join([f"**{i+1}**" for i in range(n)]) + " |"
    separator = "| " + " | ".join(["---" for _ in range(n)]) + " |"
    
    # Create table rows
    table_rows = []
    for row in grid:
        table_rows.append("| " + " | ".join(row) + " |")
    
    # Combine all parts
    table_markdown = "\n".join([headers, separator] + table_rows)
    st.markdown(table_markdown)


def main():
    st.title("Irregular Rectangle Transposition Cipher")
    plaintext = st.text_input("Enter your plaintext (without spaces):")
    key = st.text_input("Enter your numeric key:")
    columns = st.number_input("Enter the number of columns:", min_value=1)

    if st.button("Encrypt"):
        if not plaintext.isalpha() or not key.isdigit():
            st.error("Please enter a valid plaintext (letters only) and a numeric key!")
            return
        
        grid = create_grid(plaintext, key, columns)
        display_grid(grid)

        # Generate Ciphertext
        ciphertext = generate_ciphertext(grid)
        st.success(f"Ciphertext: {ciphertext}")

if __name__ == "__main__":
    main()
