def permute(original_key, permutation_table):
    permuted_key = ''
    for index in permutation_table:
        permuted_key += original_key[index - 1]
    return permuted_key

def generate_keys(initial_key):
    # Initial key permutation table (PC-1)
    pc1_table = [57, 49, 41, 33, 25, 17, 9,
                 1, 58, 50, 42, 34, 26, 18,
                 10, 2, 59, 51, 43, 35, 27,
                 19, 11, 3, 60, 52, 44, 36,
                 63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                 14, 6, 61, 53, 45, 37, 29,
                 21, 13, 5, 28, 20, 12, 4]
    
    # Left shift table for key schedule
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    # Permuted choice 2 table (PC-2)
    pc2_table = [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]
    
    # Perform initial permutation (PC-1)
    permuted_key = permute(initial_key, pc1_table)
    
    # Split the permuted key into two halves
    left_half = permuted_key[:28]
    right_half = permuted_key[28:]
    
    # Generate 16 subkeys using key schedule
    subkeys = []
    for shift in shift_table:
        # Left circular shift
        left_half = left_half[shift:] + left_half[:shift]
        right_half = right_half[shift:] + right_half[:shift]
        
        # Combine the halves
        combined_half = left_half + right_half
        
        # Perform permuted choice 2 (PC-2)
        subkey = permute(combined_half, pc2_table)
        subkeys.append(subkey)
    
    return subkeys

def main():
    # Example initial key (64 bits)
    initial_key = '0001001100110100010101110111100110011011101111001101111111110001'
    
    # Generate keys
    keys = generate_keys(initial_key)
    
    # Print the generated keys
    for i, key in enumerate(keys):
        print(f"Subkey {i+1}: {key}")

if __name__ == "__main__":
    main()
