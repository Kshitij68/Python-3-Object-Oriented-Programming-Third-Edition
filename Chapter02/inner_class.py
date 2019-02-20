def format_string(string, formatter=None):
    """Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string."""

    class DefaultFormatter:
        """Format a string in title case."""

        def format(self, string):
            """
            str.title(): splits the string, converts first letter of each item in list to upper case and joins tham back on " "
            :param string:
            :return:
            """
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


hello_string = "hello world, how are you today?"
print(" input: " + hello_string)
print("output: " + format_string(hello_string))
