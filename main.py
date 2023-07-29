import re

def get_equations(file_name: str = "equations.txt") -> str:
	with open(file_name) as fl:
		equations = fl.read()

	return equations

def get_coefficients(equations: str) -> list:
	"""Gets the coefficients"""
	# input  # "a1x + b1y = s1\na2x + b2y = s2"
	# output # [a1, b1, s1, a2, b2, s2]
	#           0   1   2   3   4   5

	c = re.findall(r"\d{1,}", equations)
	return [int(_) for _ in c]

def get_solution(c: list):
	"""c - coefficients
	returns solution [x, y] or 'Infinite solutions'"""

	sys_det = (c[0]*c[4]) - (c[3]*c[1])

	x_det = (c[2]*c[4]) - (c[5]*c[1])
	y_det = (c[0]*c[5]) - (c[3]*c[2])

	if sys_det == 0:
		return "Infinite solutions or no solutions or it is very simple"
	else:
		x = x_det / sys_det
		y = y_det / sys_det

		return [x, y]

def main():
	eq = get_equations()
	c = get_coefficients(eq)
	print(get_solution(c))

if __name__ == "__main__":
	main()
