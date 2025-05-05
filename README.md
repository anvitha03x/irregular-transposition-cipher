# Irregular Rectangle Transposition Cipher

This Streamlit app demonstrates an encryption technique based on the Irregular Rectangle Transposition Cipher, a modified form of columnar transposition where each row begins filling from a different column as defined by a numeric key.

---

## How It Works

### Cipher Logic

Given:
- A numeric key `k = k₁ k₂ ... kₙ`, where each digit `kᵢ` specifies the starting column (1-indexed) for row `i`.
- A plaintext (only alphabetic characters, no spaces).
- A specified number of columns.

### Steps:

i. Create a grid with `len(key)` rows and `n` columns.

ii. Fill the grid row by row. For each row `i`, begin inserting characters starting at column `kᵢ`.

iii. Generate ciphertext by reading characters column by column, from top to bottom and left to right, skipping any empty cells.

---

## Example

**Input:**
- Key: `23614`
- Plaintext: `NAOBGPCHQU`
- Columns: `5`

**Step-by-step Grid Filling:**
