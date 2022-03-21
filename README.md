# wordle_helper
Small CLI to help one cheat at wordle and termo

## Installation

* Download/clone this repository, run `pip install -r requirements.txt`, run script directly with `python wordle_helper.py [options]`.

or

* Download the bundled executable and run `wordle_helper.exe [options]`.

## Usage:

Word 1:

1. Current guess: SLATE ⬜⬜⬜🟨🟨
2. Run `python wordle_helper.py -y ___te -b sla` or `wordle_helper.exe -y ___te -b sla`
3. Prints a list of possible words. Find a proper one.

```
['rebut', 'quiet', 'unmet', 'totem', 'greet', 'tweed', 'comet', 'retch', 'tiger', 'other', 'their', 'depot', 'inert', 'crept', 'retro', 'egret', 'merit', 'inter', 'inept', 'threw', 'recut', 'deter', 'rivet', 'covet', 'octet', 'erupt', 'tenet', 'edict', 'fetid', 'often', 'eight', 'event', 'outer', 'evict', 'enter', 'otter', 'tuber', 'overt', 'ether', 'timer', 'beget', 'tempo', 'debit', 'remit', 'fetch', 'thief', 'tweet', 'duvet', 'detox', 'retry', 'utter', 'debut', 'ethic', 'befit', 'token', 'entry', 'voter', 'tried', 'tenor', 'trend', 'tower', 'truer', 'erect', 'beret', 'exert', 'metro', 'theft', 'meter', 'teddy', 'tepid', 'eject', 'refit', 'begot', 'benet', 'beted', 'betid', 'beton', 'bewet', 'bidet', 'biter', 'bowet', 'brent', 'buret', 'buteo', 'chert', 'cited', 'citer', 'civet', 'coted', 'cruet', 'curet', 'cuter', 'cutey', 'demit', 'dempt', 'denet', 'devot', 'dited', 'doted', 'doter', 'drent', 'ebbet', 'educt', 'eejit', 'emmet', 'epopt', 'ergot', 'eruct', 'ettin', 'evert', 'fecht', 'fecit', 'feint', 'feted', 'fetor', 'fient', 'fouet', 'freet', 'freit', 'fumet', 'gemot', 'genet', 'getup', 'godet', 'hecht', 'hoten', 'ident', 'ither', 'jeton', 'kempt', 'ketch', 'kited', 'kiter', 'meint', 'meted', 'metho', 'metic', 'metif', 'meynt', 'miter', 'moted', 'moten', 'motet', 'motey', 'mpret', 'muted', 'muter', 'nempt', 'nepit', 'netop', 'niter', 'nonet', 'noted', 'noter', 'objet', 'ofter', 'oncet', 'opted', 'opter', 'outed', 'oxter', 'peter', 'petit', 'petri', 'pewit', 'piert', 'pipet', 'poted', 'prent', 'rebit', 'recit', 'remet', 'repot', 'retem', 'retox', 'revet', 'rewet', 'roted', 'rozet', 'techy', 'teend', 'teeny', 'teiid', 'teind', 'temed', 'tempi', 'tempt', 'tench', 'tendu', 'tenno', 'tenny', 'tenon', 'tepoy', 'terek', 'terry', 'tetri', 'teuch', 'teugh', 'tewed', 'tewit', 'theed', 'theek', 'thegn', 'theic', 'thein', 'theow', 'therm', 'thewy', 'ticed', 'tided', 'timed', 'tined', 'tired', 'titer', 'toged', 'toked', 'toker', 'toned', 'toner', 'toney', 'toped', 'topek', 'toper', 'toted', 'toter', 'towed', 'toyed', 'toyer', 'tozed', 'treck', 'treed', 'treen', 'treif', 'treyf', 'trier', 'trued', 'tryer', 'tubed', 'tuned', 'tuner', 'tupek', 'tuyer', 'tween', 'tweep', 'tweer', 'twerk', 'twerp', 'twier', 'twoer', 'twyer', 'tyned', 'typed', 'typey', 'tyred', 'unget', 'unket', 'unwet', 'upjet', 'upter', 'urent', 'uteri', 'vetch', 'vitex', 'voted', 'wecht', 'wheft', 'wited', 'wyted', 'yrent', 'zibet']
```

Word 2:

1. Current guess: MITER ⬜🟨🟨🟨🟩
2. Run `python wordle_helper.py -y _itee -k ____r -b slam` or `wordle_helper.exe -y _itee -k ____r -b slam`
3. Prints a list of possible words. Find a proper one.

```
['their']
```

Word 3:

1. Current guess: THEIR 🟩🟩🟩🟩🟩
2. Congrats! You cheated!
