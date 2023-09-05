# Atmos Documentation
Here is where you can find a little bit more information about atmos, how to use it, and what does what, etc.
__ __

<br>
<br>

# Randint
- `randint(minimum, maximum, how_many)`

  This function allows you to generate random numbers/integers. If `how_many` is more than 1, it will retun a list of random numbers as type `int`.

<br>

# Choice
- `choice(list_of_data)`

  This function will randomly pick an item/option from a list of items/options. The types it can choose from are as follows; `list, tuple, dictionary, sets`. If a dictionary is used/passed to the function, you will get returned type `dictionary`.

> Dev Note;
>
> When working with `sets`, it is important to know that "**True**" is the same as "**1**" for some reason.
>
> https://stackoverflow.com/a/65499571/15114290

<br>

# Shuffle
- `shuffle(list_of_data)`

  This function will shuffle/move items/options around in the provided list of data. The types it can work with and shuffle are as follows; `list, tuple, dictionary, str`. It can **NOT** work with type `set` as they are based off of hashes/hash tables and can't really be shuffled around. They are also automatically ordered/sorted and would negate the shuffling.

> Dev Note;
>
> If I were to inclue sets, the only things being shuffled would potentially be the strings and or integers. I haven't messed around with it much but I just didn't like how the end result turned out was so I decided to leave sets out.
__ __

<br>

# Gen_bytes
- `gen_bytes(32)`

  This function will allow you to generate bytes. Whether or not they can be used for cryptography is yet to be determined, but you will have bytes generated based off of atmospheric noise. Argument passed to this function MUST be `<class 'int'>`.
__ __

<br>

# Gen_bits
- `gen_bits(25)`

  This function will allow you to generate random bits. It works the same if not similarly to how `secrets` works in that it will return an `int` with xyz amount of bits. The argument passed to this function MUST be `<class 'int'>`.
__ __

<br>

# Bytes_urlsafe
- `bytes_urlsafe(20)`
> Dev Note:
>
> This function can be called without passing anything to the function. It will return a base64 encoded string of `20` bytes by `default`. You can also pass `length=None` and it will do the same.

  This function will allow you to generate a base64 urlsafe encoded string of random bytes. This function will work similarly or the same-ish to [secrets.token_urlsafe](https://docs.python.org/3/library/secrets.html#secrets.token_urlsafe) in its purpose but still based off of atmospheric noise.
__ __

<br>
<br>

This documentation is not 100% set it stone and will be updated with more information, features, and changes as time goes on.
