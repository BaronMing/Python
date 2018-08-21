from threading import Thread

"""
# 使用方法：
- 1.创建线程管理对象
	```
	threads = ThreadsManager()
	```
- 2.使用线程管理对象装饰要作为线程运行时的函数
	```
	@threads()
	def func1():
		pass
		
	@threads()
	def func2():
		pass
	```
- 3.线程启动
	- 第一种方法：
		```
		func1()
		func2()
		threads.start()
		```
		启动threads内的所有线程
	
	- 第二种方法:
		```
		threads.start = {
			func1(),
			func2()
		}
		```
		启动threads内的所有线程
		
	- 第三种方法:
		```
		func1()
		func2()
		```
		运行函数即等于启动线程

"""


class ThreadsManager:
	def __init__(self, immediately=True):
		self.threads = set()
		self.immediately = immediately
	
	def __call__(self, name=None, daemon=None):
		def fn_wrapper(fn):
			def args_wrapper(*args, **kwargs):
				thread = Thread(target=fn, name=name, args=args, kwargs=kwargs, daemon=daemon)
				
				if self.immediately:
					thread.start()
				else:
					self.threads.add(thread)
				
				return thread
			
			return args_wrapper
		
		return fn_wrapper
	
	def __start(self):
		return [thread.start for thread in self.threads]
	
	@property
	def start(self):
		if self.threads:
			def wrapper():
				self.__start()
			
			return wrapper
		else:
			raise Exception('必须先调用进程函数')
	
	@start.setter
	def start(self, _set):
		if not _set:
			raise TypeError('必须传入有效参数')
		elif _set == self.threads:
			self.__start()
		else:
			raise TypeError('类型为%s，要求参数类型为"集合"' % type(_set))
