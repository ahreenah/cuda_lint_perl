"""This module exports the Perl -c util."""

from cuda_lint import Linter, util
from cudatext import * 


class Perl(Linter):

    """Provides an interface to perl -c"""
    cmd = None
    executable = 'perl'
    multiline = False
    syntax = ('Perl')
    regex = (
        r'(?P<stdin>.*)line (?P<line>\d+),(?P<message>.*)'
    )
    base_cmd = (
    '-c'
    )
    tempfile_suffix = 'pl'


    def split_match(self, match):
        print('plit_match')
        print(match)
   
        """Return the components of the error."""
        split_match = super(Perl, self).split_match(match)

        match, line, col, error, warning, message, near = split_match
        return match, line, 0, '', '', message, ''
        


    def cmd(self):
        print('cmd')
        """Return the command line to execute."""
        result = self.executable + ' ' + self.base_cmd

        return result
