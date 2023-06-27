Atmos-rng is a randomness generator based off of atmospheric noise instead of math to generate numbers, make choices, and shuffle lists. It does what you'd think it does, and can be used as an alternative to "random" and Maaayyybee "secrets" if you want something abit more special.

- Special credits to [random.org](https://random.org/).

<br>
<br>

# Installation
 > [Directly from here/this repo.]
```bash
[therealOri ~]$ pip install git+https://github.com/therealOri/atmos-rng
```

or

> [From Pypi.]
```bash
[therealOri ~]$ pip install atmos-rng
```
__ __

<br />
<br />

# Ussage and Info
```python
import atmos

if __name__ == '__main__':
    atmos.clear() # clears terminal/cmd window.
    number = atmos.randint(0, 10, 1)
    print(number)

    stuff = [69, True, False, 420, 'Apples', 'Bananas', 'Cats', 'Dogs']
    choice = atmos.choice(stuff)
    print(choice)

    scrambled = atmos.shuffle(stuff)
    print(scrambled)
```
You can find more information here: [Documentation](https://github.com/therealOri/atmos-rng/blob/main/DOCS.md).
__ __

<br />
<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
