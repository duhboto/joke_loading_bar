# joke_loading_bar

`joke_loading_bar` is a Python package that provides a fun and interactive way to display a loading bar in your command line applications. Instead of a boring progress bar, `joke_loading_bar` displays a series of jokes and puns while your application is loading, making the waiting time more enjoyable.

The package uses a JSON file containing a collection of jokes, which are randomly selected and displayed in the command line during the loading process. The jokes are color-coded and decorated with emojis to make them more engaging. The loading bar itself is also customizable, with different themes and animation styles available.

## Installation

To install `joke_loading_bar`, simply run:

```bash
pip install joke_loading_bar
```

## Usage

To use `joke_loading_bar` in your Python application, simply import the `tell_jokes` function from the package and call it during the loading process:

```python
from joke_loading_bar import tell_jokes

# Your code goes here
tell_jokes()
```

This will display the loading bar with jokes while your code runs. You can customize the appearance of the loading bar by passing arguments to the `tell_jokes` function.

## License

This package is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to modify and adapt this description as needed to fit your specific use case and audience.
