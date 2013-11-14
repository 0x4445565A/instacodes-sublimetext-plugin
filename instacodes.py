import sublime, sublime_plugin, re, urllib, webbrowser

class SelectionToInstacodeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sel = self.view.sel()[0]
    if not sel.empty():
      selection = urllib.parse.quote_plus(self.view.substr(sel))
      syntax = re.search('\/.*\/', self.view.settings().get('syntax')).group(0).replace('/', '')
      sendToBrowser(selection, syntax)
    else:
      print('Nothing was Selected')

class FileToInstacodeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    selection = urllib.parse.quote_plus(self.view.substr(self.view.visible_region()))
    syntax = re.search('\/.*\/', self.view.settings().get('syntax')).group(0).replace('/', '')
    sendToBrowser(selection, syntax)

def sendToBrowser(code, syntax):
  webbrowser.open('http://InstaCod.es/?post_code=' + code + '&post_lang=' + syntax)