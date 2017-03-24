#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import *

html = '''<html>
            <head>
            <title>Caesar</title>
            </head>
            <body>'''

html_end = '''</body>
            </html>'''

form = '''<h1>  Web Caesar </h1>
            <form>
            <label>Keyword
            <input type="text" value="keyword">
            <label>Message
            <input type="text" value="message">
            <input type=''' + encrypt'''value="translate">'''

text = encrypt('jason is so awesome', 13)

main_text = html + text + form + html_end


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
