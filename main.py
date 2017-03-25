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
import cgi
from caesar import *


def buildPage(textarea_content):
    html = '''<html>
                <head>
                <title>Caesar</title>
                </head>
                <body bgcolor="lightblue">'''

    html_end = '''</body>
                </html>'''

    form = '''
            <div align="center">
            <h1>  Web Caesar </h1>
                <form method="POST">
                <label>Message to encrypt
                <br>
                <textarea name="message" style="height: 100px; width: 400px;">''' + textarea_content + '''
                </textarea>
                <br>
                <label>Number of times to rotate
                <br>
                <input type="number" name="rotation">
                <br>
                <input type="submit">
                </form>
            </div>'''

    main_text = html + form + html_end
    return main_text


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildPage("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotation")
        encrypted_message = encrypt(message, int(rotation))
        escaped = cgi.escape(encrypted_message)
        msg = 'Secret message:' + escaped
        content = buildPage(msg)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
