# S-box 1
s_box_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def s_box(input_bits, sbox):
    row = int(input_bits[0] * 2 + input_bits[5])
    col = int(''.join(map(str, input_bits[1:5])), 2)
    output_decimal = sbox[row][col]
    # Convert decimal to 4-bit binary
    output_bits = [int(bit) for bit in format(output_decimal, '04b')]
    return output_bits

def get_input_bit():
    input_bit = input("Enter a 6-bit input (0s and 1s only): ")
    # Check if the input is exactly 6 bits
    if len(input_bit) != 6:
        print("Input must be 6 bits long.")
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

    # S-box 1
    output_bits = s_box(input_bits, s_box_1)
    
    print("Input to S-box 1:")
    print(''.join(map(str, input_bits)))

    print("\nOutput from S-box 1:")
    print(''.join(map(str, output_bits)))

if __name__ == "__main__":
    main()
