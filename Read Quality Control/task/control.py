# FASTQ_FILE_NAME = "example.fastq"

MSG_READS = "Reads in the file ="
MSG_LENGTH = "\twith length"
MSG_AVERAGE = "Reads sequence average length ="

readings = dict()

FASTQ_FILE_NAME = input()
file = open(FASTQ_FILE_NAME, 'rt')
lines = file.readlines()
for line in lines[1::4]:
    reading = line.rstrip("\n")
    k = len(reading)
    if k not in readings:
        readings[k] = 1
    else:
        readings[k] += 1
file.close()

readings_occurrences = 0
total_sum = 0
for k, v in readings.items():
    readings_occurrences += v
    total_sum += k * v

average_len = round(total_sum / readings_occurrences)

print(f'{MSG_READS} {readings_occurrences}:')
for k in sorted(readings.keys()):
    print(f'{MSG_LENGTH} {k} = {readings[k]}')

print(f'{MSG_AVERAGE} {average_len}')
