class PositiveNumberConverter:
    regex = "([1-9]\d*)"  # noqa

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
