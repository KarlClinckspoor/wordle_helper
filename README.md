# wordle_helper
Small CLI to help one cheat at wordle and termo

## Installation

* `pip install -r requirements.txt`

## Usage:

Word 1:

1. Current guess: SLATE ⬜⬜🟨🟨🟨
2. Run `python wordle_helper.py --yellows __ate
3. Prints a list of possible words. Find a proper one.

```
['great', 'cheat', 'pleat', 'cater', 'metal', 'asset', 'stead', 'treat', 'eclat', 'valet', 'avert', 'tamer', 'hater', 'eater', 'eaten', 'matey', 'later', 'taper', 'tread', 'steal', 'sweat', 'begat', 'steak', 'adept', 'after', 'bleat', 'alter', 'alert', 'cleat', 'facet', 'agent', 'water', 'taken', 'terra', 'petal', 'fetal', 'cadet', 'tweak', 'steam', 'wheat', 'taker', 'extra', 'ablet', 'acted', 'aglet', 'ahent', 'aleft', 'ament', 'anent', 'anted', 'antes', 'apert', 'apted', 'apter', 'armet', 'arret', 'artel', 'ashet', 'aster', 'bated', 'bates', 'bepat', 'besat', 'betas', 'caret', 'cates', 'dated', 'dater', 'dates', 'defat', 'derat', 'earnt', 'earst', 'entia', 'ethal', 'etnas', 'etyma', 'exeat', 'expat', 'fated', 'fates', 'fetas', 'fetwa', 'gated', 'gater', 'gates', 'getas', 'hated', 'hates', 'ketas', 'lacet', 'lated', 'laten', 'latex', 'lutea', 'manet', 'mated', 'mater', 'mates', 'nates', 'oaten', 'oater', 'palet', 'pated', 'paten', 'pater', 'pates', 'petar', 'ramet', 'rated', 'ratel', 'rater', 'rates', 'resat', 'retag', 'retax', 'retia', 'salet', 'sated', 'satem', 'sates', 'sceat', 'setal', 'speat', 'stean', 'stear', 'stela', 'taber', 'tabes', 'taces', 'tacet', 'taels', 'tajes', 'takes', 'talea', 'taler', 'tales', 'tamed', 'tames', 'taped', 'tapen', 'tapes', 'tapet', 'tared', 'tares', 'tased', 'taser', 'tases', 'tater', 'tates', 'taver', 'tawed', 'tawer', 'taxed', 'taxer', 'taxes', 'tegua', 'telia', 'tenia', 'tepal', 'tepas', 'terai', 'teras', 'terga', 'tesla', 'tetra', 'texas', 'theca', 'thema', 'tinea', 'toeas', 'trefa', 'trema', 'wetas', 'yates', 'zetas']
```

Word 2:

1. Current guess: CADET 🟩🟩⬜🟩🟨
2. Run `python wordle_helper.py --yellows ____t --known ca_e_
3. Prints a list of possible words. Find a proper one.

```
['cater', 'cates']
```

Word 3:

1. Current guess: CATER 🟩🟩🟩🟩🟩
2. Congrats! You cheated!
