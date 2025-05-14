import re


text = """
# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
"""


def duplicate_labels(file):
	FILTER_PATTERN = re.compile(r"(#.*?$)|(\"{3}.*?\"{3})|('{3}.*?'{3})", flags=re.DOTALL | re.IGNORECASE | re.MULTILINE)

	lines = file.splitlines()
	parsed_data = {'code': [], 'label': []}

	label = []
	code = []
	i = 0
	next_label_exists = True

	while i < len(lines):
		# Keep capturing while complexity comments are present
		while i < len(lines) and re.search(r"#.*\sO\(", lines[i]):
			label.append(lines[i])
			i += 1

		# Add the label only once before a solution is added
		if label and len(parsed_data['label']) - len(parsed_data['code']) < 1:
			parsed_data['label'].append('\n'.join(label))
		
		# Check if it's the definition of solution
		if i < len(lines) and re.search(r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE):

			# Keep consuming until a label from the next solution is hit
			while i < len(lines) and not re.search(r"#.*\sO\(", lines[i]):
				code.append(lines[i])
				next_label_exists = True
				i += 1

				# If no next label was found (from the next solution)
				if i < len(lines) and re.search(r"(?:class|def)\sSolution", lines[i], flags=re.IGNORECASE):
					next_label_exists = False
					# New solution was found, break out of the loop
					break

			# Add the code snippet
			solution = re.sub(FILTER_PATTERN, "", '\n'.join(code))
			parsed_data['code'].append(solution)

			# If there was no label at the beginning, add a placeholder
			if len(parsed_data['code']) > len(parsed_data['label']):
				parsed_data['label'].append('')
			
			# Reset the current label only if the next one exists, else keep it for further borrowing 
			if next_label_exists:
				label = []

			# Reset the current label and code snippet
			code = []

			# Rewind one step back to account for the main iteration
			i -= 1

		# Next line
		i += 1

	# Make sure we have the same number of solutions as labels
	assert len(parsed_data['label']) == len(parsed_data['code'])
	
	return parsed_data


if __name__ == "__main__":
	parsed_data = duplicate_labels(text)
	print(parsed_data)

	# Inspect
	for i, (code, label) in enumerate(zip(parsed_data['code'], parsed_data['label'])):
		print(f"Sample #{i+1}:\nLabel:\n{label}\nCode:\n{code}\n", end='\n\n')