import random
class Noise:
	def __init__(self):
		self.alpha = list("qwertyuiopasdfghjklzxcvbnm")
	def encode(self, string):
		const = []
		for s in list(string):
			sin = random.randint(0, 4)
			for i in range(5):
				if i == sin:
					const.append(s)
				else:
					cap = random.randint(0, 2)
					if cap == 0:
						const.append(random.choice(self.alpha))
					else:
						const.append((random.choice(self.alpha)).upper())
			const.append(str(sin))
		return "".join(const)

	def decode(self, string: str) -> str:
		table = []
		for c in string:
			try:
				ic = int(c)
			except:
				continue
			else:
				table.append(ic)
		for i in range(6):
			string = string.replace(str(i), "|")
		broken_string = string.split("|")
		broken_string.pop((len(broken_string)-1))
		const = []
		counter = 0
		for segment in broken_string:
			const.append(segment[table[counter]])
			counter += 1
		return "".join(const)
