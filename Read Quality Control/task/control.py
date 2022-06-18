# FASTQ_FILE_NAME = "example.fastq"

FASTQ_FILE_NAME = input()
file = open(FASTQ_FILE_NAME, 'rt')
lines = file.readlines()
for line in lines[:4]:
    print(line, end='')
file.close()
