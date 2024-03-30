import pickle

with open('emails.pkl', 'rb') as f:
    words = pickle.load(f)

print(words)