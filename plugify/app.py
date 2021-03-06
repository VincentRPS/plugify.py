"""
MIT License

Copyright (c) 2021-present VincentRPS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class App:
    """Represents a Plugify Application(App)
    
    .. versionadded:: 1.0.0

    Parameters
    ----------
    data: :class:`dict`
        The raw dict data
    """
    def __init__(self, data: dict):
        self.from_dict = data
    
    @property
    def name(self) -> str:
        return self.from_dict['name']
    
    @property
    def owner(self) -> str:
        return self.from_dict['owner']
    
    def verified(self) -> bool:
        return self.from_dict['verified']

    @property
    def created_at(self) -> str:
        return self.from_dict['createdAt']
