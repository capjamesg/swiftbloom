# swiftbloom

An implementation of the bloom filter data structure in Python.

This data structure is ideal for applications where you want to efficiently determine whether an item is _definitely not_ in a sequence. The bloom filter cannot say with absolute certainty if a specific value is in the sequence, only whether an item is definitely not in the sequence.

## Install

You can only install `swiftbloom` from source.

To install `swiftbloom`, run:

```
git clone https://github.com/capjamesg/swiftbloom
cd swiftbloom/
pip3 install -e .
```

## Quickstart

You can:

- Create a bloom filter
- Add items to the filter
- Use the filter to check if an element is definitely not in or perhaps in the filter

### Create a filter

A filter needs a defined size. The below example creates a bloom filter with room for 1,000 elements:

```python
bloom = SwiftBloom(1000)
```

### Add items to the filter

```python
names = ["James", "Taylor", "TayTay"]

for name in names:
    bloom.add(name)
```

### Check if an item is definitely not or perhaps in the filter

```python
print(bloom.query("x"))
False
```

## License

This project is licensed under an [MIT license](LICENSE).
