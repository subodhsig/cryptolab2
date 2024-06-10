# Expansion P-box (E)
expansion_permutation = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def expand(input_bits, expansion_box):
    output_bits = [input_bits[i - 1] for i in expansion_box]
    return output_bits

def get_input_bit():
    input_bit = input("Enter a 32-bit input (0s and 1s only): ")
    # Check if the input is exactly 32 bits
    if len(input_bit) != 32:
        print("Input must be 32 bits long.")
        return None
    # Check if the input consists of only 0s and 1s
    if not all(bit in ['0', '1'] for bit in input_bit):
        print("Input must consist only of 0s and 1s.")
        return None
    return [int(bit) for bit in input_bit]

def main():
    # Get input from user
    input_bits = get_input_bit()
    # If input is invalid, exit
    if input_bits is None:
        return

    # Expansion P-box (E)
    expanded_bits = expand(input_bits, expansion_permutation)
    
    print("Original 32-bit input:")
    print(''.join(map(str, input_bits)))

    print("\nExpanded 48-bit output:")
    print(''.join(map(str, expanded_bits)))

if __name__ == "__main__":
    main()
