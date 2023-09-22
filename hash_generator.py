'''Reads input.txt line by line and outputs hashes for each of the lines to a file for
MD-5, SHA-256, and SHA-512.
'''
import hashlib
def main():
    '''
    '''
    linesIn = ""
    lines = []
    md5_lines_out = []
    sha256_lines_out = []
    sha512_lines_out = []
    #Reads the lines into a temporary input list.
    #UTF-16 encoding is used for the default windows txt file format.
    with open('input.txt', encoding='utf-16') as f:
        linesIn = [line for line in f]

    #Removes the newlines from the list and strips them from the end of the strings
    #for processing.
    for line in linesIn:
        if line != '\n':
            lines.append(line.rstrip())
    f.close()

    #Creates the lists of hashes to output to files
    for line in lines:
        md5_lines_out.append(hashlib.md5(line.encode()).hexdigest() + "\n")
        sha256_lines_out.append(hashlib.sha256(line.encode()).hexdigest() + "\n")
        sha512_lines_out.append(hashlib.sha512(line.encode()).hexdigest() + "\n")

    #outputs the lists of hashes to the corresponding files
    with open('md5_output.txt', 'w') as f:
        f.writelines(md5_lines_out)
    f.close()
    with open('sha256_output.txt', 'w') as f:
        f.writelines(sha256_lines_out)
    f.close()
    with open('sha512_output.txt', 'w') as f:
        f.writelines(sha512_lines_out)
    f.close()
main()
