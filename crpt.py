# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 20:42:21 2016
@author: evehaa
"""

import unicodedata


class Cryptography(object):
    
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'    
    alphabet_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                      '....', '..', '.---', '-.-', '.-..', '--', '-.',
                      '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                      '...-', '.--', '-..-', '-.--', '--..']    
    alphabet_semaf = [['Z/ZW', 'ZW/Z'], ['Z/W', 'W/Z'], ['Z/NW', 'NW/Z'],
                      ['Z/N', 'N/Z'], ['Z/NO', 'NO/Z'], ['Z/O', 'O/Z'],
                      ['Z/ZO', 'ZO/Z'], ['ZW/W', 'W/ZW'], ['ZW/NW'],
                      ['ZW/N', 'N/ZW'], ['ZW/NO', 'NO/ZW'], ['N/O', 'O/N'],
                      ['ZW/O', 'O/ZW'], ['ZW/ZO', 'ZO/ZW'], ['W/NW', 'NW/W'],
                      ['W/N', 'N/W'], ['W/NO', 'NO/W'], ['W/O', 'O/W'],
                      ['W/ZO', 'ZO/W'], ['NW/N', 'N/NW'], ['NW/NO', 'NO/NW'],
                      ['N/ZO', 'ZO/N'], ['NO/O', 'O/NO'], ['NO/ZO', 'ZO/NO'],
                      ['NW/O', 'O/NW'], ['O/ZO', 'ZO/O']]
    alphabet_baudot = {
        'letters':
            {'00000': '', '00001': 'a', '00010': 'e', '00011': '/', '00100': 'y',
             '00101': 'u', '00110': 'i', '00111': 'o', '01000': 'FS', '01001': 'j',
             '01010': 'g', '01011': 'h', '01100': 'b', '01101': 'c', '01110': 'f',
             '01111': 'd', '10000': ' ', '10001': '-', '10010': 'x', '10011': 'z',
             '10100': 's', '10101': 't', '10110': 'w', '10111': 'v', '11000': '',
             '11001': 'k', '11010': 'm', '11011': 'l', '11100': 'r', '11101': 'q',
             '11110': 'n', '11111': 'p'},
        'figures':
            {'00000': '', '00001': '1', '00010': '2', '00011': '1/', '00100': '3',
             '00101': '4', '00110': '3/', '00111': '5', '01000': ' ', '01001': '6',
             '01010': '7', '01011': '^1', '01100': '8', '01101': '9', '01110': '5/',
             '01111': '0', '10000': 'LS', '10001': '.', '10010': '9/', '10011': ':',
             '10100': '7/', '10101': '^2', '10110': '?', '10111': '\'', '11000': '',
             '11001': '(', '11010': ')', '11011': '=', '11100': '-', '11101': '/',
             '11110': '€', '11111': '+'}
    }
    
    def __init__(self):
        self.encoded_text = ''
        self.decoded_text = ''
    
    def set_encoded_text(self, text):
        self.encoded_text = text.upper()
    
    def set_decoded_text(self, text):
        self.decoded_text = text.lower()
    
    def encode_vigenere(self, key, to_unicode=True):
        # Clean up the key
        local_key = self._get_clean_key(key.replace(' ', ''), to_unicode)
        
        # Get the decoded text
        decoded_text_orig = self.decoded_text
        decoded_text = decoded_text_orig.replace(' ', '')
        
        # Repeat the local key to match at least the length of the encoded text
        local_key = local_key * (len(decoded_text) // len(local_key) + 1)
        
        encoded_text = ''
        # Apply the Vigenere decyphering        
        for i in range(len(decoded_text)):
            # Determine the rotation (the position of the letter in the alphabet)
            rotation = self.alphabet_upper.index(local_key[i])
            # Encode the one character based on the given rotation
            self.set_decoded_text(decoded_text[i])
            encoded_text += self.encode_rotation(rotation)
        
        # Restore the true encoded text
        self.set_decoded_text(decoded_text_orig)
        
        return self._add_spaces(encoded_text)
    
    def decode_vigenere(self, key, to_unicode=True):
        # Clean up the key
        local_key = self._get_clean_key(key.replace(' ', ''), to_unicode)
        
        # Get the encoded text
        encoded_text_orig = self.encoded_text
        encoded_text = encoded_text_orig.replace(' ', '')
        
        # Repeat the local key to match at least the length of the encoded text
        local_key = local_key * (len(encoded_text) // len(local_key) + 1)
        
        decoded_text = ''
        # Apply the Vigenere decyphering        
        for i in range(len(encoded_text)):
            # Determine the rotation (the position of the letter in the alphabet)
            rotation = self.alphabet_upper.index(local_key[i])
            # Decipher the one character based on the given rotation
            self.set_encoded_text(encoded_text[i])
            decoded_text += self.decode_rotation(rotation)
        
        # Restore the true encoded text
        self.set_encoded_text(encoded_text_orig)
        
        return self._add_spaces(decoded_text)

    def get_vigenere_key(self):
        # Get the decoded and encoded text
        decoded_text_orig = self.decoded_text
        decoded_text = decoded_text_orig.replace(' ', '')
        encoded_text_orig = self.encoded_text
        encoded_text = encoded_text_orig.replace(' ', '')

        i = 0
        key = ''
        for i in range(0, len(decoded_text)):
            # Find the positions of the decoded and encoded letters
            pos_decoded = self.alphabet_lower.index(decoded_text[i])
            pos_encoded = self.alphabet_upper.index(encoded_text[i])
            # Determine the rotation from decoded to encoded
            if pos_encoded >= pos_decoded:
                rotation = pos_encoded - pos_decoded
            else:
                rotation = pos_encoded + 26 - pos_decoded
            # Determine the letter corresponding to the rotation
            key = key + chr(65 + rotation)
        
        # Restore the true decoded and encoded text
        self.set_decoded_text(decoded_text_orig)
        self.set_encoded_text(encoded_text_orig)

        return self._add_spaces(key)
    
    def encode_monoalphabetic(self, key, to_unicode=True):
        # Get the old and new alphabets
        alphabet_old = self.alphabet_lower
        alphabet_new = self._get_unique_key(key, to_unicode)
        
        # Apply the monoalphabetic replacement to the decoded text
        encoded_text = ''
        for char in self.decoded_text:
            if char in alphabet_old:
                encoded_text += alphabet_new[alphabet_old.index(char)]
            else:
                encoded_text += char
        
        return encoded_text
    
    def decode_monoalphabetic(self, key, to_unicode=True):
        # Get the old and new alphabets
        alphabet_old = self._get_unique_key(key, to_unicode)
        alphabet_new = self.alphabet_lower
        
        # Apply the monoalphabetic replacement to the encoded text
        decoded_text = ''
        for char in self.encoded_text:
            if char in alphabet_old:
                decoded_text += alphabet_new[alphabet_old.index(char)]
            else:
                decoded_text += char
        
        return decoded_text

    def get_monoalphabetic_key(self):
        # Get the decoded and encoded text
        decoded_text_orig = self.decoded_text
        decoded_text = self._get_clean_key(decoded_text_orig.replace(' ', '')).lower()
        encoded_text_orig = self.encoded_text
        encoded_text = self._get_clean_key(encoded_text_orig.replace(' ', ''))

        # Return an error if the decoded and encoded messages are not the same in length
        assert len(decoded_text) == len(encoded_text)

        remaining_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = '.'*26
        for i in range(0, len(encoded_text)):
            alph_position = ord(decoded_text[i]) - ord('a')
            key = key[:alph_position] + encoded_text[i].upper() + key[alph_position+1:]
            remaining_chars = remaining_chars.replace(encoded_text[i], '')
        
        # Restore the true decoded and encoded text
        self.set_decoded_text(decoded_text_orig)
        self.set_encoded_text(encoded_text_orig)

        # Return an error if there is no key (i.e. the same letter occurs at multiple positions in the key)
        key_chars = key.replace('.', '')
        assert len(key_chars) == len(set(key_chars))

        return self._add_spaces(key), remaining_chars
    
    def encode_rotation(self, rotation):
        encoded_text = ''
        for char in self.decoded_text:
            if char in self.alphabet_lower:
                encoded_text += chr((ord(char) - ord('a') + rotation) % 26 + ord('a'))
            else:
                encoded_text += char
            
        return encoded_text.upper()
    
    def decode_rotation(self, rotation):
        decoded_text = ''
        for char in self.encoded_text:
            if char in self.alphabet_upper:
                decoded_text += chr((ord(char) - ord('A') - rotation) % 26 + ord('A'))
            else:
                decoded_text += char
            
        return decoded_text.lower()
    
    def decode_playfair(self, key, to_unicode=True):
        # Get the full key alphabet
        full_key = self._get_unique_key(key, to_unicode)
        # Remove the J from the full key (same matrix cell as the I)
        fk = full_key.replace('J', '')
        
        # Make the matrix
        matrix = self._key_to_matrix(fk)
        
        # Replace all J's in the original text by an I (same matrix cell)
        encoded_text = self.encoded_text.replace('J', 'I').replace(' ', '')
        
        # Decode: Take groups of two letters
        decoded_text = ''
        for i in range(int(len(encoded_text)/2)):
            letter1 = encoded_text[i*2]
            letter2 = encoded_text[i*2+1]
            
            # Get the posistions in the matrix of the original letters
            letter1_row, letter1_col = self._get_matrix_location(matrix, letter1)
            letter2_row, letter2_col = self._get_matrix_location(matrix, letter2)
            
            if letter1_row == letter2_row:
                # They are in the same row: Take the letter to the left of each of the two letters
                decoded_text += matrix[letter1_row][(letter1_col-1)%5] + matrix[letter2_row][(letter2_col-1)%5]
            elif letter1_col == letter2_col:
                # They are in the same column: Take the letter to above each of the two letters
                decoded_text += matrix[(letter1_row-1)%5][letter1_col] + matrix[(letter2_row-1)%5][letter2_col]
            else:
                # They are in different rows and columns: Take the elements on the two intersections of the elements (RC)
                decoded_text += matrix[letter1_row][letter2_col] + matrix[letter2_row][letter1_col]
                            
        return decoded_text.lower()
    
    def encode_bifid(self, key, to_unicode=True):
        # Get the full key alphabet
        full_key = self._get_unique_key(key, to_unicode)
        # Remove the J from the full key (same matrix cell as the I)
        fk = full_key.replace('J', '').lower()
        
        # Make the matrix
        matrix = self._key_to_matrix(fk)
        
        # Replace all j's in the original text by an i (same matrix cell)
        decoded_text = self.decoded_text.replace('j', 'i').replace(' ', '')
        
        # Find the position of the original letters
        rows = []
        cols = []
        for i in range(len(decoded_text)):
            # Find the position of the decoded letter
            row, col = self._get_matrix_location(matrix, decoded_text[i])
            
            # Save the row and column information
            rows.append(row)
            cols.append(col)
        
        # Put the rows and columns behind one another
        positions = rows + cols
        # Every pair of two numbers is a row and a column
        rows = positions[0::2]
        cols = positions[1::2]
        
        # Encode the text with the row and column information
        encoded_text = ''
        for row, col in zip(rows, cols):
            encoded_text += matrix[row][col]
                            
        return encoded_text.upper()
    
    def decode_bifid(self, key, to_unicode=True):
        # Get the full key alphabet
        full_key = self._get_unique_key(key, to_unicode)
        # Remove the J from the full key (same matrix cell as the I)
        fk = full_key.replace('J', '')
        
        # Make the matrix
        matrix = self._key_to_matrix(fk)
        
        # Replace all J's in the original text by an I (same matrix cell)
        encoded_text = self.encoded_text.replace('J', 'I').replace(' ', '')
        
        # Find the position of the original letters
        positions = []
        for i in range(len(encoded_text)):
            # Find the position of the encoded letter
            row, col = self._get_matrix_location(matrix, encoded_text[i])
            
            # Save the row and column information
            positions.extend([row, col])
            
        # The rows are the first half of the positions, and the colums the second half
        rows = positions[0:len(encoded_text)]
        cols = positions[len(encoded_text):]
        
        # Decode the text with the row and column information
        decoded_text = ''
        for row, col in zip(rows, cols):
            decoded_text += matrix[row][col]
                            
        return decoded_text.lower()
        
    def encode_morse(self):
        alphabet_old = self.alphabet_lower
        alphabet_new = self.alphabet_morse
        
        encoded_text = ''
        for i in range(len(self.decoded_text)):
            encoded_text += alphabet_new[alphabet_old.index(self.decoded_text[i])]
                
        return encoded_text
        
    def decode_morse(self):
        alphabet_old = self.alphabet_morse
        alphabet_new = self.alphabet_lower
        
        for key, val in enumerate(alphabet_old):
            if val == self.encoded_text:
                return alphabet_new[key]
                
        return None
        
    def decode_polybius(self, coordinates):
        # Get the full key alphabet
        full_key = self._get_unique_key('')
        # Remove the K from the full key (same matrix cell as the C)
        fk = full_key.replace('K', '')
        
        # Make the matrix
        matrix = self._key_to_matrix(fk)
        
        # Decode: Take the letter at the position in the matrix
        decoded_text = ''
        for coord in coordinates:
            decoded_text += matrix[coord[0]][coord[1]]
        
        return decoded_text.replace('C', '[C/K]').lower()

    def encode_rail_fence(self, num_rails):
        message_length = len(self.decoded_text)
        new_positions = []
        
        # Determine the new positions of the items in the list
        for i in range(num_rails):
            for j in range(round(message_length/num_rails)+1):
                pos1 = 2 * j * (num_rails - 1) - i
                pos2 = 2 * j * (num_rails - 1) + i
                

                if (pos1 < message_length) and (pos1 >= 0):
                    new_positions.append(pos1)
                else:
                    pass                
                
                if (pos2 < message_length) and (i < num_rails-1) and (i > 0):
                    new_positions.append(pos2)
                else:
                    pass      
        
        # Reorder the letters
        encoded_text = ''
        for i in range(message_length):
            encoded_text += self.decoded_text[new_positions[i]]
            
        return encoded_text.upper()

    def decode_rail_fence(self, num_rails):
        message_length = len(self.encoded_text)
        original_positions = []
        
        # Determine the original positions of the items in the list
        for i in range(num_rails):
            for j in range(round(message_length/num_rails)+1):
                pos1 = 2 * j * (num_rails - 1) - i
                pos2 = 2 * j * (num_rails - 1) + i
                

                if (pos1 < message_length) and (pos1 >= 0):
                    original_positions.append(pos1)
                else:
                    pass                
                
                if (pos2 < message_length) and (i < num_rails-1) and (i > 0):
                    original_positions.append(pos2)
                else:
                    pass      
        
        # Reorder the letters
        decoded_text = ''
        for i in range(message_length):
            decoded_text += self.encoded_text[original_positions.index(i)]
            
        return decoded_text.lower()

    def encode_atbash(self):
        # Replace a by Z, b by Y, etc.
        encoded_text = ''
        for char in self.decoded_text:
            letter_num = ord(char) - ord('a') + 1
            encoded_text += char(ord('A') + 26 - letter_num) 
        
        return encoded_text

    def decode_atbash(self):
        # Replace A by z, B by y, etc.
        decoded_text = ''
        for char in self.encoded_text:
            letter_num = ord(char) - ord('A') + 1
            decoded_text += chr(ord('a') + 26 - letter_num) 
        
        return decoded_text

    def decode_baudot(self, lsb_or_msb='msb'):
        # Make sure the stream only contains ones and zeros
        assert len(self.encoded_text.replace('0', '').replace('1', '')) == 0
        # Split the stream in blocks of five numbers
        assert len(self.encoded_text) % 5 == 0
        signs = [self.encoded_text[i:i+5] for i in range(0, len(self.encoded_text), 5)]

        decoded_text = ''
        alphabet = 'letters'
        for sign in signs:
            # Reverse the sign if we need to look right to left
            if lsb_or_msb.lower() == 'lsb':
                sign = sign[::-1]
          
            decoded_char = self.alphabet_baudot[alphabet][sign]
            if decoded_char == 'FS':
                alphabet = 'figures'
            elif decoded_char == 'LS':
                alphabet = 'letters'
            else:
                decoded_text += decoded_char

        return decoded_text 
            
    def _get_unique_key(self, key, to_unicode=True):
        local_key = self._get_clean_key(key, to_unicode)
                    
        # Construct the old alphabet based on the key
        unique_key = ''
        unique_key_rem = self.alphabet_upper
        
        # Add all unique letters of the key, in order
        for char in local_key.upper():
            if char not in unique_key and char in unique_key_rem:
                unique_key += char
                unique_key_rem = unique_key_rem.replace(char, '', )
        
        # Add all letters which have not yet been used
        unique_key += unique_key_rem
        
        return unique_key
        
    def _get_clean_key(self, key, to_unicode=True):
        clean_key = key.upper()
        if to_unicode:
            clean_key = ''.join(
                (c for c in unicodedata.normalize('NFD', clean_key) 
                if unicodedata.category(c) != 'Mn'))
                    
        return clean_key
    
    def _get_matrix_location(self, matrix, element, row=None, col=None):
        if row is None and col is None:
            # Find the element in the full matrix
            for row_key, row_val in enumerate(matrix):
                for col_key, col_val in enumerate(row_val):
                    if col_val == element:
                        return row_key, col_key
        elif row is not None:
            # Find the element in a matrix column
            for row_key, row_val in enumerate(matrix):
                if row_key == row:
                    for col_key, col_val in enumerate(row_val):
                        if col_val == element:
                            return row_key, col_key
        elif col is not None:
            # Find the element in a matrix column
            for row_key, row_val in enumerate(matrix):
                for col_key, col_val in enumerate(row_val):
                    if col_key == col:
                        if col_val == element:
                            return row_key, col_key
        else:
            return None, None
    
    def _key_to_matrix(self, key):
        matrix = [
            [key[0], key[1], key[2], key[3], key[4]],
            [key[5], key[6], key[7], key[8], key[9]],
            [key[10], key[11], key[12], key[13], key[14]],
            [key[15], key[16], key[17], key[18], key[19]],
            [key[20], key[21], key[22], key[23], key[24]]
        ]
        return matrix
    
    def _add_spaces(self, message):
        spaced_message = message
        for key, char in enumerate(self.encoded_text):
            if char == ' ':
                spaced_message = spaced_message[:key] + ' ' + spaced_message[key:]
                
        return spaced_message


if __name__ == '__main__':
    pass
