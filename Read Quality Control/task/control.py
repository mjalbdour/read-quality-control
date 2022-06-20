import gzip


class FASTQData:
    def __init__(self, reads=None, total_reads=0, avg_read_len=0, repeats=0, reads_ns=0, avg_gc_content=0, ns_per_seq=0):
        if reads is None:
            reads = dict()
        self.reads = reads
        self.total_reads = total_reads
        self.avg_read_len = avg_read_len
        self.repeats = repeats
        self.reads_ns = reads_ns
        self.avg_gc_content = avg_gc_content
        self.ns_per_seq = ns_per_seq


class FASTQDataAnalyzer:
    @staticmethod
    def read_archive(archive):
        file = gzip.open(archive, mode="rt")
        lines = file.readlines()
        file.close()
        return lines

    @staticmethod
    def analyze_archive(archive):
        lines = FASTQDataAnalyzer.read_archive(archive)
        data = FASTQData()
        sum_avg_ns = 0
        sum_avg_gc_content = 0
        for line in lines[1::4]:
            reading = line.rstrip("\n")
            k = len(reading)
            if k not in data.reads:
                data.reads[k] = 1
            else:
                data.reads[k] += 1

            gc_content = 0
            ns = 0
            for n in line:
                if n in {'G', 'C'}:
                    gc_content += 1
                elif n == "N":
                    ns += 1
            if ns > 0:
                data.reads_ns += 1
                sum_avg_ns += ns / k

            sum_avg_gc_content += gc_content / k

        sum_reads = 0
        for k, v in data.reads.items():
            data.total_reads += v
            sum_reads += k * v

        data.avg_read_len = round(sum_reads / data.total_reads)
        data.avg_gc_content = round(sum_avg_gc_content / data.total_reads * 100, 2)
        data.ns_per_seq = round(sum_avg_ns / data.total_reads * 100, 2)
        return data

    @staticmethod
    def find_best_data(d1, d2, d3):
        if d1.repeats + d1.reads_ns < d2.repeats + d2.reads_ns:
            if d1.repeats + d1.reads_ns < d3.repeats + d3.reads_ns:
                return d1
            else:
                return d3
        else:
            return d2

    @staticmethod
    def print_analysis(data):
        print(f'{MSG_READS} {data.total_reads}')
        print(f'{MSG_AVERAGE} {data.avg_read_len}')

        print(f'\n{MSG_REPEATS} {data.repeats}')
        print(f'{MSG_NS_READS} {data.reads_ns}')

        print(f'\n{MSG_GC_CONTENT} {data.avg_gc_content}%')
        print(f'{MSG_NS} {data.ns_per_seq}%')


# MESSAGES
MSG_READS = "Reads in the file ="
MSG_LENGTH = "\twith length"
MSG_AVERAGE = "Reads sequence average length ="
MSG_REPEATS = "Repeats ="
MSG_GC_CONTENT = "GC content average ="
MSG_NS_READS = "Reads with Ns ="
MSG_NS = "Ns per read sequence ="

# ARCHIVES
DATA_1 = "data1.gz"
DATA_2 = "data2.gz"
DATA_3 = "data3.gz"


# archives = [DATA_1, DATA_2, DATA_3]
archives = [input(), input(), input()]

data1, data2, data3 = [FASTQDataAnalyzer.analyze_archive(a) for a in archives]

FASTQDataAnalyzer.print_analysis(FASTQDataAnalyzer.find_best_data(data1, data2, data3))
