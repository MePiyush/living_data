import csv
import sys

def merge_headers(headers_file1, headers_file2):
	matched_headers_file2 = []
	global new_headers

	for attributes1 in headers_file1:
		print '\nPlease select corresponding Attribute Number for <' + attributes1 + '> from:'
		for index, attributes2 in enumerate(headers_file2):
			print index, attributes2
		choice = raw_input('Enter Your Choice, write None if nothing matches:')
		while(1):	
			if choice.lower() == 'none':
				matched_headers_file2.append('None')
				header_name = raw_input('Enter New Name for ' + attributes1 + ': ')
				new_headers.append(header_name)
				break
			else:
				try:
					val = int(choice)
					if (int(choice) in range(len(headers_file2))):
						matched_headers_file2.append(headers_file2[int(choice)])
						header_name = raw_input('Enter New Name for ' + attributes1 + ' & ' + headers_file2[int(choice)] + ': ')
						new_headers.append(header_name)

						headers_file2.remove(headers_file2[int(choice)])
						break
				except ValueError:
					choice = raw_input('Wrong Choice, Please Enter Your Again: ')

	for attributes2 in headers_file2:
		header_name = raw_input('Enter New Name for ' + attributes2 + ': ')
		new_headers.append(header_name)

	matched_headers_file2 = matched_headers_file2 + headers_file2 	

	global merged_headers
	merged_headers = map(None, headers_file1, matched_headers_file2)
	
file1 = open(sys.argv[1], 'rb')
file2 = open(sys.argv[2], 'rb')

merged_headers = []
new_headers = []
none_pos = []

try:
	reader_file1 = csv.reader(file1)
	headers_file1 = reader_file1.next()
	headers_file1_copy = list(headers_file1)
	no_of_attributes_file1 = len(headers_file1)

	reader_file2 = csv.reader(file2)
	headers_file2 = reader_file2.next()
	headers_file2_copy = list(headers_file2)
	no_of_attributes_file2 = len(headers_file2)

	print '\nHeaders for First file are: ' + str(headers_file1)
	print '\nHeaders for Second file are: ' + str(headers_file2)

	merge_headers(headers_file2_copy, headers_file1_copy) if (no_of_attributes_file1>no_of_attributes_file2) else merge_headers(headers_file1_copy, headers_file2_copy)
	print '\nMerged Headers are: ' + str(merged_headers)
	print '\nNew Headers are: ' + str(new_headers)

	merged_file = open('Merged.csv', 'wb')
	writer_merged_file = csv.writer(merged_file)
	writer_merged_file.writerow(new_headers)

	for index in range(len(merged_headers)):
		if (merged_headers[index][1] == 'None'):
			none_pos.append(index)

	if (no_of_attributes_file1>no_of_attributes_file2):
		for row in reader_file2:
			writer_merged_file.writerow(row)
		for row in reader_file1:
			for none_item in range(len(none_pos)):
				row.insert(none_pos[none_item], '')
			writer_merged_file.writerow(row)	
	else:
		for row in reader_file1:
			writer_merged_file.writerow(row)
		for row in reader_file2:
			for none_item in range(len(none_pos)):
				row.insert(none_pos[none_item], '')
			writer_merged_file.writerow(row)

finally:
	file1.close()
	file2.close()
	merged_file.close()

