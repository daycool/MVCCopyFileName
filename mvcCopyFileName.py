import sublime, sublime_plugin, os

class MvcCopyFileNameCommand(sublime_plugin.TextCommand):
	def run(self, edit, type=''):
		
		filePath = self.view.file_name()
		fileName = os.path.basename(filePath)
		realFileName = os.path.splitext(fileName)[0]
		sublime.set_clipboard(realFileName)
		# print realFileName
		# self.view.run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName})
		# self.view.window().run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName})
		# sublime.run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName})
		if type == '':
			self.view.window().run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName})
		elif type == 'html':
			self.view.window().run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName + '.html'})
		elif type == 'js':
			self.view.window().run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName + '.js'})
		elif type == 'css':
			self.view.window().run_command('show_overlay', {"overlay": "goto", "show_files": True, "text": realFileName + '.css'})



        
