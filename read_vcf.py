import argparse

def parse_vcf(vcf_file, query_depth):
    zygosity_count = {'0/0': 0, '0/1': 0, '1/0': 0, '1/1': 0}
    with open(vcf_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#'):
                continue  # Skip header lines
            fields = line.split('\t')
            sample = fields[11]
            info = fields[7]
            format_field = fields[8]
            format_values = fields[9:]
            info_fields = info.split(';')
            depth = None
            for field in info_fields:
                if field.startswith('DP='):
                    depth = int(field.split('=')[1])
                    break
            if depth is None or depth <= query_depth:
                continue
            format_index = format_field.split(':').index('GT')
            for value in format_values:
                genotype = value.split(':')[format_index]
                if genotype in zygosity_count:
                    zygosity_count[genotype] += 1
    return zygosity_count

def main():
    parser = argparse.ArgumentParser(description='VCF Parser')
    parser.add_argument('vcf_file', help='Path to the VCF file')
    parser.add_argument('--depth', type=int, default=10, help='Minimum depth threshold (default: 10)')
    args = parser.parse_args()
    zygosity_count = parse_vcf(args.vcf_file, args.depth)
    print(f"Zygosity breakdown for {sum(zygosity_count.values())} variants with depth > {args.depth}:")
    for genotype, count in zygosity_count.items():
        print(f"{genotype}: {count}")

if __name__ == '__main__':
    main()
