
import re
import sublime
import sublime_plugin

# how to change the case of first letter of a string?
# https://stackoverflow.com/questions/4223923/how-to-change-the-case-of-first-letter-of-a-string
def upcase_first_letter(s):
    return s[0].upper() + s[1:]

def lower_first_letter(s):
    return s[0].lower() + s[1:]

class ToggleTitleCaseCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        for region in self.view.sel():

            if region.empty():
                region = self.view.word(region)

            word = self.view.substr(region)

            # print( "before: " + word )
            match = re.search('(\w)', word, flags=re.UNICODE)

            if match:
                # print( "found: " + match.group(0) )

                # how do i return a string from a regex match in python
                # https://stackoverflow.com/questions/18493677/how-do-i-return-a-string-from-a-regex-match-in-python
                if( match.group(0).istitle() ):
                    word = lower_first_letter(word)

                else:
                    word = upcase_first_letter(word)

                # print( "after: " + word)

            self.view.replace(edit, region, word)


