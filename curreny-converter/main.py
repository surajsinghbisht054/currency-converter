#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#	
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Import Module
try:
	import Tkinter
	import ttk
except:
	import tkinter as Tkinter
	import tkinter.ttk as ttk

# Creating Main Class
class converter(Tkinter.Tk):
	def __init__(self, *args, **kwargs):
		Tkinter.Tk.__init__(self, *args, **kwargs)
		self['padx']=50
		self['pady']=50
		self['bg']="powder blue"
		self.create_variable_stores()
		self.create_dashboard()
		self.create_conversion_mechanizism()

	# Event Function
	def convert_base_to_currency(self, *args, **kwargs):
		try:
			obj = self.converting_currency.get() * self.Currency_rates.get()
			self.converted_currency.set(obj)
		except:
			pass
		return

	# Creating Main Conversion Mechanizm
	def create_conversion_mechanizism(self):
		ttk.Entry(self, textvariable=self.converting_currency, font=("arial 30 bold")).grid(row=4, column=1)
		ttk.Entry(self, textvariable=self.converted_currency, font=("arial 30 bold")).grid(row=4, column=3)
		return

	# Creating Main DashBoard
	def create_dashboard(self):
		ttk.Label(self, text=" Base Currency ", font=("arial 30 bold")).grid(row=1, column=1, padx=10, pady=10)
		ttk.Separator(self, orient="vertical").grid(row=1, column=2,sticky="ns", padx=10, pady=10)
		ttk.Label(self, text=" Currency ", font=("arial 30 bold")).grid(row=1, column=3, padx=10, pady=10)
		ttk.Label(self, text=" $ 1  = ", font=("arial 30 bold")).grid(row=2, column=1, padx=10, pady=10)
		ttk.Entry(self, textvariable=self.Currency_rates, font=("arial 30 bold")).grid(row=2, column=3, padx=10, pady=10)
		return

	# Creating Variables
	def create_variable_stores(self):
		self.Currency_rates = Tkinter.DoubleVar()
		self.converted_currency = Tkinter.DoubleVar()
		self.converting_currency = Tkinter.DoubleVar()
		# Adding Auto Trace Variable Event
		self.converting_currency.trace_variable("w", self.convert_base_to_currency)
		

# Main Function
def main():
	root = converter(className = " Simple Currency Converter")
	root.mainloop()
	return

# Main Trigger
if __name__ == '__main__':
	main()