import time
import sys

lyrics = [
        ("Aku...... yang jatuh cinta",0.30),
        ("Haruskah kau kuberi kesempatan",0.16),
        ("Ingin aku jadi kekasih yang baik",0.15),
        ("Berikan aku kesempatan ohhhhh",0.20),
        ("Tahukah dirimu?, tahukah hatimu?",0.15),
        ("Berulang kuketuk, aku mencintamu",0.18),
        ("Tapi dirimu tak pernah sadari",0.15),
        ("Aku...... yang jatuh cinta",0.30)
    ]
delays = [7.5, 4.5, 5, 8.5, 5.5, 5, 3.5, 3.5]
    
def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            # Calculate the time until the next line should start
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()