import sublime, sublime_plugin, os, sys

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

class MouseLeftClickCommand(sublime_plugin.TextCommand):
	def run(self, edit, type=''):
		# print self.view.sel()[0]
		# print self.view.word(self.view.sel()[0])
		# print self.view.substr(self.view.sel()[0])
		
			# print wordEnd
			# print lineEnd
			# print currLineStr
			# print urlStartIndex
			# print urlEndIndex
		url = self.getQuoteContent()
		
		if(len(url) > 0):
			url = self.getFormatUrl(url)
			if(os.path.isfile(url)):
				self.view.window().open_file(url)
				print 'open file'
		# self.view.window().open_file('D:\weimi\git\uedprojects\op17shihui\shihui\index.html')
	
		
	def getQuoteContent(self):
		sel = self.view.sel()[0]
		lineRegion = self.view.line(sel)
		wordRegion = self.view.word(sel)
		totalSize = self.view.size()
		currLineStr = self.view.substr(lineRegion)
		# print currLineStr;
		lineLen = len(currLineStr)
		lineStart = lineRegion.begin()
		lineEnd = lineRegion.end()
		wordStart = wordRegion.begin()
		wordEnd = wordRegion.end()

		lineEnd = lineEnd - lineStart
		wordStart = wordStart - lineStart
		wordEnd = wordEnd - lineStart
		lineStart = lineStart - lineStart
		url = ''
		urlStartIndex = 0
		urlEndIndex = 0

		flag = self.checkQuote(currLineStr, lineStart, wordStart)
		# print flag
		if(flag == 1):
			urlStartIndex = currLineStr.rfind("'", lineStart, wordStart) 
			urlEndIndex = currLineStr.find("'", wordEnd, lineEnd) 
			url = currLineStr[urlStartIndex+1:urlEndIndex] 
			# print url
		if(flag == 2):
			urlStartIndex = currLineStr.rfind('"', lineStart, wordStart) 
			urlEndIndex = currLineStr.find('"', wordEnd, lineEnd) 
			url = currLineStr[urlStartIndex+1:urlEndIndex]

		return url
		

	def checkQuote(self, str, start, end):
		singleQuote = str.rfind("'", start, end)
		doubleQuote = str.rfind('"', start, end)
		# print	singleQuote
		# print	doubleQuote		
		if(singleQuote == -1 and doubleQuote == -1 ):
			return 3
		elif(singleQuote >= 0 and doubleQuote >= 0):
			if(singleQuote > doubleQuote):
				return 1
			else:
				return 2
		elif(singleQuote >= 0 and doubleQuote == -1):
			return 1
		elif(doubleQuote >= 0 and singleQuote == -1):
			return 2

		return 3
		# print edit
	def getFormatUrl(self, url):
		formatUrl = ''
		projectName = 'op17shihui'
		projectPath = self.view.window().folders()[0] + '/'
		# print projectPath
		location = ''
		setting = sublime.load_settings("config.sublime-settings");
		
		segments = url.split('/')
		segment = ''
		if(len(segments) > 0):
			segment = segments[0]

		# print sublime.packages_path() + 'MVCCopyFileName\config.sublime-settings'
		if(setting.has(projectName)):
			config = setting.get(projectName)
			# print config
			# print config['packages']
			baseUrl = config.get('baseUrl')
			pkg = [p for p in config['packages'] if p['name'] == segment]
			# print pkg
			if(len(pkg) > 0):
				print pkg
				location = pkg[0]['location']

			if(location):
				formatUrl = location + '/' + ('/'.join(segments[1:len(segments)]))
				
			if(len(baseUrl) > 0):
				formatUrl = baseUrl + formatUrl

			if(len(projectPath) > 0):
				formatUrl = projectPath + formatUrl

			# print formatUrl
			# return formatUrl;

		else:
			print 'not search project config, use default'
			formatUrl = projectPath + formatUrl

		print formatUrl
		return formatUrl + '.js'
	def getRealUrl(self, url, setting):
		print ''

