from collections import Counter, defaultdict

fp = open("data/parallel/lsc extracted/meteo_joined.lsc", "r")
lines = fp.readlines()

modifiers = []
modified_words = defaultdict(set)

for line in lines:
    glosses = line.split()
    for gloss in glosses:
        parts = gloss.split("/")
        if len(parts) > 1:
            modified_words[parts[0]] = modified_words[parts[0]].union(parts[1:])
            modifiers.extend(parts[1:])

modifiers = Counter(modifiers)
for el in modifiers.items():
    print(el)

for el in modified_words.items():
    print(el)
fp.close()
