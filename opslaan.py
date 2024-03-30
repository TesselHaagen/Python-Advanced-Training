import pickle


with open('emails.txt', 'r') as f:
    raw_text = f.readline()

words = raw_text.split()

with open('emails.pkl', 'wb') as f:
    pickle.dump(words, f)