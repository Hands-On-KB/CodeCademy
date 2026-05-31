#This project had to do with encoding and decoding Caesar Cipher and Vigenere Cipher messages.
enc_msg1 = "ebiil"
enc_msg2 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
enc_msg3 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."      
enc_msg4 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
enc_msg5 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

msg_to_v = "Yes, I was able to decode your message. This is a great way to practice alphabetical character and array manipulation in Python."

vig_enc_msg1 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludqwy mhfbz cza ruxzal wg zztylktoikqq!"

vig_dec_msg1 = "This has been a fun way to learn about basic ciphers and string and index manipulation in Python."

vig_key1 = "friends"
vig_key2 = "buddies"

# Convert letter to numeric position (A=0, B=1, etc.) in 
def get_letter_position(letter):
    return ord(letter.upper()) - ord('A') #Use the 0 position for A as a baseline.

# Convert numeric position back to letter
def position_to_letter(position):
    return chr(position + ord('A')) #Use the 0 position for A as a baseline.

def decode_msg(offset, msg):
    decoded_text = ""
    
    for letter in msg:
        if letter.isalpha():  
            pos = get_letter_position(letter)
            # CHANGED: We add the offset to decode this specific cipher
            new_pos = (pos + offset) % 26
            decoded_char = position_to_letter(new_pos)      
            # Keep original lowercase formatting
            if letter.islower():
                decoded_text += decoded_char.lower()
            else:
                decoded_text += decoded_char
        else:
            decoded_text += letter   
    return decoded_text

# Test both messages
print("Decoding Message 2 (Offset 10):", decode_msg(10, enc_msg2))

def msg_to_vishal(offset, msg):
  encoded_msg = ""

  for letter in msg:
    if letter.isalpha():
      pos = get_letter_position(letter)
      new_pos = (pos + offset) % 26
      encoded_char = position_to_letter(new_pos)
      encoded_msg += encoded_char
    if letter.islower():
      encoded_char = position_to_letter(new_pos)
      encoded_msg += encoded_char
    else:
      encoded_msg += letter
  return encoded_msg

print("Encoding Message to Vishal (Offset 10):", msg_to_vishal(10, msg_to_v))
print("Decoding Message 3 (Offset 10):", decode_msg(10, enc_msg3))
print("Decoding Message 4 (Offset 14):", decode_msg(14, enc_msg4))

def brute_caesar_decode(msg):
    print("\n--- Starting Brute Force Attempt ---")
    # Try every single possible shift in the 26-letter alphabet
    for offset in range(1, 26):
        # We reuse your excellent decode_msg function here
        attempt = decode_msg(offset, msg)
        print(f"Offset {offset}: {attempt}")
        print("\n")
    print("--- Brute Force Complete ---")

def decode_vigenere(msg, key):
    decoded_text = ""
    keyword_index = 0
    
    for letter in msg:
        if letter.isalpha():
            msg_pos = get_letter_position(letter)
            key_letter = key[keyword_index % len(key)]
            offset = get_letter_position(key_letter)
            new_pos = (msg_pos + offset) % 26
            decoded_char = position_to_letter(new_pos)
            if letter.islower():
                decoded_text += decoded_char.lower()
            else:
                decoded_text += decoded_char 
            keyword_index += 1
        else:
            decoded_text += letter
    return decoded_text

def encode_vigenere(msg, key):
    encoded_text = ""
    keyword_index = 0
    
    for letter in msg:
        if letter.isalpha():
            #Get the current message letter position
            msg_pos = get_letter_position(letter)
            
            #Get the current key letter position to use as our offset. We use % len(key) to make the keyword repeat over and over
            key_letter = key[keyword_index % len(key)]
            offset = get_letter_position(key_letter)
            #Using the modulo mathematical operator to make sure the shift never goes beyond the range of the English alphabet.
            new_pos = (msg_pos - offset) % 26
            encoded_char = position_to_letter(new_pos)
            if letter.islower():
                encoded_text += encoded_char.lower()
            else:
                encoded_text += encoded_char 
            keyword_index += 1
        else:
            encoded_text += letter
    return encoded_text

print(decode_vigenere(vig_enc_msg1, vig_key1))
print("Encoding Vigenere message to Vishal:", encode_vigenere(vig_dec_msg1, vig_key2))
