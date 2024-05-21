def clean_text(text):
    """Remove non-letters and convert to lowercase."""
    return ''.join([c.lower() for c in text if c.isalpha()])

def vigenere_encrypt(plaintext, key):
    """Encrypt the plaintext using Vigenère cipher with the given key."""
    key_length = len(key)
    key_indices = [ord(k) - ord('a') for k in key]
    plaintext = clean_text(plaintext)
    ciphertext = []

    for i, char in enumerate(plaintext):
        shift = key_indices[i % key_length]
        encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        ciphertext.append(encrypted_char)

    return ''.join(ciphertext)
    
def format_output(ciphertext):
    """Format the output text in groups of 8 characters, 8 groups per line."""
    chunks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    formatted_text = '\n'.join([' '.join(chunks[i:i+8]) for i in range(0, len(chunks), 8)])
    return formatted_text

def main():
    key = "qwert"
    # plaintext1 = ("Hello World, Testing")
    plaintext1 = ("The man sighed, seeming to put his thoughts in order. Then he spoke again. \"Simply stated,\" he said, \"although it's not really simple at all, my job is to transmit to you all the memories I have within me. Memories of the past." "Sir,\" Jonas said tentatively, \"I would be very interested to hear the story of your life, and to listen to your memories. \"I apologize for interrupting,\" he added quickly. The man waved his hand impatiently. \"No apologies in this room. We haven't time." "Well,\" Jonas went on, uncomfortably aware that he might be interrupting again, \"I am really interested, I don't mean that I'm not. But I don't exactly understand why it's so important. I could do some adult job in the community, and in my recreation time I could come and listen to the stories from your childhood. I'd like that. Actually,\" he added, \"I've done that already, in the House of the 6 Old. The Old like to tell about their childhoods, and it's always fun to listen.\" The man shook his head. \"No, no,\" he said. \"I'm not being clear. It's not my past, not my childhood that I must transmit to you.\" He leaned back, resting his head against the back of the upholstered chair. \"It's the memories of the whole world,\" he said with a sigh. \"Before you, before me, before the previous Receiver, and generations before him.\" Jonas frowned. \"The whole world?\" he asked. \"I don't understand. Do you mean not just us? Not just the community? Do you mean Elsewhere, too?\" He tried, in his mind, to grasp the concept. \"I'm sorry, sir. I don't understand exactly. Maybe I'm not smart enough. I don't know what you mean when you say 'the whole world' or 'generations before him.' I thought there was only us. I thought there was only now." "There's much more. There's all that goes beyond--all that is Elsewhere--and all that goes back, and back, and back. I received all of those, when I was selected. And here in this room, all alone, I re-experience them again and again. It is how wisdom comes. And how we shape our future.\" He rested for a moment, breathing deeply. \"I am so weighted with them,\" he said. Jonas felt a terrible concern for the man, suddenly. \"It's as if ... \" The man paused, seeming to search his mind for the right words of description. \"It's like going downhill through deep snow on a sled,\" he said, finally. \"At first it\'s exhilarating: the speed; the sharp, clear air; but then the snow accumulates, builds up on the runners, and you slow, you have to push hard to keep going, and--\" He shook his head suddenly, and peered at Jonas. \"That meant nothing to you, did it?\" he asked.")
    plaintext2 = ("\"Sunshine,\" he said aloud, opening his eyes. \"Good. You did get the word. That makes my job easier. Not so much explaining." "And it came from the sky." "That's right,\" the old man said. \"Just the way it used to.” \"Before Sameness. Before Climate Control,\" Jonas added. The man laughed. \"You receive well, and learn quickly. I'm very pleased with you. That's enough for today, I think. We're off to a good start.\" There was a question bothering Jonas. \"Sir,\" he said, \"The Chief Elder told me--she told everyone--and you told me, too, that it would be painful. So I was a little scared. But it didn't hurt at all. I really enjoyed it.\" He looked quizzically at the old man. The man sighed. \"I started you with memories of pleasure. My previous failure gave me the wisdom to do that.\" He took a few 6 deep breaths. \"Jonas,\" he said, \"it will be painful. But it need not be painful yet." "I'm brave. I really am.\" Jonas sat up a little straighter. The old man looked at him for a moment. He smiled. \"I can see that,\" he said. \"Well, since you asked the question--I think I have enough energy for one more transmission.” \"Lie down once more. This will be the last today.\" Jonas obeyed cheerfully. He dosed his eyes, waiting, and felt the hands again; then he felt the warmth again, the sunshine again, coming from the sky of this other consciousness that was so new to him. This time, as he lay basking in the wonderful warmth, he felt the passage of time. His real self was aware that it was only a minute or two; but his other, memory-receiving self felt hours pass in the sun. His skin began to sting. Restlessly he moved one arm, bending it, and felt a sharp pain in the crease of his inner arm at the elbow. \"Ouch,\" he said loudly, and shifted on the bed. \"Owwww,\" he said, wincing at the shift, and even moving his mouth to speak made his face hurt. He knew there was a word, but the pain kept him from grasping it. Then it ended. He opened his eyes, wincing with discomfort. \"It hurt,\" he told the man, \"and I couldn't get the word for it." "It was sunburn,\" the old man told him. \"It hurt a lot,\" Jonas said, \"but I'm glad you gave it to me. It was interesting. And now I understand better, what it meant, that there would be pain.\" The man didn't respond. He sat silently for a second. Finally he said, \"Get up, now. It's time for you to go home.\" 7 They both walked to the center of the room. \"Goodbye, sir,\" he said. \"Thank you for my first day.\" The old man nodded to him. He looked drained, and a little sad. \"Sir?\" Jonas said shyly. \"Yes? Do you have a question?" "It's just that I don't know your name. I thought you were The Receiver, but you say that now I'm The Receiver. So I don't know what to call you.\" The man had sat back down in the comfortable upholstered chair. He moved his shoulders around as if to ease away an aching sensation. He seemed terribly weary. \"Call me The Giver,\" he told Jonas.")

    ciphertext1 = vigenere_encrypt(plaintext1, key)
    ciphertext2 = vigenere_encrypt(plaintext2, key)

    formatted_ciphertext1 = format_output(ciphertext1)
    formatted_ciphertext2 = format_output(ciphertext2)

    with open('ciphertext.txt', 'w') as f:
        f.write(formatted_ciphertext1)
        
    with open('ciphertext2.txt', 'w') as f:
        f.write(formatted_ciphertext2)

    print("Program successfully encrypted the texts and saved the output.")

if __name__ == "__main__":
    main()
