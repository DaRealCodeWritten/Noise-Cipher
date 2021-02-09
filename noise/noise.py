#pylint:disable=R0914
if __name__ == "__main__":
	import random
	import charsets
	import warnings
	import errors
else:
	import random
	import warnings
	from noise import charsets
	from noise import errors
class Noise:
	def __init__(self):
		self.fallback = {
		"charset": charsets.charset_alpha(),
		"stringlen": 4,
		"segmentsep": "table"
		}
		self.settings = {}
	def set_settings(self, settings: dict) -> None:
		if isinstance(settings, dict):
			self.settings = settings
		else:
			raise TypeError("set_settings takes a dict, not {}".format(type(settings)))
		string = settings.get("stringlen")
		if string is not None:
			if string > 27:
				warnings.warn("The value of 'stringlen' shouldn't exceed 27, anything higher may cause errors")
	def encode(self, string) -> str:
		const = []
		charset = self.settings.get("charset")
		if charset is None:
			charset = self.fallback.get("charset")
		stringlen = self.settings.get("stringlen")
		if stringlen is None:
			stringlen = self.fallback.get("stringlen")
		for s in list(string):
			sin = random.randint(0, (stringlen-1))
			for i in range(stringlen):
				if i == sin:
					const.append(s)
				else:
					cap = random.randint(0, 2)
					if (cap == 0):
						const.append(random.choice(charset))
					elif (cap != 0):
						up = random.choice(charset)
						if up.isalpha():
							const.append(up.upper())
						else:
							const.append(up)
			const.append(str(sin))
		return "".join(const)

	def decode(self, string: str) -> str:
		stringlen = self.settings.get("stringlen")
		if stringlen is None:
			stringlen = self.fallback.get("stringlen")
		table = []
		last_int = False
		subtable = []
		for c in string:
			if last_int and c.isnumeric():
				subtable.append(str(c))
			if c.isnumeric():
				last_int = True
				subtable.append(str(c))
			if not c.isnumeric() and last_int:
				last_int = False
				try:
					subtable.pop(2)
				except IndexError:
					pass
				sub = "".join(subtable)
				string.replace(sub, "0")
				sub = int(sub)
				table.append(sub)
				subtable = []
		if string[len(string)-1].isnumeric() and string[len(string)-2].isnumeric():
			conc = string[len(string)-2]+string[len(string)-1]
			table.append(int(conc))
		elif string[len(string)-1].isnumeric():
			table.append(int(string[len(string)-1]))
		for i in range(stringlen):
		    string = string.replace(str(i), "|")
		broken_string = string.split("|")
		broken_string.pop((len(broken_string)-1))
		for m in broken_string:
			if m in (" ", ""):
				broken_string.pop(broken_string.index(m))
		const = []
		counter = 0
		for segment in broken_string:
			tbl = table[counter]
			sgmt = segment[tbl]
			const.append(sgmt)
			counter += 1
		return "".join(const)
	
	def decode_to(self, string: str, stream):
		ret = self.decode(string)
		try:
			stream.write(ret)
		except AttributeError as e:
			err = "The 'stream' arg must support .write(), but the stream you supplied does not"
			raise errors.NotSupported(err) from e
		return stream
	
	def encode_to(self, string: str, stream):
		ret = self.encode(string)
		try:
			stream.write(ret)
		except AttributeError as e:
			err = "The 'stream' arg must support .write(), but the stream you supplied does not"
			raise errors.NotSupported(err) from e
		return stream