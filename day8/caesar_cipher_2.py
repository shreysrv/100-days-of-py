alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift, direction_ind):
    end_text = ""
    if shift >= 26:
        shift = shift % 26
    if direction_ind == "decode":
        shift *= -1
    for char in start_text:
        index = alphabet_array.index(char)
        pos = index + shift
        end_text += alphabet_array[pos]
    return end_text


text = input("Enter word to start:")
direction = input("Enter encode/decode :")
shift_key = int(input("Enter shift key:"))

encrypted_text = caesar(text, shift_key, direction)
print(f"{direction}d text:{encrypted_text}")
