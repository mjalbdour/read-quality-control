# FASTQ_FILE_NAME = "example.fastq"
# FASTQ_FILE_NAME = "SRR16506265_1.fastq"

MSG_READS = "Reads in the file ="
MSG_LENGTH = "\twith length"
MSG_AVERAGE = "Reads sequence average length ="
MSG_REPEATS = "Repeats ="
MSG_GC_CONTENT = "GC content average ="

readings = dict()
reads_repeats = dict()
sum_avg_gc_content = 0
repeats = 0
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
    if reading not in reads_repeats:
        reads_repeats[reading] = 0
    else:
        reads_repeats[reading] += 1
        repeats += 1

    gc_content = 0
    for n in line:
        if n in {'G', 'C'}:
            gc_content += 1
    sum_avg_gc_content += gc_content / k

file.close()

reads = 0
sum_reads = 0
for k, v in readings.items():
    reads += v
    sum_reads += k * v

avg_read_len = round(sum_reads / reads)
avg_gc_content = round(sum_avg_gc_content / reads * 100, 2)


# print(f'{MSG_READS} {reads}:')
# for k in sorted(readings.keys()):
#     print(f'{MSG_LENGTH} {k} = {readings[k]}')
#

print(f'{MSG_READS} {reads}')
print(f'{MSG_AVERAGE} {avg_read_len}')
print(f'\n{MSG_REPEATS} {repeats}')
print(f'\n{MSG_GC_CONTENT} {avg_gc_content}%')
