# Initial Permutation Box (IP)
initial_permutation = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation Box (FP)
final_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def permute(input_bits, permutation_box):
    output_bits = [input_bits[i - 1] for i in permutation_box]
    return output_bits

def get_plaintext_input():
    plaintext = input("Enter the plaintext (64 bits): ")
    # Check if the input is exactly 64 bits
    if len(plaintext) != 64:
        print("Plaintext must be 64 bits long.")
        return None
    # Check if the input consists of only 0s and 1s
    if not all(bit in ['0', '1'] for bit in plaintext):
        print("Plaintext must consist only of 0s and 1s.")
        return None
    return plaintext

def main():
    # Get plaintext input from user
    plaintext = get_plaintext_input()
    # If input is invalid, exit
    if plaintext is None:
        return
    
    plaintext_bits = [int(bit) for bit in plaintext]

    # Initial Permutation (IP)
    initial_permuted = permute(plaintext_bits, initial_permutation)
    print("Initial Permutation (IP):")
    print(''.join(map(str, initial_permuted)))

    # Final Permutation (FP)
    final_permuted = permute(plaintext_bits, final_permutation)
    print("\nFinal Permutation (FP):")
    print(''.join(map(str, final_permuted)))

if __name__ == "__main__":
    main()
